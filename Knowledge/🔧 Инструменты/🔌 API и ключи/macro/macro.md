# Macro Ecosystem Metrics — Dune + Aggregators

## Risk Regime
- **Current:** aggressive
- **Last Updated:** 2026-05-13T19:40
- **Modifier:** 5% to growth_probability
- **Reasoning:** automated from macro data

## Metrics Table

*Только Pump.fun и Bonk. Другие launchpad'ы (Raydium, Meteora) — не отслеживаются.*

| timestamp | solana_dex_volume_24h | pumpfun_volume_24h | bonk_volume_24h | tokens_launched_24h | migrated_tokens_24h | active_traders_24h | regime |
|---|---|---|---|---|---|---|---|
| 2026-05-13T19:40 | 1967096625 | 65231694 | 0 | 23442 | 0 | 96906 | aggressive |

## Risk Rules
- **conservative** — TP ×1.3-1.5, fast exit, low allocation (modifier: -5%)
- **moderate** — TP ×1.5-2.5, standard allocation (modifier: 0%)
- **aggressive** — TP ×2-5, hold longer, higher allocation (modifier: +5%)
- **anomaly** — TP ×3-10, max allocation, season detected (modifier: +10%)

## Day-over-Day Change Tracking
| date | regime | pnl_day | pnl_cumulative | notes |
|---|---|---|---|---|
