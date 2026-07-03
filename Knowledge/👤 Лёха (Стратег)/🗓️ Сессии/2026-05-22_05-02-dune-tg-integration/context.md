# Session 2026-05-22 — Full session log

## Sequence of events

1. User asked "What did we do so far?" — loaded AGENTS.md, gave full project status
2. User: "пусто в метриках. Я могу с тобой общаться через бота?" — explained old tokens in Fasol Exporter, offered to build Telegram bridge (deferred)
3. User: "Позже, добавь текущие токены в метрики" — replaced TRACKED_COINS in /opt/fasol-exporter/exporter.py with: RKC, TOLYBOT, Opossum, Panda, WURLDCAP, CupMarkets
4. User: "я хотел что бы ты эти токены добавил в дашборд промефеус" — started Grafana (was stopped), created dashboard via API "Portfolio — Fasol Intelligence" (uid: ffmrlbi6du680a), sent link to TG
5. User: "ошибка, удали пока, потом настроим" — deleted Grafana dashboard via API
6. User: "сколько токенов потратится до завтрешнего вечера пока меня не будет" — explained ~0 LLM tokens while away, only cron jobs run
7. User: "заодно тогда проверяй данные с дюны" — modified /opt/daily-token-analysis.sh to fetch Dune data (:9103) each session, detect market regime, log to snapshots.csv
8. User: "Тогда сразу скидывай в бота результаты проверки, и краткий вывод про динамику развития" — added Telegram auto-send to script (bot: 8531388683:AAGJHWMQ5DRaj-2ZPW8ji0qiKxA6VDSFZws, chat: 267693252)
9. User: "И скажи как отключить бота если что то пойдет не так" — kill switch: touch /tmp/disable-bot-alerts
10. User: "отлично" — satisfied
11. User: "Сохранил сессию, а тоя не перезапускал опенкод" — saved session
12. User: "сохранил все от самого начала ?" — expanding this record

## Key decisions
- Fasol Exporter now tracks current portfolio tokens, not old ones
- Grafana dashboard created then removed (user wants to redo later)
- Dune Exporter started (:9103) for market-level context per session
- Session analysis auto-posts to Telegram with token stats + Dune data
- LLM tokens: zero usage while user away (no automated LLM calls)

## Active services
- Fasol Exporter (:9101) — running, current portfolio
- Dune Exporter (:9103) — running, 600s scrape interval
- Grafana (:3000) — running, no portfolio dashboard yet
- Telegram bot — active, session reports enabled

## Cron schedule
- 02:00 UTC — Asia session analysis
- 10:00 UTC — Europe session analysis
- 16:00 UTC — US session analysis

## Kill switch
- touch /tmp/disable-bot-alerts — stops Telegram sends, analysis continues
- crontab -e — comment lines for full stop
