# ⚠️ ЖЁСТКИЙ ПРОТОКОЛ АНАЛИЗА ТОКЕНОВ v3
> MUST FOLLOW — каждый шаг обязателен. Пропуск шага = риск пропустить катализатор.
> **Bull/Bear дебаты + Reflection Log + Wallet Tracing + Social Depth**

## Преамбула: почему я ошибаюсь

| Причина | Симптом | Фикс |
|---------|---------|------|
| Смотрю на числа, а не на контекст | Пропускаю Twitter/KOL связи | Шаг 1 — СОЦСЕТИ (делать первым!) |
| Не кликаю ссылки | "twitter есть" ≠ прочитал | Каждую ссылку открыть или проверить |
| Параллельные запросы → теряю фокус | Забываю проверить важное | Протокол выполняется ПОСЛЕДОВАТЕЛЬНО |
| Нет принудительного порядка | Пропускаю шаги | Каждый шаг с check-box |
| JSON-поля кажутся полными | "chooserich/status/..." — не битая ссылка, а KOL! | Всегда гуглить/открывать handle |
| Только одна точка зрения | Упускаю Bear case или Bull case | **Bull/Bear дебаты перед вердиктом** |
| Не запоминаю что решил → что вышло | Повторяю одни ошибки | **Reflection Log после каждой сделки** |

---

## Протокол анализа (выполнять строго по порядку)

### Шаг 0: Базовая инфа (быстрый сбор)
- [ ] `token info` — symbol, name, price, MC, liq, holders, age
- [ ] `token security` — mint, freeze, tax, LP burn, top10 rate, rug_ratio
- [ ] `token pool` — DEX, liquidity depth, reserves
- [ ] **СКОРОСТНОЙ ФАКТ:** запущен <6h назад, OG/CTO флаг, HOT level

### ⚡ Шаг 1а: СОЦСЕТИ — ДЕЛАЙ ПЕРВЫМ (где я проигрывал)
- [ ] **Twitter — ОБЯЗАТЕЛЬНО открыть ссылку/прочитать:**
  ```bash
  # Если есть twitter_username — загуглить кто это, сколько подписчиков
  # Если это chooserich/status/... — ЭТО НЕ БИТАЯ ССЫЛКА, ЭТО КОНКРЕТНЫЙ ТВИТ KOL!
  # Проверить: username это аккаунт (@nick) или твит (nick/status/...)?
  ```
- [ ] **Social Graph Depth (НОВОЕ):**
  - [ ] Кто владелец аккаунта? Реальная персона или аноним?
  - [ ] Сколько подписчиков? (>10K = микро-KOL, >100K = KOL, >1M = альфа)
  - [ ] **Проскроллить последние 10 твитов** — о чём пишет? Есть ли твиты про токен?
  - [ ] **Реакции на твиты про токен** — сколько лайков? ретвитов? комментариев?
  - [ ] Кто комментирует? Другие KOL или боты?
  - [ ] Есть ли ответы от команды токена?
  - [ ] **Другие токены, которые этот аккаунт продвигал** — чем кончилось?
  - [ ] Website — что за сайт? Реальный проект или пустышка?
  - [ ] **Telegram** — открыть, сколько участников, активность, ссылка в описании TG?
- [ ] **Описание токена** — есть ли нарратив? Что обещают?

### Шаг 1б: Dev / Creator
- [ ] Dev кошелёк, статус (creator_hold/close)
- [ ] Сколько токенов создал
- [ ] ATH токен дева (его лучший проект)
- [ ] Fund from (откуда деньги на запуск)
- [ ] Есть ли серийность? (creator_open_count > 5)
- [ ] **Wallet Tracing (НОВОЕ):**
  - [ ] Dev wallet funded from? (CEX, другой кошелёк, fresh?)
  - [ ] Куда ушли токены dev? (переводы на другие кошельки, продажа)
  - [ ] Связанные кошельки dev (common funding source)
  - [ ] Есть ли cluster wallet (группа кошельков из одного источника)
  - [ ] Анализ первого трейда dev — паттерн поведения (тест LP, массовая закупка)

### Шаг 2: Рынок
- [ ] Price, MC, ATH, просадка от ATH
- [ ] 24h объём, 1h объём, тренд (растёт/падает)
- [ ] Buys vs Sells (соотношение)
- [ ] Цена 1m/5m/1h/6h/24h — динамика
- [ ] Hot level (0-3)
- [ ] Volume/MC ratio (>0.5 = активная торговля)

### Шаг 3: Холдеры
- [ ] Total holders (+ рост/падение за последние часы)
- [ ] Top 10 rate (безопасно <20%, ⚠️ 20-30%, 🚫 >30%)
- [ ] **Top 20 holders — детальный разбор:**
  - [ ] P&L каждого (кто в плюсе/минусе, насколько)
  - [ ] sell % каждого (0-100%, кто уже сливает)
  - [ ] Тип каждого (SM, KOL, bundler, fresh, CEX)
  - [ ] Взаимосвязи между топ-холдерами (одни и те же кошельки в других проектах?)
- [ ] Bundler rate, fresh wallet rate, bot rate
- [ ] Крупные держатели в плюсе или минусе?
- [ ] **Cluster analysis (НОВОЕ):** похожи ли топ-холдеры по времени создания, funding source, паттерну поведения?

### Шаг 4: Smart Money & KOLs
- [ ] SM count (сколько всего заходило)
- [ ] SM holders — сколько ещё держат, их P&L, sell %
- [ ] SM traders — buy/sell volume, кто сливает
- [ ] **SM Convergence Check (НОВОЕ):**
  - [ ] Есть ли свежие покупки от SM за последние 5/15/60 минут?
  - [ ] Сколько уникальных SM купило за последний час?
  - [ ] Добавился ли новый SM (не было раньше — появился сейчас)?
  - [ ] Общий объём SM покупок vs SM продаж (net flow)
  - [ ] Средний размер SM сделки (whale или мелкие позы)
- [ ] KOL count
- [ ] KOL holders — кто держит, P&L, sell %
- [ ] KOL traders — кто вышел, с каким P&L
- [ ] **КЛЮЧЕВОЙ СИГНАЛ:** KOL всё ещё держит? (RC, nyhrox и т.д.)
- [ ] **Топ-3 SM/KOL разобрать вручную:** адрес, когда зашёл, размер, P&L, активность в других токенах

### Шаг 5: Narrative Intelligence — анализ нарратива, юмора и виральности
> Полный разбор концепции токена: от культурного референса до вирального потенциала.
> Использует библиотеку нарративов (`narratives.md`) + x-intelligence для соц-доказательств.

#### 5a: Классификация нарратива
- [ ] **Категория нарратива** (из библиотеки):
  - Absurdist / NPC / Internet Culture / AI Meme / Celebrity Parody
  - Anti-Establishment / Influencer Meme / Political / Event-Driven
  - Brainrot / Survival / Другое
- [ ] **Tier нарратива:** S (2-4 нед) / A (1-2 нед) / B (2-5 дн) / C (<24ч)
- [ ] **Стадия жизненного цикла:**
  - 🟢 Birth — только появился, низкая MC, ранние упоминания
  - 🟡 Expansion — растёт, появляются вариации
  - 🟠 Peak/Saturation — максимум, начинается dilution
  - 🔴 Decline/Fatigue — падение внимания
  - 💀 Revival/Death — возврат с новым контекстом или смерть
- [ ] **Культурный референс:** конкретный мем/персона/событие/игра
- [ ] **Image dup count:** 0 = оригинал, 1-5 = свежо, 5-10 = заезжено, >10 = мусор
- [ ] **Кто/что стоит за проектом:** известная персона, аноним, CTO, AI-сгенерировано
- [ ] **Конкретный ивент/дата:** листинг, твит, анонс, халвинг, выборы
- [ ] **Narrative Velocity:** как быстро растёт упоминание в соцсетях?
  - Нет упоминаний / Единичные твиты / Растёт / Виральный / Спам-фронт

#### 5b: Narrative Score — таблица оценки

| Критерий | Что оцениваем | Балл /10 | Вес | Взвешенный |
|----------|--------------|----------|-----|-----------|
| **🎭 Юмор (Humor)** | Смешно ли? Абсурд, ирония, самоирония, интернет-юмор? | /10 | ×2 | /20 |
| **📢 Виральность (Virality)** | Форматность — легко репостить, мемить, варировать? Есть ли шаблон? | /10 | ×2 | /20 |
| **📈 Тренды (Trend Alignment)** | Совпадает с текущим трендом? (AI-агенты, Pump-культура, политика) | /10 | ×2 | /20 |
| **🌍 Популярность (Popularity)** | Насколько известен референс? (нишевый / интернет-культура / мейнстрим) | /10 | ×1 | /10 |
| **🎨 Креатив (Creativity)** | Оригинальный твист или копия? Неожиданная комбинация? | /10 | ×1 | /10 |
| **🧠 Контекст (Context)** | Какие знания нужны чтобы понять? (крипто-контекст / культура / без контекста) | /10 | ×1 | /10 |
| **📜 Исторические параллели (Resilience)** | Были ли похожие нарративы? Сколько прожили? Чем кончилось? | /10 | ×1 | /10 |
| | **COMPOSITE MEME SCORE** | | **/100** | |

**Шкала Composite Meme Score:**
- **80-100:** 🟢🟢 ELITE — нарратив-киллер, культурный архетип
- **60-79:** 🟢 STRONG — хороший нарратив, есть потенциал
- **40-59:** 🟡 MODERATE — проходной, без искры
- **20-39:** 🟠 WEAK — слабый, быстро умрёт
- **0-19:** 🔴 DEAD — мёртвый нарратив, low-effort мусор

#### 5c: Social Proof (через x-intelligence)
- [ ] **`search_viral_content("$TICKER + keyword", hours_back=48)`** — кто пишет про токен?
- [ ] **Количество упоминаний:** 0 / 1-5 / 5-20 / 20-100 / 100+
- [ ] **Тон обсуждений:** позитивный / нейтральный / негативный / спам / шум
- [ ] **Виральные посты:** есть ли твиты с >100 лайков про токен?
- [ ] **KOL pickups:** кто из влиятельных лиц подхватил нарратив?
- [ ] **`get_niche_leaders("keyword")`** — кто лидеры в этой нише? могут ли подхватить?
- [ ] **Пересечение с другими активными токенами:** один и тот же нарратив на разных токенах? (dilution risk)

#### 5d: Narrative Verdict
- [ ] **Сила нарратива:** Weak / Medium / Strong / Elite
- [ ] **Narrative Risk:** перегрет? заезжен? умирает? (Decline/Fatigue стадия)
- [ ] **Lifetime expectancy:** часы / дни / недели
- [ ] **Может ли нарратив мутировать?** (приобрести новый контекст и жить дольше)
- [ ] **Интеграция с другими шагами:**
  - Если Tier S + Composite >70 → сильный сигнал к входу
  - Если Decline стадия + Composite <40 → фильтр на пропуск
  - Если Social Proof 0 → нарратив не взлетел, даже если идея хорошая

### Шаг 6: Риски и бенчмарк
- [ ] **Risk Score таблица (НОВОЕ):**

| Фактор | Вес | Балл | Комментарий |
|--------|-----|------|-------------|
| Dev вышел/продал | −3 | /3 | |
| Bundler rate >30% | −2 | /2 | |
| Bot rate >20% | −1 | /1 | |
| SM все слили | −3 | /3 | |
| SM свежие покупки | +3 | /3 | |
| KOL всё ещё держит | +2 | /2 | |
| Top10 <20% | +1 | /1 | |
| Контракт не верифицирован | −1 | /1 | |
| Контракт чистый (mint/freeze/tax) | +1 | /1 | |
| LP locked/burned | +1 | /1 | |
| Объём живой (>0.5 MC/vol) | +1 | /1 | |
| Composite Meme 80-100 (Elite) | +3 | /3 | |
| Composite Meme 60-79 (Strong) | +2 | /2 | |
| Composite Meme 40-59 (Moderate) | +1 | /1 | |
| Composite Meme <40 (Weak/Dead) | 0 | /0 | |
| **ИТОГО** | | **/22** | |

**Шкала:**
- ≤5: 🔴 HIGH RISK — не входить
- 6-10: 🟡 WATCH — наблюдать, искать конвергенцию
- 11-15: 🟢 MODERATE — можно half-size
- 16+: 🟢🟢 STRONG — можно full entry

- [ ] Красные флаги
- [ ] Зелёные сигналы
- [ ] Сравнение с похожим проектом
- [ ] Потенциал (x? от текущей MC)

### Шаг 7: Bull/Bear дебаты (НОВОЕ — вместо одного вердикта)
Перед финальным вердиктом — запустить две перспективы:

**1. BULL CASE** — адвокат дьявола в пользу входа:
- Почему этот токен может x5?
- Что я упускаю позитивного?
- Какой сценарий, где я буду жалеть что не вошёл?
- Кто из SM/KOL может купить завтра?

**2. BEAR CASE** — адвокат против входа:
- Почему этот токен может упасть −80%?
- Что я игнорирую из красных флагов?
- Что скажут будущие уроки trade-log?
- Какой сценарий, где я буду рад что пропустил?

**3. SYNTHESIS — решение:**
| Критерий | Bull | Bear | Вес |
|----------|------|------|-----|
| Narrative (Composite/20) | /5 | /5 | x2 |
| SM/KOL | /5 | /5 | x3 |
| Risk/Hygeine | /5 | /5 | x2 |
| Timing | /5 | /5 | x1 |
| **Weighted** | **/40** | **/40** | |

> Narrative: Composite Meme Score / 20 = (min(max(score,0),100)/20) → /5
> Например: CMS 73 → 73/20 = 3.65 → Bull 4/5, Bear аргумент тоже оценивается /5

### Шаг 8: Вердикт
- [ ] 🟢 Strong Buy / 🟢 Buy / 🟡 Watch / 🔴 Skip / 🔴 Hard Pass
- [ ] **Conviction: LOW (0-33%) / MEDIUM (34-66%) / HIGH (67-100%)**
- [ ] **Time horizon:** скальп (<1ч) / свинг (1-24ч) / холд (дни)
- [ ] **Ключевой аргумент** (одна строка)

### Шаг 9: Structured Decision Output (МАШИНОЧИТАЕМЫЙ)

После вердикта — сформировать JSON-решение для потенциальной автоматической торговли:

```json
{
  "decision_id": "dec_20260605_001",
  "timestamp": "2026-06-05T14:30:00Z",
  "token": {
    "symbol": "SV151",
    "contract": "SV151D5pjygAKA8aJJcKzm4wFnRX5G92Fye94jQJk7g",
    "chain": "solana",
    "launchpad": "meteora_virtual_curve",
    "age_hours": 18
  },
  "decision": {
    "action": "SKIP",
    "conviction_pct": 85,
    "bucket": "dev_tracking"
  },
  "risk_score": {
    "total": 4,
    "max": 21,
    "factors": {
      "dev_exit": -3,
      "bundler_rate_over_30": -2,
      "bot_rate_over_20": -1,
      "sm_all_sold": -3,
      "sm_fresh_buys": 0,
      "kol_still_holding": 0,
      "top10_under_20": 1,
      "contract_not_verified": -1,
      "contract_clean": 1,
      "lp_locked": 1,
      "vol_live": 1,
      "narrative_strong": 0
    }
  },
  "narrative": {
    "category": "Internet Culture",
    "tier": "B",
    "lifecycle": "Birth",
    "composite_meme_score": 67,
    "humor": "8/10",
    "virality": "7/10",
    "trend_alignment": "8/10",
    "popularity": "5/10",
    "creativity": "6/10",
    "context": "6/10",
    "resilience": "5/10",
    "social_proof": {
      "mentions_48h": 12,
      "viral_tweets": 1,
      "kol_pickups": 0,
      "sentiment": "positive"
    },
    "verdict": "Strong — свежий интернет-мем, Tier B, есть виральный потенциал"
  },
  "bull_bear": {
    "bull_score": 12,
    "bear_score": 32,
    "bull_case": "Bedrock Foundation — реальный проект Meteora×grvn_ai, CTO, чистый контракт",
    "bear_case": "Dev вышел, 46% объёма боты, SM/KOL полностью слили, -44% от ATH"
  },
  "entry": null,
  "exit": null,
  "reflection": {
    "lesson": "Токены без SM конвергенции на второй день = труп",
    "recheck_at": "2026-06-06T14:00:00Z",
    "recheck_conditions": ["SM_convergence", "price_stabilization", "twitter_activity"]
  }
}
```

#### Schema полей

| Поле | Тип | Допустимые значения |
|------|-----|---------------------|
| `decision.action` | enum | `BUY` / `SELL` / `SKIP` / `WATCH` |
| `decision.conviction_pct` | int | 0-100 (насколько уверен в решении) |
| `decision.bucket` | enum | `dev_tracking` / `narrative` / `deep_dip` / `sm_convergence` / `momentum` |
| `entry.zone_mc_low` | int | Нижняя граница MC для входа |
| `entry.zone_mc_high` | int | Верхняя граница MC для входа |
| `entry.position_sol` | float | Размер позиции в SOL |
| `entry.position_pct` | float | % от портфеля |
| `entry.type` | enum | `market` / `limit` / `scale_in` |
| `exit.tp1_mc` | int | Take Profit 1 |
| `exit.tp1_pct` | float | % позиции для TP1 |
| `exit.tp2_mc` | int | Take Profit 2 |
| `exit.sl_mc` | int | Stop Loss MC |
| `exit.trailing_stop` | bool | Использовать трейлинг? |
| `exit.time_stop_mins` | int | Через сколько минут закрыть, если не сработало |
| `narrative.category` | enum | Категория нарратива (см. библиотеку) |
| `narrative.tier` | enum | `S` / `A` / `B` / `C` |
| `narrative.lifecycle` | enum | `Birth` / `Expansion` / `Peak` / `Decline` / `Revival` |
| `narrative.composite_meme_score` | int | 0-100 (Composite Meme Score) |
| `narrative.social_proof.mentions_48h` | int | Количество упоминаний за 48ч |
| `narrative.social_proof.viral_tweets` | int | Твиты с >100 лайков |
| `narrative.social_proof.kol_pickups` | int | KOL, подхватившие нарратив |
| `narrative.social_proof.sentiment` | enum | `positive` / `neutral` / `negative` / `noise` |

---

### Шаг 10: Portfolio Sizing (РАСЧЁТ РАЗМЕРА ПОЗИЦИИ)

Если решение `BUY` — рассчитать точный размер позиции:

#### Алгоритм

```
risk_per_trade = 5%    # Макс потерь на сделку (% портфеля)
conviction_mult = conviction_pct / 100  # 0.0 - 1.0

if action == "SKIP":
    position_sol = 0
elif action == "WATCH":
    position_sol = 0  # не входить, следить
elif action == "BUY":
    base_size = portfolio_balance_sol * risk_per_trade / 100
    position_sol = base_size * conviction_mult
    
    # Модификаторы:
    if risk_score <= 5:    # HIGH RISK
        position_sol = 0  # не входить никогда
    elif risk_score <= 10: # WATCH
        position_sol *= 0.5  # половинный размер
    elif risk_score <= 15: # MODERATE
        position_sol *= 1.0  # полный размер
    else:                  # STRONG
        position_sol *= 1.5  # +50% к размеру
    
    # Модификатор bucket:
    if bucket == "deep_dip":
        position_sol *= 0.7  # deep dip = выше риск
    elif bucket == "sm_convergence":
        position_sol *= 1.3  # SM convergence = ниже риск
    
    # Модификатор timeframe:
    if timeframe == "scalp":
        position_sol *= 1.2  # скальп = быстрый выход
    elif timeframe == "hold":
        position_sol *= 0.7  # холд = больше неизвестность

    # Ограничения:
    position_sol = min(position_sol, max_position_sol)  # не больше макс
    position_sol = max(position_sol, min_position_sol) if position_sol > 0 else 0  # или 0 если слишком мало
```

#### Пример расчёта

```
portfolio_balance = 5 SOL
risk_per_trade = 5% → 0.25 SOL base
conviction = 70% → 0.25 * 0.7 = 0.175 SOL
risk_score = 14 (MODERATE) → 0.175 * 1.0 = 0.175 SOL
bucket = sm_convergence → 0.175 * 1.3 = 0.2275 SOL
timeframe = scalp → 0.2275 * 1.2 = 0.273 SOL

Итог: 0.27 SOL (5.4% портфеля)
```

---

### Шаг 11: Decision Queue (ДЛЯ АВТОМАТИЗАЦИИ)

Каждое решение сохраняется в `/root/lexa-knowledge/decisions/` как JSON:

```
/root/lexa-knowledge/decisions/
├── 2026-06-05_SV151_dec.json     # структурированное решение
├── 2026-06-05_SV151_reflection.md # человеко-читаемая рефлексия
└── queue/                        # активные позиции (для auto-trader)
    ├── active.json               # текущие открытые позиции
    └── history.json              # история закрытых позиций
```

Отсюда любой auto-trader (Fasol, скрипт, бот) может читать решения и исполнять.

---

## Quick-check безопасности (перед любой операцией)

- [ ] Honeypot? (🚫 стоп)
- [ ] Mint renounced?
- [ ] Freeze renounced?
- [ ] Buy/sell tax = 0%
- [ ] LP burned?
- [ ] Top 10 < 20%?
- [ ] Rug ratio < 0.3?

---

## Reflection Log (АВТОМАТИЧЕСКИЙ ПОСЛЕ КАЖДОГО АНАЛИЗА)

После завершения анализа (вход или пропуск) — сразу сохранить запись:

```yaml
date: 2026-06-05
token: SV151
contract: SV151D5pjygAKA8aJJcKzm4wFnRX5G92Fye94jQJk7g
action: SKIP
verdict: HIGH RISK — AVOID
conviction: HIGH
key_metric: dev_exit + 46% bots + SM fully sold
risk_score: 4/21

# Если вошёл:
entry_mc: 
entry_price: 
position_sol: 
exit_mc: 
exit_price: 
pnl_percent: 
pnl_sol: 

# Рефлексия (заполняется при закрытии сделки или через 24ч):
predicted_vs_actual: 
what_i_missed: 
lesson: 
update_rules: true/false
```

**Reflection Loop Rules:**
1. При следующем анализе — прочитать **последние 5 entries** из Reflection Log
2. Если есть неучтённый урок → добавить в `rules.md`
3. Если тот же токен анализируется повторно → сначала прочитать предыдущий entry
4. Каждые 10 анализов → ревью паттернов ошибок

---

## Wallet Tracing Protocol (при глубоком анализе)

Для токенов с Risk Score >10 или при наличии SM/KOL интереса:

### Source Tracing
- [ ] Dev wallet funded from? trace back 2-3 hops
- [ ] Common funding cluster? (несколько кошельков с одним source)
- [ ] CEX withdrawal pattern? (одинаковый размер, время?)

### Distribution Tracing
- [ ] Dev → Top holders: есть ли прямые переводы?
- [ ] Top holders → друг другу: есть ли внутренние переводы?
- [ ] Bundler cluster: одинаковый паттерн выхода?

### Smart Money Deep Dive
- [ ] Когда SM впервые зашёл? (первый блок или позже?)
- [ ] SM avg buy price vs current price
- [ ] SM последняя активность (всё ещё торгует или ушёл?)
- [ ] SM активность в других токенах (параллельные позиции)

---

## Мои прошлые ошибки (памятка)

| Дата | Токен | Ошибка | Что надо было сделать |
|------|-------|--------|----------------------|
| 24.05.26 | RICH | Не проверил Twitter → пропустил @chooserich (Nick O'Neill, 281K) | Открыть ссылку, прочитать твиты |
| 24.05.26 | GLOVE | — | — |
| 24.05.26 | TOLYBOT | — | — |
