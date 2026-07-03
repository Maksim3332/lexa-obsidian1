# Telegram → Open Notebook Bridge

**Дата:** 2026-06-10
**Статус:** ✅ Production

## Схема работы

```
Пользователь (Telegram) → Telegram Bot → Open Notebook API → Lexa (supermemory)
```

1. Пользователь отправляет ссылку Telegram-боту (`@...`)
2. Бот (`telegram-notebook-bridge.py`) создаёт source в Open Notebook (`POST /api/sources/json`)
3. Open Notebook скачивает контент (статья, YouTube субтитры, PDF)
4. Lexa через `notebook-bridge.sh` может:
   - `ask <question>` — Q&A по загруженным материалам
   - `search <query>` — поиск источников
   - `import <query>` — найти релевантное и сохранить в supermemory
   - `sync` — проверить новые источники
5. При старте сессии AGENTS.md выводит сводку новых источников

## Компоненты

| Файл | Назначение |
|------|-----------|
| `/usr/local/bin/telegram-notebook-bridge.py` | Telegram bot (polling) |
| `/etc/systemd/system/telegram-notebook-bridge.service` | systemd unit |
| `/usr/local/bin/notebook-bridge.sh` | CLI для взаимодействия с Open Notebook |
| `/var/log/telegram-notebook-bridge.log` | Лог бота |

## Open Notebook

- Web UI: `http://82.29.72.151:8502`
- REST API: `http://localhost:5055`
- SurrealDB: порт 8000
- Docker Compose: `/opt/open-notebook/docker-compose.yml`

## API эндпоинты

- `POST /api/sources/json` — создание источника (type: link/upload/text)
- `GET /api/sources` — список источников
- `GET /api/sources/{id}` — детали источника + контент
- `POST /api/search/ask/simple` — Q&A с RAG контекстом

## Проанализированные материалы

1. **«КАК НЕ ПРОЕБАТЬ ВСЕ ДЕНЬГИ В ЩИТКАХ. ЧАСТЬ 2»** (nemiroffdao) — [MEDIUM CONFIDENCE]
   - Советы по анализу монет, DEV, фильтрам
   - Большая часть уже реализована в Fasol Scanner
2. **«Хочешь результата? Спросили у 15 криптанов»** (nemiroffdao) — [MEDIUM CONFIDENCE]
   - 15 трейдеров (>69K подписчиков) делятся инсайтами
   - Пересекается с нашим подходом (трекинг кошельков, контроль рисков)
3. **TagMarkets обзор** (YouTube, канал «Думай Действуй») — [LOW CONFIDENCE]
   - Forex copy-trading, аффилиат-обзор
   - Не релевантно (FX ≠ Solana on-chain)
