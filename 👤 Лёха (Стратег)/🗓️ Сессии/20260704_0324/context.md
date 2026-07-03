- [2026-06-06 02:47:42] [setup] Настроено авто-сохранение шагов: save-step.sh + AGENTS.md + memory-lexa + supermemory
- [2026-06-06 02:49:33] [setup] Установлен ocwatch v0.6.0, порт 50234, дашборд добавлен в lexa-obsidian
- [2026-06-06 02:49:34] [setup] Добавлено правило ПРОМТ: в AGENTS.md
- [2026-06-06 02:52:01] [fasol] Обновлён fasol-skills: два новых sub-skill (smart-money-stream, calls-stream) + changelog прочитан
- [2026-06-06 03:02:00] [infra] Установлен twitter-research MCP (twitterapi.io) — 7 инструментов зарегистрированы в settings.json
- [2026-06-06 03:15:00] [research] v3 Research: $DATBIHGAH — 1-я попытка (неполная). Пропущен @DatBihGahonsol, не понят нарратив
- [2026-06-06 03:25:00] [research] v3 Research: $DATBIHGAH — 2-я попытка (полная). Найдены @DatBihGahonsol (0 foll, 10 tweets), KYM roundup, мем-активность. Понят нарратив: виральный TikTok kid (@braydenharrelson1) → Kool-Aid pineapple → "Dat Bih Gah" как новый сленг вместо "fire/gas"
- [2026-06-06 03:11:07] [research] v3 Research DATBIHGAH: полный разбор с twitterapi.io. Нарратив — TikTok Kool-Aid pineapple kid (@braydenharrelson1), фраза 'Dat Bih Gah' как новый сленг вместо fire/gas. KYM + Yahoo News подтверждают виральность. @DatBihGahonsol жив (0 foll, 10 tweets). Вердикт: pump-аккаунт слабый, но культурный мем реален — требует мониторинга
- [2026-06-06 03:11:09] [session-end] Сессия завершена
- [2026-06-06 03:14:20] [protocol] v2.0 протокола: добавлен Этап 2 (Narrative Intelligence) — Сначала разобрать мем, потом привязать к токену. Обновлены Social и On-Chain разделы. Исправлены параметры twitterapi.io (userName вместо userNameOrEmailAddress)
- [2026-06-06 03:14:21] [session-end] Сессия завершена
- [2026-06-06 03:22:39] [infra] Починил nginx: root / теперь проксирует на ocwatch (50234). Fasol Journal вынесен на /journal/. SSE таймаут увеличен до 1ч для live-обновлений
- [2026-06-06 03:22:40] [session-end] Сессия завершена
- [2026-06-06 19:30:00] [infra] Отладка OCWatch: белый экран через nginx. Причина — двойное сжатие (bun gzip + nginx). Фикс: proxy_set_header Accept-Encoding "";
- [2026-06-06 19:45:00] [infra] Настроен SSL (самоподписанный) на 443 порт для авто-HTTPS браузера
- [2026-06-06 20:00:00] [infra] OCWatch на http://82.29.72.151/ (корень, работает). Dashboard на /cabin/
- [2026-06-06 20:15:00] [session-end] Сессия завершена. Итог: OCWatch починен, SSL настроен, nginx оптимизирован

## 2026-06-07 — Прерывание сессии
- Причина: оплата через 5 дней, перебои на сервере
- Сессия прервана
- Последний контекст: SV151 — HIGH RISK AVOID, Fasol Scanner v2 scalp pipeline, Protocol v3
- [2026-06-07 03:29:45] [session-interrupt] Сессия прервана — оплата через 5 дней, перебои сервера
- [2026-06-07 03:30:30] [session-resume] Сессия восстановлена после reboot сервера

## 2026-06-07 — Удаление Fasol Journal + отключение алертов
- Fasol Journal: сервис остановлен, systemd файл удалён, директория /opt/fasol-journal удалена
- Telegram алерты: TELEGRAM_ENABLED = False в /opt/fasol-scanner/config.py
- Добавлена проверка TELEGRAM_ENABLED в scanner.py перед send_alert
- Скальп-стратегия и скилы — сохранены
- Решение: торгуем реальной SOL
- [2026-06-07 03:45:11] [rule] Добавлено правило пошаговой разработки в AGENTS.md
- [2026-06-07 03:57:51] [hermes-progress] Hermes: Фаза 2 и Фаза 5 завершены. Остались Фаза 3 (GEPA) и Фаза 4 (Cron)
- [2026-06-07 04:53:59] [session-end] Сессия: MemeSniper запущен, Hermes Фаза 2+5 готовы
- [2026-06-08 19:27:55] [cluster] Snapshot 7 SM-cluster tokens saved (shibpost, Teletubby, POG, PHOTO, KEKIUS, AMERICA, LIFE) для проверки в след. сессии
- [2026-06-08 20:32:56] [general] Dune wallet pipeline: query created, 100 wallets imported, cluster snapshot taken, auto-update on session start
- [2026-06-08 20:53:37] [general] Dune winrate70+ avgPnL50+ query. 32 clean wallets saved to clipboard after GMGN balance+activity check
- [2026-06-08 22:23:45] [general] Глобальный план: пауза на кластерной стратегии, фиксим направление
- [2026-06-08 22:24:41] [general] Глобальный план: global-plan.md + обновление active/backlog
- [2026-06-08 22:31:12] [general] Глобальный план: Signal Dashboard Platform — Фазы 1-3
- [2026-06-08 23:30] [milestone] Внедрение Vellum-inspired архитектуры: Graph Memory + SubAgent Roles + Pattern Scanner + Heartbeat. Ключевые файлы: /usr/local/bin/graph-memory, agent-role, pattern-scan, lexa-heartbeat. DB: /root/lexa-knowledge/graph-memory/store.db (12 нод, 5 рёбер). AGENTS.md переписан.
- [2026-06-10 01:00:27] [session-start] Сессия восстановлена после лимитов. Graph Memory (16 нод). Scanner+MemeSniper запущены.
- [2026-06-10 01:00:28] [session-end] Сессия завершена
- [2026-06-10 01:00:36] [session-start] Сессия старт. Всё поднято. Graph Memory 16 нод.
- [2026-06-10 01:09:18] [research] Разобрали TradingAgents — multi-agent LLM trading framework. 84.7k★. LangGraph, 4 команды агентов, дебаты, checkpoint/resume, двухфазная память. Можно забрать: structured output fallback, message clear nodes, дебейтные циклы, checkpoint resume.
- [2026-06-10 01:27:41] [dev] Checkpoint система: /usr/local/bin/checkpoint — SQLite-база прогресса анализа. save/load/latest/list/done/remove. Этапы 0-7. Данные мержатся инкрементально. Resume после OpenCode лимитов.
- [2026-06-10 01:39:21] [infra] Camofox browser уже работает. Docker на 9377/6080. CLI /usr/local/bin/camofox. Twitter-scraper (TheRoaringKitty, RKC) через Camofox на 9102. VNC сессия vnc_login с куками Twitter.
- [2026-06-10 01:52:30] [dev] Установлены AutoHedge (v0.1.6) и Vibe-Trading (v0.1.9). AutoHedge — Jupiter Ultra API инструменты для Solana. Vibe-Trading — 452 alphas, 10 brokers, swarm, MCP. План обновлён.
[2026-06-10 02:20:27] Safety Mandate + Kill Switch deployed
  - /usr/local/bin/safety-mandate CLI (halt/resume/pause/edit/audit/daily-reset)
  - /usr/local/bin/gmgn-safe wrapper (pre-trade checks: HALT, score, position, limit)
  - /opt/safe-server.py with /api/safety-status endpoint
  - NFT dashboard safety indicator on port 8080
  - Audit log: /root/lexa-knowledge/safety/audit/
  - Daily counter auto-reset via cron (midnight)
- [2026-06-10 02:48:56] [general] SM Cluster 48h follow-up: 7 tokens from 8 Jun. AMERICA stable -1.6% (SM 31→33), KEKIUS -7.1% (SM 32→33). SM bought dip: Teletubby +16 SM at -77.6%, LIFE +10 SM at -82.1%. Dead: shibpost -93.9%, POG -97.3%, PHOTO -87%
- [2026-06-10 02:48:56] [session-end] Сессия завершена
- [2026-06-10 03:22:11] [general] Настроен snapshot-collector.sh — авто-снапшоты кластеров и скальпинг-кандидатов каждые 6ч через cron. Первый снапшот: 12 кластерных токенов, 8 скальп-кандидатов (Puffy SM=4 лучший). Данные для бектеста копятся в /root/lexa-knowledge/snapshots/
- [2026-06-10 03:22:12] [session-end] Сессия завершена
- [2026-06-10 03:48:28] [general] Dreamer layer deployed: walk + signal filter + board + handoff + digest + cron + agent-role
- [2026-06-10 03:48:29] [session-end] Сессия завершена
- [2026-06-10 04:03:01] [session-end] Сессия завершена
- [2026-06-11 03:09:23] [general] Настроен Telegram → Open Notebook bridge: пользователь шлёт ссылки в TG, бот кладёт в Open Notebook, я анализирую и сохраняю в supermemory. При старте сессии отображаю новые источники.
- [2026-06-11 03:09:24] [session-end] Сессия завершена
- [2026-06-11 03:10:25] [general] Session 2026-06-11: Telegram→Open Notebook bridge, Buildroom→Dreamer bridge, tools audit
- [2026-06-11 03:10:27] [session-end] Сессия завершена
- [2026-06-11 03:49:18] [walrus-memory] Walrus Memory: ключ не добыт (нужно 66 hex символов с сайта memory.walrus.xyz, отложено)
- [2026-06-11 03:49:22] [walrus-memory] BaiBit seed phrase проверена — не совпадает с Walrus ключом
- [2026-06-11 03:49:22] [session-end] Сессия завершена
- [2026-06-11 19:48:31] [general] Аудит инструментов: 35 скилов, Open Notebook TG-бридж, Buildroom→Dreamer bridge
- [2026-06-11 19:48:32] [tools-audit] Аудит инструментов: 35 скилов, Open Notebook TG-бридж, Buildroom→Dreamer bridge
- [2026-06-11 19:48:34] [session-end] Сессия завершена
- [2026-06-11 20:27:02] [signal-platform] MemeSniper: добавлен русский язык, переключатель zh→en→ru
- [2026-06-11 20:44:19] [signal-platform] MemeSniper: агенты → 4 метрики интереса (✈ TG, 𝕏 Twitter, 🧠 SM, ⭐ KOL)

## Session 2026-06-15 — Scalp Alert Optimization
- Scalp V3 alert created: MC 50-150K, migrated, liq≥20K, vol≥80K, holders≥100, top10≤20%, bot_fee<$5 → 81% 1.5x
- Profit backtest: 36 coins/5d, TP 1.5x SL -20% = +36% ROI ($883)
- Autobuy configured on alert 19384
- [2026-06-15 03:46:42] [general] Scalp V3 81% alert saved with autobuy TP 1.5x SL -20%, profit backtest done, session saved
- [2026-06-15 03:48:40] [session-end] Сессия завершена. В следующей сессии — гем хантинг

## [2026-06-16 03:30] Gem Team Pipeline — Checkpoint

### Создано
- `/opt/scripts/gem-pipeline/chart-score.py` — анализ минутных свечей (волатильность, фитили, гэпы, объёмы)
- `/opt/scripts/gem-pipeline/bundle-detect.py` — детект бандлинга (funding кластеры + security метрики)
- `/opt/scripts/gem-pipeline/gem-analyze.sh` — 7-шаговый pipeline (Safety→Holders→Charts→Metrics→Social→Decision)
- `/opt/scripts/gem-pipeline/gem-scan.py` — batch scan трендов через pipeline с отправкой в TG

### Методология Gem Team (с他们的 постов)
1. **Safety** — renounced mint, verified, no tax, no honeypot, no malicious functions
2. **Holders** — top10 rate, bundler rate, sniper count, funding clusters (native_transfer)
3. **Charts** — минутные 1m свечи: штраф за "ёлку" (CV>10%), длинные фитили(>40%), гэпы(>5%), всплески объёмов(>3σ)
4. **Metrics** — MC ($10K-$200K), liquidity (>$10K), vol/MC ratio (>0.2x), holder count (>50), social links
5. **Social** — Twitter/X, website, telegram

### Первый запуск
- 25 candidates в MC $10K-$200K
- 20 GEM QUALIFIED (≥70), 5 WATCHLIST (50-69)
- Выявлена проблема: слишком много GEM, нужна калибровка

### Что делать дальше
1. **Закрутить гайки скоринга** — повысить вес Chart Score, штрафовать за bundler_rate >0.3, поднять вес Social
2. **Добавить мониторинг новых деплоев** (по аналогии с Gem Team на Ethereum)
3. **Интегрировать с Fasol Alert** для автоматических алертов при нахождении GEM

### Команда для восстановления контекста
"привет восстанови контекст"
- [2026-06-18 02:58:33] [general] Создал 3 scalp алерта 1.2x в Fasol (V21 freq #19512, V16 safe #19513, V15 balance #19514)
- [2026-06-18 03:36:35] [general] fasol-monitor: baseline+checkpoint+recalibrate+alert-apply+AGENTS hook — система мониторинга деградации алертов и авто-калибровки готова

## [2026-06-18 04:00] TimesFM TimesFM_2p5_200M — протестирован для скальпинг сигналов на pump.fun
### Создано
- `/usr/local/bin/fm-forecast` — CLI: forecast одного токена или batch сканирование
- Установлен: google/timesfm-2.5-200m-pytorch (200M params, torch 2.12.1+cpu)

### Результаты тестов
- **pump.fun 1m (12 шагов = 12 мин)**: 15 токенов → 0/15 с +10%. MAX +5.25% (UPTOBER). Confidence в основном LOW (13-36%)
- **pump.fun 5m/15m**: недостаточно свечей — токены живут <12 часов
- **Mature Meteora 5m (12 шагов = 60 мин)**: достаточно свечей, но волатильность низкая (<+1%)
- **Mature Meteora 15m (12 шагов = 3ч)**: 3/10 с 100 свечами, forecast флет ±0.1-6.5%

### Вывод
TimesFM zero-shot не видит скальпинг сигналы +10% на pump.fun. Причина: модель обучена на плавных рынках (акции/BTC), pump.fun 1m — это шум с внезапными пампами. Нужен либо LoRA fine-tune на pump.fun данных, либо гибрид GMGN сигналов + ML.

### Использование
```bash
fm-forecast <token_address>              # single, 1m/12 steps
fm-forecast <token_address> --res 5m --horizon 12  # custom
fm-forecast --batch                       # top 5 trending
```

## Autobuy план (согласован, НЕ ВЫПОЛНЕН)
- Старт: консерватив (5-15 SOL) → TP 1.2x SL -20%
- Фаза 2: умерен (15-30 SOL) → TP 1.5x или ladder
- Фаза 3: агрессив (30+ SOL) → TP 2-3x или TSL
- Алерты готовы: V21 (19512), V16 (19513), V15 (19514) — фильтры настроены, autobuy OFF
- Пользователь решил: ничего не менять сейчас, запомнить на будущее
- [2026-06-18 23:16:37] [general] 
- [2026-06-18 23:16:42] [timesfm-test] TimesFM тесты: 0/15 pump.fun сигналов +10%, сохранён fm-forecast CLI, zero-shot не эффективен

## [2026-06-19 19:34] Step 1 — gem-pipeline refactored to gmgn-cli

### Что сделано
- `gem-analyze.sh` больше не вызывает внешние Python-скрипты
- **bundle-detect.py** → inlined (строки 64-137): `gmgn-cli token security` + `token holders --limit 30`
- **chart-score.py** → inlined (строки 151-240): `gmgn-cli market kline --resolution 1m`
- Оба удалены из `/opt/scripts/gem-pipeline/`

### Результат
- 743 LOC custom Python заменены на прямые gmgn-cli вызовы
- Pipeline всё ещё 7 шагов, тот же output format
- gem-scan.py не менялся — совместим

### Состав gem-pipeline/
- `gem-analyze.sh` — pipeline (только gmgn-cli + inline python)
- `gem-scan.py` — batch scan (вызывает gem-analyze.sh)
- `gem-scan.sh` — shell-версия (не используется)

### Что дальше
- Step 2: n8n workflow Trench→GMGN→scoring→MemeSniper
- Step 3: удалить старые Python-скрипты после стабилизации

## [2026-06-19 19:54] TPM analysis and tpm-monitor

### Что выяснили
- Rate limit **не по дневному бюджету**, а по TPM (tokens per minute) на стороне Zen/Fireworks
- **Пик вчера:** 1.35M tokens/min (включая cache reads)
- **Rate limit сработал** при ~650K tokens/min в 16:33
- **Доминанта — cache reads** (~95% всего трафика)
- Big Pickle **бесплатный** (Free/Free/Free по прайсингу Zen)

### Создано
- `/usr/local/bin/tpm-monitor` — мониторинг TPM в реальном времени
- Команды: `tpm-monitor` (статус за 15 мин), `tpm-monitor watch` (live), `tpm-monitor peak` (топ пиков)
- Пороги: 🟡 400K, 🔴 600K tokens/min

### Данные из agentsview
- `agentsview usage daily` — таблица по дням (все токены)
- `tpm-monitor` — per-minute с cache reads

## [2026-06-19 20:16] Meteora Alert — реализован и забектещен

### Что сделано
1. **config.py** — новый блок `METEORA` с фильтрами:
   - MC: $50K-$20M, ликвидность: $10K+, холдеры: 50+
   - Безопасность мягкая (renounced необязателен, tax до 10%)
   - Vol/MC: от 0.2x
   - Пороги: pass 50, strong_buy 65, super_call 80

2. **scoring.py** — `score_meteora()` со своими весами:
   - Security: 10 (мягко)
   - Dev: 15 (track record)
   - Holders: 25 (ключевой — распределение + объём)
   - SM: 15
   - Volume: 15
   - Social: 15 (реальные проекты)
   - Technical: 5

3. **scanner.py** — 3 новые функции:
   - `discover_meteora()` — ищет через `pool_meteora` + `meteora_virtual_curve` (24h)
   - `pre_filter_meteora()` — мягкий префильтр под Meteora
   - Интеграция в `run_scan_cycle()` — 5-я стратегия (после V3, до Scalp)
   - Дип-анализ использует `score_meteora()` для Meteora-токенов

### Результаты бектеста
- **NEST** ($6.5M, 10 SM, 3 KOL, 1176 holders) → **77/100 — Strong Buy** 🚀
- **USA** ($74K, 0 SM, 1308 holders) → **58/100 — Pass** ✅

### Что дальше
- Алерт уже встроен в `run_scan_cycle()` — будет работать при следующем скане
- Telegram пока выключен (`TELEGRAM_ENABLED = False`)
- Для включения: `TELEGRAM_ENABLED = True` в config.py
- [2026-06-20 15:30:35] [session-end] Сессия завершена
- [2026-06-20 17:36:05] [general] gmgn analysis chain completed
- [2026-06-21 22:30:01] [general] Профилактика диска: очистил cache/npm/tmp/logs, freed 6GB, добавил правило профилактики в AGENTS.md
- [2026-06-21 22:32:19] [general] Доп. чистка: Docker лог (14GB) + ClawController (293MB) — freed ~14.3GB
- [2026-06-22 00:09:54] [general] Пайплайн Бот1→HotSniper→LLM→Бот2 готов: polling worker + processed_ca + alert-api
- [2026-06-23 20:46:50] [general] Alpha Feed: кастомная средняя колонка — trending 1m + SM signals (7,8,12) + композитный скор + % от ATH
- [2026-06-23 20:46:52] [session-end] Сессия завершена
- [2026-06-26 18:13:32] [general] Чистка диска: удалена рекурсия Knowledge (14G), ollama модели, go cache. Диск 100%→59%
- [2026-06-26 18:13:33] [session-end] Сессия завершена
- [2026-06-26 23:47:23] [general] Перестроил колонки Cyber Cabin: col-tr = Trending, col-sm скрыта
- [2026-07-03 03:25:47] [general] cleanup: checkpoint 3vYr...Qj4 -> flat, dreamer board purged of 42 walk-overload items, scan re-run
- [2026-07-03 03:25:49] [session-end] Сессия завершена
- [2026-07-03 20:59:55] [session-end] Сессия завершена
- [2026-07-03 21:07:32] [session-end] Сессия завершена
- [2026-07-03 21:07:35] [session-end] Сессия завершена
- [2026-07-03 21:07:35] [session-end] Сессия завершена
- [2026-07-03 21:10:04] [session-end] Сессия завершена
- [2026-07-03 21:10:14] [session-end] Сессия завершена
- [2026-07-03 21:34:41] [session-end] Сессия завершена
- [2026-07-03 22:52:51] [session-end] Сессия завершена
- [2026-07-03 22:52:59] [infra] Настроен проект lexa-project/ для OpenCode Desktop: opencode.json + systemd-сервис + startup.sh + AGENTS.md. Сервер на порту 3000
- [2026-07-03 22:53:14] [session-end] Сессия завершена
- [2026-07-03 22:56:37] [session-end] Сессия завершена
- [2026-07-04 01:16:07] [session-end] Сессия завершена
- [2026-07-04 03:04:01] [session-end] Сессия завершена
- [2026-07-04 03:04:22] [session-end] Сессия завершена
- [2026-07-04 03:04:42] [session-end] Сессия завершена
- [2026-07-04 03:05:12] [session-end] Сессия завершена
- [2026-07-04 03:15:29] [session-end] Сессия завершена
- [2026-07-04 03:15:29] [session-end] Сессия завершена
- [2026-07-04 03:16:15] [session-end] Сессия завершена
- [2026-07-04 03:18:53] [session-end] Сессия завершена
- [2026-07-04 03:18:54] [session-end] Сессия завершена
- [2026-07-04 03:18:54] [session-end] Сессия завершена
- [2026-07-04 03:22:40] [session-end] Сессия завершена
- [2026-07-04 03:23:08] [session-end] Сессия завершена
- [2026-07-04 03:23:30] [session-end] Сессия завершена
- [2026-07-04 03:24:22] [session-end] Сессия завершена
