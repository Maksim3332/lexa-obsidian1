# Сессия 23 May 2026 — Сканер починен, алерты летят

## Ключевые решения
- **TOLYBOT** — MC: $558K. Ждём 0.4 SOL вход, SL $300K, TP $800K-1.2M
- **BUFFDON** — держать (Euronews альбинос-буйвол, CTO, rescue mission)
- **USDP** — держать до SL $30K MC
- **Ryker** — вышли (мёртвый)
- Wallet: 0.435 SOL (~$37), портфель ~$146
- Пари TOLYBOT: Дима $800K vs Лёха $880K — проверить кто выиграл

## Fasol Scanner — статус
- ✅ Сканер запущен (systemd, перезапускается сам)
- ✅ Баг с `sm_data` починен
- ✅ Ссылка на кошелёк GMGN поправлена (`/address/`)
- ✅ Ссылка Fasol поправлена (`/coin/`)
- ✅ GMGN первая ссылка в алерте — превью с картинкой токена
- ✅ Алерты летят в TG (бот токен + чат ID в env)
- ✅ Дедуп — один алерт на токен навсегда
- DexScreener API (CTO + Boosts) — работает
- Социальный анализ (Twitter, Instagram, News) — работает
- Smart Money данные в алертах — подтягиваются

## Telegram Bot
- Старый SM трекер (`/opt/fasol-telegram/bot.py`) — неактуален, SM уже в сканере

## Что не доделано
- Парсинг DexDegens чата (отложено)
- Возможно понадобится настройка TG бота для Лёхи

## Инфраструктура
- Fasol Scanner: порт 9101, systemd, /opt/fasol-scanner/
- Telegram: bot token + chat id в env
- Prometheus: порт 9091
- Grafana: порт 3000, admin/LexaAgentoxa
- Fasol Journal: порт 9200
