# Session: 28 May 2026 — Post-Analysis v2 + Scanner MC fix + Local ATH

## Что сделано

### 1. token-post-analysis.py — полный рефакторинг
- **Схема**: 5ч → 24ч → 72ч вместо ежедневных батчей
- **Smart wallets**: до 100 SM трейдеров, фильтр `start_holding_at < alert_ts` (только зашедшие ДО алерта)
- **Top holders**: топ-10 по доле
- **Порог роста**: 50% от MC при алерте
- **Миграция**: 160 старых токенов конвертированы из `check_count` → `next_check_idx`
- **Батч**: до 50 токенов за запуск, ±4h tolerance
- **Cron**: 0 3,11,19 * * * (3x в день)

### 2. Baseline MC fix — правильный % от алерта
- **Проблема**: Первый снапшот (T+5h) становился базой, % от алерта терялся
- **Фикс**: При добавлении токена в трекинг сразу захватывается baseline MC
- **Scanner токены**: `mc_at_alert` из sent_tokens.json (новый формат с MC/timestamp)
- **Journal токены**: `mc_at_alert` из alert_tokens.json (уже был)
- **Telegram токены**: baseline MC захватывается при первом появлении в трекинге
- **Расчёт %**: всегда от `mc_at_alert`, не от `snapshots[0].mc`

### 3. Local ATH через K-line
- При каждом снапшоте: `gmgn-cli market kline --resolution 15m --from X --to Y`
- Период: от alert_ts или от предыдущего снапшота до сейчас
- Сохраняется в snapshot: `local_ath_mc`, `local_ath_price`, `local_ath_time`
- Отчёт: ATH 🏆 + % ATH колонки
- ATH обновляется если новый период даёт более высокую цену

### 4. Scanner (alerter.py) — SentTokens с MC/timestamp
- `SentTokens` теперь хранит объекты `{address, market_cap, symbol, timestamp}`
- 116 старых записей мигрированы
- `mark_sent(addr, token_data)` передаёт MC и symbol

## Статус
- 30 токенов: next_check_idx=1 (ждут 24h check) — сработают в ~19:00 UTC
- 130 токенов: next_check_idx=0 (ждут 5h check)
- Базы кошельков пусты (ждут первые 50%+ профиты)
- В отчёте появились колонки ATH 🏆

## TODO (на будущее)
- Проверить результаты первого прогона после миграции
- Оценить скорость K-line запросов, при необходимости сменить resolution на 5m
