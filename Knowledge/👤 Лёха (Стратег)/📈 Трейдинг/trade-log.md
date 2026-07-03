# Trade Log & Reflection

## Структура записи

```yaml
---
id: trade_20260605_001
date: 2026-06-05
token: SV151
contract: SV151D5pjygAKA8aJJcKzm4wFnRX5G92Fye94jQJk7g
bucket: dev_tracking
action: SKIP
decision: HIGH RISK — AVOID
conviction_pct: 85
risk_score: 4/21
narrative: Pokémon 151 + Bedrock Foundation (Meteora×grvn_ai)

# Structured Decision (from Шаг 9)
structured: {
  "entry": null,
  "exit": null,
  "bull_bear": {
    "bull_score": 12,
    "bear_score": 32
  },
  "key_metric": "dev_exit + 46% bots + SM all sold",
  "recheck_at": "2026-06-06",
  "recheck_conditions": ["SM_convergence", "price_stabilization", "twitter_activity"]
}

# Reflection
lesson: "Токены без SM конвергенции на второй день — труп"
update_rules: true
---
```

## Log

### 5 June 2026

#### SV151 — SKIP (HIGH RISK)
| Поле | Значение |
|------|----------|
| Bucket | Dev Tracking (post-launch) |
| Decision | 🔴 Skip — HIGH RISK |
| Conviction | HIGH |
| Risk Score | 4/21 |
| Narrative | Pokémon SV + Bedrock Foundation RWA |
| Почему | Dev вышел, 46% боты, SM/KOL всё слили, -44% от ATH |
| План ре-чек | 6 июня: SM convergence, цена, Twitter активность |

#### Что пошло хорошо
- Полный сбор данных (security, dev, SM, KOL, соцсети)
- Twitter верифицирован — Bedrock Foundation настоящий
- Верная оценка ботового объёма

#### Что можно улучшить
- Не посмотрел Telegram/чат проекта
- Не сделал wallet tracing (куда ушли dev деньги кроме продажи?)
- Bull/Bear дебаты не проводились (теперь будет!)

### 24 May 2026

#### RICH — SKIP (ошибка)
| Поле | Значение |
|------|----------|
| Bucket | Narrative (CTO) |
| Decision | Skip — missed @chooserich KOL |
| Lesson | Twitter проверять первым, открывать ссылки |

#### 24 May 2026 — Другие токены
- GLOVE — мёртвый токен, SM вышли
- TOLYBOT — затухание после ATH, RC держит
- BUFFDON — перелив из GLOVE, SM массово вышли

---

## Pattern Tracker (авто-заполняется после каждых 10 логов)

| # | Паттерн | Встречаемость | Profitability |
|---|---------|---------------|---------------|
| 1 | Dev exit → токен умирает | 3/3 | — |
| 2 | SM convergence = живой токен | 2/2 | + |
| 3 | No SM на 2й день = труп | 2/2 | — |
| 4 | | | |

---

## Auto-Reflection (запускать при старте нового анализа)

```
Последние 5 записей:
1. SV151 — SKIP: dev exit, bots, no SM
2. ...
3. ...
4. ...
5. ...

Извлечённые уроки для этого анализа:
- 
```
