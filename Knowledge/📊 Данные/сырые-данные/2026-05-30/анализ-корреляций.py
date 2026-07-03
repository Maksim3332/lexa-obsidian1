#!/usr/bin/env python3
"""Анализ корреляций между объёмом, ценой и социальной активностью мемкоинов Solana."""

import csv, json, sqlite3, os, sys
from datetime import datetime
from pathlib import Path

# ============================================================
# Конфигурация
# ============================================================
RAW_DIR = Path("/root/lexa-knowledge/сырые-данные/2026-05-30")
CSV_PATH = RAW_DIR / "сводка.csv"
DB_PATH = RAW_DIR / "анализ.db"
REPORT_DIR = Path("/root/lexa-obsidian/знания/ежедневные-отчёты/2026-05-30")

os.makedirs(REPORT_DIR, exist_ok=True)

# Социальный порог: если у токена есть Twitter/X — считаем, что есть соц.активность
# Более точный анализ потребовал бы данных о количестве упоминаний, тональности, виральности

# ============================================================
# 1. Загрузка данных
# ============================================================
def load_data():
    tokens = []
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            row['market_cap'] = float(row['market_cap'])
            row['volume_24h'] = float(row['volume_24h'])
            row['price_change_24h'] = float(row['price_change_24h'])
            row['holder_count'] = int(row['holder_count'])
            row['smart_degen'] = int(row['smart_degen'])
            row['renowned_count'] = int(row['renowned_count'])
            row['liquidity'] = float(row['liquidity'])
            row['rug_ratio'] = float(row['rug_ratio'])
            row['has_social'] = bool(row.get('twitter', '').strip())
            tokens.append(row)
    return tokens

# ============================================================
# 2. Анализ корреляций
# ============================================================
def analyze_correlations(tokens):
    n = len(tokens)
    if n < 2:
        return {"error": "Недостаточно данных для корреляционного анализа"}

    volumes = [t['volume_24h'] for t in tokens]
    changes = [t['price_change_24h'] for t in tokens]
    holders = [t['holder_count'] for t in tokens]
    smart_degen = [t['smart_degen'] for t in tokens]
    liquidity = [t['liquidity'] for t in tokens]

    def pearson(x, y):
        """Коэффициент корреляции Пирсона."""
        n = len(x)
        if n < 2: return 0
        mx, my = sum(x)/n, sum(y)/n
        num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
        den = (sum((x[i]-mx)**2 for i in range(n)) * sum((y[i]-my)**2 for i in range(n))) ** 0.5
        return num / den if den != 0 else 0

    correlations = {
        "объём_↔_изменение_цены": {
            "коэффициент": round(pearson(volumes, changes), 4),
            "интерпретация": ""
        },
        "объём_↔_количество_холдеров": {
            "коэффициент": round(pearson(volumes, holders), 4),
            "интерпретация": ""
        },
        "изменение_цены_↔_холдеры": {
            "коэффициент": round(pearson(changes, holders), 4),
            "интерпретация": ""
        },
        "smart_degen_↔_объём": {
            "коэффициент": round(pearson(smart_degen, volumes), 4),
            "интерпретация": ""
        },
        "ликвидность_↔_объём": {
            "коэффициент": round(pearson(liquidity, volumes), 4),
            "интерпретация": ""
        },
    }

    # Интерпретации
    for key, val in correlations.items():
        r = val['коэффициент']
        if abs(r) < 0.1:
            val['интерпретация'] = "Связь отсутствует"
        elif abs(r) < 0.3:
            val['интерпретация'] = "Слабая связь"
        elif abs(r) < 0.5:
            val['интерпретация'] = "Умеренная связь"
        elif abs(r) < 0.7:
            val['интерпретация'] = "Заметная связь"
        else:
            val['интерпретация'] = "Сильная связь"
        val['направление'] = "положительная" if r > 0 else "отрицательная"

    # Определение природы пампа
    results = []
    for t in tokens:
        entry = {
            "символ": t['symbol'],
            "цена": t['price'],
            "mc": t['market_cap'],
            "объём_24ч": t['volume_24h'],
            "изменение_24ч": t['price_change_24h'],
            "холдеры": t['holder_count'],
            "smart_degen": t['smart_degen'],
            "ликвидность": t['liquidity'],
            "есть_соцсети": t['has_social'],
            "статус_создателя": t['creator_status'],
            "платформа": t.get('platform', ''),
        }

        # Классификация типа движения
        # Социальный памп: есть соцсети + рост цены + рост объёма + smart money
        # Органический рост: без соцсетей, но рост за счёт реального объёма
        # Искусственный: низкая ликвидность, нет smart money, подозрительно высокий объём

        vol_per_liq = t['volume_24h'] / t['liquidity'] if t['liquidity'] > 0 else float('inf')
        has_smart_money = t['smart_degen'] >= 3 or t['renowned_count'] >= 1

        if t['price_change_24h'] > 100 and t['has_social'] and has_smart_money:
            entry['тип_движения'] = "📱 Социальный памп"
            entry['обоснование'] = f"Рост +{t['price_change_24h']:.0f}%, есть соцсети, есть smart money ({t['smart_degen']})"
        elif t['price_change_24h'] > 100 and has_smart_money:
            entry['тип_движения'] = "📊 Органический рост (smart money)"
            entry['обоснование'] = f"Рост +{t['price_change_24h']:.0f}%, smart money {t['smart_degen']}, соцсетей нет"
        elif t['price_change_24h'] > 100 and not t['has_social'] and vol_per_liq > 50:
            entry['тип_движения'] = "⚠️ Подозрительный (возможно накрутка)"
            entry['обоснование'] = f"Рост +{t['price_change_24h']:.0f}%, объём/ликвидность {vol_per_liq:.0f}×, нет smart money"
        elif t['price_change_24h'] > 50:
            entry['тип_движения'] = "🟡 Умеренный рост"
            entry['обоснование'] = f"Рост +{t['price_change_24h']:.0f}%, требует дальнейшего анализа"
        elif t['price_change_24h'] < -10:
            entry['тип_движения'] = "🔴 Падение"
            entry['обоснование'] = f"Падение {t['price_change_24h']:.1f}%"
        else:
            entry['тип_движения'] = "➡️ Флэт / боковик"
            entry['обоснование'] = f"Изменение {t['price_change_24h']:.1f}%"

        results.append(entry)

    return {
        "корреляции": correlations,
        "токены": results,
        "мета": {
            "всего_токенов": n,
            "токенов_с_ростом": sum(1 for t in tokens if t['price_change_24h'] > 100),
            "токенов_с_падением": sum(1 for t in tokens if t['price_change_24h'] < -10),
            "токенов_со_smart_money": sum(1 for t in tokens if t['smart_degen'] >= 3),
            "токенов_с_соцсетями": sum(1 for t in tokens if t['has_social']),
            "средний_объём": round(sum(volumes)/n),
            "среднее_изменение_цены": round(sum(changes)/n, 1),
        }
    }

# ============================================================
# 3. Сохранение в SQLite
# ============================================================
def save_to_sqlite(analysis, tokens_raw):
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    # Таблица корреляций
    c.execute('''
        CREATE TABLE IF NOT EXISTS корреляции (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            пара TEXT NOT NULL,
            коэффициент REAL NOT NULL,
            интерпретация TEXT,
            направление TEXT
        )
    ''')

    for key, val in analysis['корреляции'].items():
        c.execute(
            'INSERT INTO корреляции (пара, коэффициент, интерпретация, направление) VALUES (?, ?, ?, ?)',
            (key, val['коэффициент'], val['интерпретация'], val['направление'])
        )

    # Таблица токенов
    c.execute('''
        CREATE TABLE IF NOT EXISTS токены (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            символ TEXT NOT NULL,
            цена REAL,
            mc REAL,
            объём_24ч REAL,
            изменение_24ч REAL,
            холдеры INTEGER,
            smart_degen INTEGER,
            ликвидность REAL,
            есть_соцсети INTEGER,
            статус_создателя TEXT,
            тип_движения TEXT,
            обоснование TEXT,
            платформа TEXT
        )
    ''')

    for t in analysis['токены']:
        c.execute(
            '''INSERT INTO токены 
            (символ, цена, mc, объём_24ч, изменение_24ч, холдеры, smart_degen, ликвидность, есть_соцсети, статус_создателя, тип_движения, обоснование, платформа)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (t['символ'], t['цена'], t['mc'], t['объём_24ч'], t['изменение_24ч'],
             t['холдеры'], t['smart_degen'], t['ликвидность'], int(t['есть_соцсети']),
             t['статус_создателя'], t['тип_движения'], t['обоснование'], t['платформа'])
        )

    # Таблица мета-данных
    c.execute('''
        CREATE TABLE IF NOT EXISTS мета (
            ключ TEXT PRIMARY KEY,
            значение TEXT
        )
    ''')

    meta = analysis['мета']
    for key, val in meta.items():
        c.execute('INSERT OR REPLACE INTO мета (ключ, значение) VALUES (?, ?)',
                  (key, str(val)))

    conn.commit()
    conn.close()

    print(f"✅ SQLite база сохранена: {DB_PATH}")
    print(f"   Таблицы: корреляции ({len(analysis['корреляции'])} записей), "
          f"токены ({len(analysis['токены'])} записей), мета ({len(meta)} записей)")

# ============================================================
# 4. Сохранение JSON отчёта
# ============================================================
def save_report_json(analysis):
    report_path = RAW_DIR / "анализ.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON отчёт сохранён: {report_path}")

# ============================================================
# 5. Генерация Markdown отчёта для Obsidian
# ============================================================
def save_markdown_report(analysis):
    report_path = REPORT_DIR / "карта-рынка.md"
    meta = analysis['мета']

    lines = []
    lines.append("---")
    lines.append("дата: 2026-05-30")
    lines.append("тип: карта-рынка")
    lines.append("режим: анализ")
    lines.append("---")
    lines.append("")
    lines.append(f"# 🗺️ Карта рынка — 30 мая 2026")
    lines.append("")
    lines.append("Анализ топ-10 мемкоинов Solana за последние 24 часа.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📊 Общая статистика")
    lines.append("")
    lines.append(f"- **Всего проанализировано:** {meta['всего_токенов']} токенов")
    lines.append(f"- **Средний объём 24ч:** ${meta['средний_объём']:,.0f}")
    lines.append(f"- **Среднее изменение цены:** {meta['среднее_изменение_цены']:+.1f}%")
    lines.append(f"- **Токенов с ростом >100%:** {meta['токенов_с_ростом']}")
    lines.append(f"- **Токенов с падением:** {meta['токенов_с_падением']}")
    lines.append(f"- **Токенов со smart money:** {meta['токенов_со_smart_money']}")
    lines.append(f"- **Токенов с соцсетями:** {meta['токенов_с_соцсетями']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📈 Корреляции")
    lines.append("")
    lines.append("| Пара | Коэффициент | Интерпретация |")
    lines.append("|------|-------------|---------------|")

    for key, val in analysis['корреляции'].items():
        label = key.replace('_', ' ').replace('↔', '↔').strip()
        lines.append(f"| {label} | {val['коэффициент']} | {val['интерпретация']}, {val['направление']} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🪙 Детальный анализ токенов")
    lines.append("")
    lines.append("| # | Символ | Тип движения | Цена | MC | Vol 24h | Δ24h | Холдеры | Smart |")
    lines.append("|---|--------|-------------|------|------|---------|------|---------|-------|")

    for i, t in enumerate(analysis['токены'], 1):
        smart_str = f"{t['smart_degen']}" if t['smart_degen'] > 0 else "—"
        lines.append(
            f"| {i} | ${t['символ']} | {t['тип_движения']} | "
            f"${t['цена']:.8f} | ${t['mc']:,.0f} | ${t['объём_24ч']:,.0f} | "
            f"{t['изменение_24ч']:+.1f}% | {t['холдеры']} | {smart_str} |"
        )

    lines.append("")
    lines.append("### Обоснование")
    lines.append("")
    for t in analysis['токены']:
        lines.append(f"- **${t['символ']}**: {t['тип_движения']} — {t['обоснование']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🏆 Топ-3 с наибольшим потенциалом роста")
    lines.append("")

    # Выбираем топ-3: исключаем подозрительные и упавшие, сортируем по smart money + рост + объём
    candidates = [t for t in analysis['токены'] if 'Подозрительный' not in t['тип_движения'] and 'Падение' not in t['тип_движения']]
    candidates.sort(key=lambda t: (t['smart_degen'], t['объём_24ч']), reverse=True)

    if candidates:
        for i, t in enumerate(candidates[:3], 1):
            lines.append(f"### {i}. ${t['символ']}")
            lines.append(f"- **Тип движения:** {t['тип_движения']}")
            lines.append(f"- **MC:** ${t['mc']:,.0f} | **Vol 24h:** ${t['объём_24ч']:,.0f} | **Δ24h:** {t['изменение_24ч']:+.1f}%")
            lines.append(f"- **Smart money:** {t['smart_degen']} | **Холдеров:** {t['холдеры']}")
            lines.append(f"- **Обоснование:** {t['обоснование']}")
            lines.append("")
    else:
        lines.append("Нет кандидатов для топ-3. Рынок нестабилен.")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## ⚠️ Риски")
    lines.append("")
    lines.append(f"- **{meta['токенов_со_smart_money']} из {meta['всего_токенов']}** токенов имеют smart money — рынок в основном retail")
    lines.append(f"- Большинство создателей уже вышли (creator_close) — возможен dumping")
    lines.append(f"- Единственный Pump.fun токен (CUM) всё ещё держит создатель — риск rug pull")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Создано: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    lines.append(f"*Данные: GMGN API, DexScreener*")
    lines.append(f"*[[дашборды|📊 Дашборды Grafana]]*")

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"✅ Markdown отчёт сохранён: {report_path}")

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print(f"📊 Загрузка данных из {CSV_PATH}...")
    tokens = load_data()
    print(f"   Загружено {len(tokens)} токенов")

    print(f"\n🔬 Анализ корреляций...")
    analysis = analyze_correlations(tokens)

    print(f"\n   Корреляции:")
    for key, val in analysis['корреляции'].items():
        label = key.replace('_', ' ')
        print(f"   • {label}: r = {val['коэффициент']} ({val['интерпретация']}, {val['направление']})")

    meta = analysis['мета']
    print(f"\n   Мета:")
    for key, val in meta.items():
        print(f"   • {key}: {val}")

    print(f"\n💾 Сохранение результатов...")
    save_to_sqlite(analysis, tokens)
    save_report_json(analysis)
    save_markdown_report(analysis)

    print(f"\n✅ Анализ завершён успешно!")
    print(f"   CSV:     {CSV_PATH}")
    print(f"   SQLite:  {DB_PATH}")
    print(f"   JSON:    {RAW_DIR / 'анализ.json'}")
    print(f"   Markdown:{REPORT_DIR / 'карта-рынка.md'}")
