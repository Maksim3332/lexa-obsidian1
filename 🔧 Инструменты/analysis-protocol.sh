#!/bin/bash
# ============================================================
# Анализатор токенов — протокол с принудительными шагами
# Использование: bash analysis-protocol.sh <CONTRACT_ADDRESS>
# ============================================================

ADDR=$1
if [ -z "$ADDR" ]; then
  echo "Usage: bash analysis-protocol.sh <CONTRACT_ADDRESS>"
  exit 1
fi

echo "╔══════════════════════════════════════════════╗"
echo "║  ПРОТОКОЛ АНАЛИЗА ТОКЕНА                     ║"
echo "║  Адрес: $ADDR"
echo "╚══════════════════════════════════════════════╝"

# Шаг 0: Базовая инфа
echo ""
echo "═══ ШАГ 0: БАЗОВАЯ ИНФА ═══"
gmgn-cli token info --chain sol --address "$ADDR" 2>&1 | head -20
echo "---"
gmgn-cli token security --chain sol --address "$ADDR" 2>&1 | head -15
echo "---"
gmgn-cli token pool --chain sol --address "$ADDR" 2>&1 | head -10

# Подсказка по Шагу 1
echo ""
echo "═══ ШАГ 1: СОЦСЕТИ (ОБЯЗАТЕЛЬНО ПРОВЕРИТЬ) ═══"
echo "⚠️  НЕ ПРОПУСТИ! Проверь Twitter/Telegram/Website"
echo "⚠️  Twitter handle может быть KOL, а не проектом"
echo "⚠️  Используй: gmgn-cli token info --raw | grep twitter"
echo ""
gmgn-cli token info --chain sol --address "$ADDR" --raw 2>/dev/null | python3 -c "
import json, sys
d = json.load(sys.stdin)
link = d.get('link', {})
print(f'Twitter: @{link.get(\"twitter_username\", \"-\")}')
print(f'Website: {link.get(\"website\", \"-\")}')
print(f'Telegram: {link.get(\"telegram\", \"-\")}')
print(f'Description: {link.get(\"description\", \"-\")}')
"
echo ""
echo ">>> ОТКРОЙ ССЫЛКИ И ПРОЧИТАЙ <<<"

# Шаг 2: Рынок
echo ""
echo "═══ ШАГ 2: РЫНОК ═══"
gmgn-cli token info --chain sol --address "$ADDR" --raw 2>/dev/null | python3 -c "
import json, sys
d = json.load(sys.stdin)
p = d.get('price', {})
sup = float(d.get('circulating_supply', '1'))
price = float(p.get('price', 0))
mc = price * sup
ath = float(d.get('ath_price', 0))
ath_mc = ath * sup
from_ath = (mc/ath_mc - 1) * 100 if ath_mc else 0
print(f'Price: \${price:.8f}')
print(f'MC: \${mc:,.0f}')
print(f'ATH MC: \${ath_mc:,.0f}  |  From ATH: {from_ath:.1f}%')
print(f'Liq: \${float(d.get(\"liquidity\", 0)):,.0f}')
print(f'Vol 24h: \${float(p.get(\"volume_24h\", 0)):,.0f}')
print(f'Swaps 24h: {p.get(\"swaps_24h\", 0)}')
print(f'Buys/Sells: {p.get(\"buys_24h\", 0)}/{p.get(\"sells_24h\", 0)}')
print(f'Price 1h ago: \${p.get(\"price_1h\", \"?\")}')
print(f'Price 6h ago: \${p.get(\"price_6h\", \"?\")}')
print(f'Hot level: {p.get(\"hot_level\", \"?\")}')
print(f'OG: {d.get(\"og\", \"?\")}  |  CTO: {d.get(\"dev\", {}).get(\"cto_flag\", \"?\")}')
print(f'Launchpad: {d.get(\"launchpad\", \"?\")}  |  Status: {d.get(\"launchpad_status\", \"?\")}')
"

# Шаг 3: Холдеры
echo ""
echo "═══ ШАГ 3: ХОЛДЕРЫ ═══"
gmgn-cli token holders --chain sol --address "$ADDR" --limit 30 --raw 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
holders = data.get('list', [])
wallets = [h for h in holders if h.get('addr_type') == 0]
print(f'Всего холдеров (искл. пулы): {len(wallets)}')
for i, w in enumerate(wallets[:20]):
    pct = float(w.get('amount_percentage', 0)) * 100
    profit = float(w.get('profit', 0))
    sell_pct = float(w.get('sell_amount_percentage', 0)) * 100
    usd_val = float(w.get('usd_value', 0))
    tags = ','.join(w.get('maker_token_tags', [])) or '-'
    profit_str = f'+{profit:.0f}' if profit >= 0 else f'{profit:.0f}'
    print(f'{i+1}. {w[\"address\"][:8]}... | {pct:.2f}% | \${usd_val:.0f} | P&L={profit_str} | sold={sell_pct:.0f}% | {tags}')
"

# Шаг 4: SM и KOL
echo ""
echo "═══ ШАГ 4: SMART MONEY ═══"
echo "--- SM holders ---"
gmgn-cli token holders --chain sol --address "$ADDR" --tag smart_degen --limit 20 --order-by amount_percentage --raw 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
items = data.get('list', [])
print(f'SM с позицией: {len([w for w in items if float(w.get(\"amount_percentage\",0)) > 0])}')
print(f'Всего SM: {len(items)}')
for w in items[:10]:
    pct = float(w.get('amount_percentage', 0)) * 100
    profit = float(w.get('profit', 0))
    sell_pct = float(w.get('sell_amount_percentage', 0)) * 100
    if pct > 0:
        profit_str = f'+{profit:.0f}' if profit >= 0 else f'{profit:.0f}'
        print(f'  {w[\"address\"][:8]}... | {pct:.2f}% | P&L={profit_str} | sold={sell_pct:.0f}%')
"

echo "--- KOL holders ---"
gmgn-cli token holders --chain sol --address "$ADDR" --tag renowned --limit 20 --order-by amount_percentage --raw 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
items = data.get('list', [])
print(f'KOL с позицией: {len([w for w in items if float(w.get(\"amount_percentage\",0)) > 0])}')
print(f'Всего KOL: {len(items)}')
for w in items[:10]:
    pct = float(w.get('amount_percentage', 0)) * 100
    profit = float(w.get('profit', 0))
    sell_pct = float(w.get('sell_amount_percentage', 0)) * 100
    name = w.get('name', 'anon')
    profit_str = f'+{profit:.0f}' if profit >= 0 else f'{profit:.0f}'
    print(f'  {name:20s} | {pct:.2f}% | P&L={profit_str} | sold={sell_pct:.0f}%')
"

echo ""
echo "═══ ПРОТОКОЛ ЗАВЕРШЁН ═══"
echo "⚠️  НЕ ЗАБУДЬ:"
echo "  1. Открыть Twitter/Telegram ссылки"
echo "  2. Кто владелец? (KOL? Аноним?)"
echo "  3. Какой нарратив?"
echo "  4. Вердикт: 🟢 / 🟡 / 🔴"
