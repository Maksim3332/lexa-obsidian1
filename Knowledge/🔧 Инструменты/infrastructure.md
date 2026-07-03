# Infrastructure

## Сервисы

| Сервис | Порт | Путь/URL | Статус |
|--------|------|----------|--------|
| Fasol Exporter | 9101 | `/opt/fasol-exporter/exporter.py` | Active |
| Twitter Scraper | 9102 | `/opt/twitter-scraper/scraper.py` | Mock mode |
| Dune Exporter | 9103 | `/opt/dune-exporter/exporter.py` | Active |
| Browser Server | 9105 | Playwright/Chromium headless | Active |
| Prometheus | 9091 | http://localhost:9091 | Active |
| Grafana | 3000 | http://vps67870791.hosteons.net:3000 | Active |
| LLM Proxy | 4010 | `/root/auto-trader/proxy.js` | Active |
| OpenCode Server | 4096 | Headless API | Active |

## Grafana
- **URL:** http://vps67870791.hosteons.net:3000
- **Login:** admin
- **Password:** LexaAgentoxa
- **Dashboards:**
  - Holder Intelligence: `fflulnrx6hbswc` (v6)
  - RKC — Real-Time: `dflulns19tc74e`

## API Keys
- **Fasol API Key:** fsl_live_aypvUEfwVw3KFZ0NidevLWH7N3qC8GfVE43Opqdg
- **Fasol API Base:** https://api.fasol.trade/trading_bot/agent
- **Dune Query ID:** 7482001 (All-in-One: volume, tokens, fees)

## LLM Proxy
- `/root/auto-trader/proxy.js` — Bun HTTP server
- Маппинг: gpt-4o → big-pickle, claude-opus → big-pickle, и т.д.
- systemd: `opencode-llm-proxy.service`

## Alert Rules (Fasol)

| Alert | ID | Trigger |
|-------|-----|---------|
| ⚡ Vibez Style — Serial DEXpaid | 16595 | Serial deployer + dex_paid + with_socials, MC<30K, age<10min, dev_track record |
| 🔥 DEX Paid + Fresh Entry | 16596 | Any dex_paid + with_socials, MC<50K, age<15min, vol_5m>5K |

## Meme Analyzer
- `/root/auto-trader/meme_analyzer.py` — LLM-анализ тикеров
- Результат: `~/lexa-knowledge/{TICKER}.md`
- Интеграция: exporter использует meme_score для корректировки growth_prob

## Knowledge Dashboard
- **URL:** http://vps67870791.hosteons.net:8080/knowledge/
- **Путь:** `/opt/system-viz/knowledge/index.html`
- **Описание:** Интерактивный граф базы знаний Lexa — связи между источниками, аналитикой, стратегиями, исполнением, памятью и правилами
- **Доступен:** через ссылку на Ecosystem Dashboard (:8080)

## Daily Scripts
- `/opt/fasol-exporter/daily-market-regime.sh` — ежедневный snapshot режима
- Cron: `0 8 * * *`
