# Resume Context — Gem Team Pipeline

## Last command
python3 /opt/scripts/gem-pipeline/gem-scan.py sol 50 10000 200000

## Status
✅ Chart Score module — работает
✅ Bundle Detect — работает  
✅ Pipeline gem-analyze.sh — работает
✅ Batch scan gem-scan.py — работает, шлёт в TG
⚠️ Калибровка скоринга — НЕ сделана (все 20/25 проходят как GEM)

## How to resume
1. Ужесточить пороги в gem-analyze.sh:
   - Chart Score: повысить вес с 20% до 30%
   - Bundle: штраф -25 за bundler_rate >0.3
   - Social: снизить до 0 если нет Twitter
2. Запустить повторно: python3 /opt/scripts/gem-pipeline/gem-scan.py sol 50 10000 200000
3. После калибровки — интегрировать с Fasol Alert

## Quick cmds
gem-analyze.sh sol <ADDRESS>
python3 /opt/scripts/gem-pipeline/gem-scan.py sol 50 10000 200000
cat /tmp/gem-analysis-*.json

## Telegram
Bot: 8799632628:AAF6BQSlLckyq81Qt4InyHHVJwqjqQWOZus
Chat: 267693252
Account: +16727058188 (Al Hewitt) — слушает код входа
