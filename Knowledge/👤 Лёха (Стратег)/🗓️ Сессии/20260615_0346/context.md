# Session: Scalp Alert Optimization + Profit Backtest
## Date: 2026-06-15

## Goal
Optimize scalp alert for maximum 1.5x hit rate at useful volume (2-4 tokens/day at 80%+).

## Achievements

### Alert Config: "scalp V3 81%" (ID=19384)
- Launchpads: pf
- Boolean: only_migrated
- Filters: MC 50-150K, liq≥20K, vol≥80K, holders≥100, top10≤20%, bot_fee<$5
- Performance: 81% 1.5x, 56% 2x, 17% 5x at 7.2/day (36 coins/5d)
- Autobuy: 0.0001 SOL, TP 1.5x (trigger_p:50), SL -20% (trigger_p:-20)

### Key Findings
1. MC sweet spot: 80-150K (peak hit rate)
2. bot_fee as MAX cap (<$5) improves hit rate by ~8%; as MIN cap destroys it
3. holders 100-500 all give ~73% — no strong sensitivity
4. dev_hold_p filter rejected by user
5. Best config evolved: sweet_nosocial (74%) → multi_base (72%) → clean4 (83%/1.2d) → scalp V3 81% (81%/7.2d)

### Profit Backtest (36 coins, 5d, 1 SOL entry)
- TP 1.5x, SL -20%: 81% win, +36% ROI ($883 net, ~$24.5/trade)
- TP 2.0x, SL -20%: 56% win, +47% ROI ($1133) — higher profit, lower win rate
- TP 1.3x, SL -20%: 83% win, +22% ROI ($526) — conservative
- TP 1.5x, SL -30%: 81% win, +34% ROI ($836)

### Blockers
- Wallet A4v9wfoe3N7HhcxLPVQA82w4u8ePBYxoNXPdHRSTjn9n has 0 SOL — needs funding for autobuy
- #10 top public alert (ID=16502, 100% 1.5x) filter config unknown — requires login to fasol.trade

### Open Items
1. Fund wallet for autobuy
2. Possibly test dex_paid, cashback_coin, or tighter MC (80-150K) to push beyond 81%
3. Can inspect #10 alert if user provides login
