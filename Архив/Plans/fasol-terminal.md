# Проект: Fasol Terminal

**Статус:** Building
**Created:** 30 May 2026
**Сервис:** FastAPI + HTML/JS, порт 9201
**Стиль:** 8-bit retro (пиксельная графика, CRT эффект)

## Концепция

Торговый терминал для ручного трейдинга по дип-алертам.
Не авто-сканер, а **визуальный интерфейс** для анализа и бумажной торговли.

## Архитектура

### Backend (FastAPI + SQLite)
```
/opt/fasol-terminal/
├── server.py           # FastAPI сервер (uvicorn)
├── static/
│   ├── index.html      # Терминал (Single Page App)
│   ├── style.css       # 8-bit тема
│   └── script.js       # Логика интерфейса
├── gmgn_cache.py       # GMGN API с кэшированием
├── paper_engine.py     # Бумажная торговая система
├── database.py         # SQLite: alerts + trades + кэш
├── config.toml         # Настройки TP/SL/баланс
└── fasol-terminal.service  # systemd unit
```

### Эндпоинты API
```
GET    /api/alerts?limit=N&offset=N&sort=field&order=asc|desc
POST   /api/alerts                  — добавить новый алерт
PATCH  /api/alerts/{id}             — архив/скрыть алерт
DELETE /api/alerts/{id}             — удалить алерт
GET    /api/token/{addr}            — данные токена (кэш 2-5 мин)
GET    /api/token/{addr}/kline?from=TS&to=TS  — kline (кэш ∞ для старого, 2м для свежего)
POST   /api/trade/entry             — открыть бумажную позицию { size_sol, tp_pct, sl_pct }
POST   /api/trade/exit/{id}         — закрыть позицию
GET    /api/portfolio               — баланс (5 SOL), открытые позиции, история, PnL
GET    /api/portfolio/history?limit=20  — история сделок
GET    /api/settings                — текущие настройки
PUT    /api/settings                — обновить настройки
```

### База данных (SQLite)
```
Таблица alerts:
- id INTEGER PRIMARY KEY
- symbol TEXT, address TEXT UNIQUE
- alert_price REAL, alert_mc REAL, alert_ts INTEGER
- ath_mc REAL, drop_pct REAL
- holders INTEGER, buy_sell_ratio REAL
- score INTEGER, status TEXT (active/archived)
- created_at TEXT

Таблица trades:
- id INTEGER PRIMARY KEY
- alert_id INTEGER REFERENCES alerts(id)
- entry_price REAL, entry_ts INTEGER
- size_sol REAL, tp_pct REAL, sl_pct REAL
- status TEXT (open/closed/stopped/timedout)
- exit_price REAL, exit_ts INTEGER
- pnl_sol REAL, pnl_pct REAL
- close_reason TEXT (tp/sl/timeout/manual)

Таблица cache:
- key TEXT PRIMARY KEY, value TEXT, expires_at INTEGER
```

### Frontend (SPA)
```
┌──────────────────────────────────────────────────┐
│  [FASOL TERMINAL v1.0]    BAL: 5.00 SOL           │
│  TP: 30% | SL: 30% | SIZE: 1 SOL                  │
├────────────────┬─────────────────────────────────┤
│ АЛЕРТЫ         │ ГРАФИК                          │
│                │                                 │
│ [TOKEN A]      │  📈 Candlestick chart           │
│  MC: $45K      │  🟢 Entry marker               │
│  📉 -72%       │  🔴 TP line (+30%)             │
│  B/S: 1.35     │  🔵 SL line (-30%)             │
│                │  Fib уровни: 0.382, 0.618       │
│ [TOKEN B]      │                                 │
│  MC: $12K      ├─────────────────────────────────┤
│  📉 -55%       │ ПОЗИЦИЯ:                        │
│  B/S: 0.8      │  Open: 0 | History: 3 trades   │
│                │  PnL: +0.42 SOL (+14%)          │
└────────────────┴─────────────────────────────────┘
```

### Стиль 8-bit
- Шрифт: Press Start 2P (Google Fonts)
- Цвета: #0a0a0a фон, #00ff41 зелёный, #ff0041 красный, #ffd000 жёлтый
- Эффекты: scan lines через CSS, pixel borders, CRT glow
- Иконки: Unicode символы вместо картинок
- Анимации: Typing effect, blink cursor

## TODO

### ✅ Обновления по фидбеку @oracle
- [x] SQLite вместо alerts.json
- [x] Загрузка pre-alert kline (50 свечей до алерта)
- [x] Time-stop 48h авто-закрытие позиций
- [x] Сохранение trades в SQLite
- [x] Progressive data loading (только для выбранного токена)
- [x] Default TP 25% / SL 15% (по данным post-mortem)
- [x] Pagination + sort/filter для алертов
- [x] Cache TTL по возрасту данных

### Фаза 1: Backend
- [ ] server.py + database.py + FastAPI роуты
- [ ] gmgn_cache.py (прогрессивная загрузка, TTL по возрасту)
- [ ] paper_engine.py (баланс, сделки, time-stop, PnL)
- [ ] Config (TP/SL/размер по умолчанию)
- [ ] Импорт старых алертов из sent_tokens.json

### Фаза 2: UI — 8-bit Terminal (@designer концепт)
- [ ] 8-bit CSS тема (CRT casing, scan lines, Press Start 2P)
- [ ] Boot animation sequence
- [ ] Alert list panel с карточками токенов
- [ ] Chart panel (Lightweight Charts + тема)
- [ ] Маркеры: Entry ▲, TP line (жёлтый), SL line (красный), Fib уровни (голубой)
- [ ] Pre-alert контекст (50 свечей до алерта)

### Фаза 3: Trading
- [ ] Trade control panel (TP/SL/Size инпуты)
- [ ] BUY/SELL кнопки (8-bit pixel)
- [ ] PnL дисплей (абсолютный + процентный)
- [ ] Открытые позиции + blink-индикатор
- [ ] История сделок
- [ ] Time-stop 48h авто-закрытие

### Фаза 4: Polish
- [ ] CRT эффекты (scan lines, glow, vignette)
- [ ] Звуковые эффекты (8-bit beeps)
- [ ] Keyboard shortcuts (SPACE: buy, ESC: cancel, ↑↓: navigate)
- [ ] Settings panel (TP/SL/размер)
- [ ] Счётчик лимитов GMGN в UI

## Связи
- GMGN API через gmgn-cli (существующий)
- Данные из прошлого сканера (alerts.json)
- Порт 9201 (systemd: fasol-terminal)
