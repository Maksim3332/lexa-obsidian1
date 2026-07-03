# Master Index — Проанализированные токены

Все данные по токенам: анализ, трекинг, Twitter, алерты.

---

## Портфельные / Под наблюдением

| Токен | Контракт | Статус | Последний MC | Сессий | Источник |
|-------|----------|--------|-------------|--------|----------|
| [TOLYBOT](./TOLYBOT/analysis.md) | `FjgXCL8ov5BkvZGoY2QthvhUmx82mVkSmhni6nCJpump` | 🟢 в портфеле | ~$657K | 20+ сессий | session-tracking |
| [Opossum](./Opossum/analysis.md) | `AL5SiGgTFVchgoezugke1LTaQvJq5QbDtKw8xWrhpump` | 🔴 убит | — | — | session-tracking |
| [Panda](./Panda/analysis.md) | — | 🔴 убит | — | — | session-tracking |
| [CupMarkets](./CupMarkets/analysis.md) | — | 🔴 мёртв | — | — | session-tracking |
| [WURLDCAP](./WURLDCAP/analysis.md) | — | — | — | — | session-tracking |
| [WORLDCUP](./WORLDCUP/analysis.md) | — | — | — | — | session-tracking |

## Детальный анализ

| Токен | Контракт | Откуда | Что есть |
|-------|----------|--------|----------|
| [PEETOKEN](./PEETOKEN/analysis.md) | — | Trading анализ | Анализ, Twitter |
| [FROGE](./FROGE/analysis.md) | — | Twitter анализ | Twitter |
| [RKC](./RKC/analysis.md) | `7HgfXftRBBqsYtAEYcqjGLQrNJLL6Tww9ek4rE3Apump` | Twitter анализ | Twitter |

## Алерты сканера (Fasol Scanner v1)

С 23 по 28 мая — 114 токенов отсканировано, ~50+ квалифицировались.

### SUPER CALLS (Score ≥ 85)

| Дата | Токен | Score | MC | Vol | Стратегия |
|------|-------|-------|----|-----|-----------|
| 28 May | [$Axiom](./scanner/Axiom/alert.md) | **90** | $25K | $694K | early |
| 23 May | $Gena (100) | **100** | $34K | $1.1M | — |
| 23 May | $BUFFDON (95) | **95** | $188K | — | — |
| 23 May | $RICH (102) | **102** | $737K | $11.6M | — |
| 23 May | $DEGEN (92) | **92** | $441K | $2.8M | — |
| 23 May | $WYNN (94) | **94** | $203K | $1.5M | — |
| 23 May | $JAMES (87) | **87** | $139K | $1.8M | — |
| 23 May | $CATCOIN (91) | **91** | $573K | $130K | — |
| 23 May | $UFU (93) | **93** | $73K | $1.4M | — |
| 23 May | $Ask (87) | **87** | $75K | $908K | — |
| 23 May | $dumped (85) | **85** | $26K | $861K | — |
| 23 May | $ATM (90) | **90** | $815K | $1.6M | — |
| 23 May | $PENNY (90) | **90** | $98K | $956K | — |
| 23 May | $yunc (85) | **85** | $45K | $643K | — |

### Backtest (23 May)

| Токен | Score | MC | Drop | Зона |
|-------|-------|----|------|------|
| Opossum | 81 | $33K | 61% | 🔵 Deep dip |
| Gena | **100** | $29K | 78% | 🔥 Very deep dip |
| BUFFDON | **95** | $188K | 56% | 🔵 Deep dip |
| USDP | 89 | $50K | 90% | 💀 Extreme dip |
| Ryker | 67 | $2.7K | 78% | 🔥 Dead |
| FASTEST | 59 | $37K | 17% | ⚠️ Near ATH |

---

## Источники данных (где что лежит)

| Что | Где |
|-----|-----|
| **Новая структура токенов** | `/root/lexa-knowledge/tokens/` |
| **Сессионные снепшоты** | `/root/lexa-knowledge/session-tracking/snapshots.csv` |
| **Состояние TOLYBOT** | `/root/lexa-knowledge/session-tracking/tolybot_state.json` |
| **Паттерны** | `/root/lexa-knowledge/patterns.md` |
| **Алерты Fasol Scanner** | `/opt/fasol-scanner/data/alerts.json` |
| **Лог сканера (все 114 токенов)** | `/opt/fasol-scanner/scanner.log` |
| **Trading анализы** | `/root/lexa-knowledge/trading/` (legacy) |
| **Twitter анализы** | `/root/lexa-knowledge/twitter/` (legacy) |
| **Post-Analysis трекинг (3 дня)** | `./post_analysis/data/tracking_db.json` |
| **Smart Wallets (из успешных)** | `./smart_wallets/smart_wallets.json` |
| **Top Holders (из успешных)** | `./top_holders/top_holders.json` |
| **Ежедневные отчёты** | `./post_analysis/reports/` |

> Со временем все данные переедут в `/root/lexa-knowledge/tokens/<TOKEN>/`
