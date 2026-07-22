# NHL Franchise Valuation Forecasting Model

A Python model that forecasts NHL franchise valuations through 2030 for the
Toronto Maple Leafs, Columbus Blue Jackets, Florida Panthers, and Edmonton
Oilers — built as a self-directed project to learn Python while exploring
the growing intersection of private equity and professional sports.

## Why this project

I'm interested in breaking into sports-focused private equity, and instead
of just reading about the space, I wanted to build something in it. This
was also my first coding project (I had never written a line of Python
before starting this).

## How it works

- **Data**: each team's 2025 valuation (Forbes), plus the NHL's league-wide
  average valuation for 2022 ($1.01B) and 2025 ($2.20B)
- **Growth rate**: a single league-wide CAGR (compound annual growth rate,
  ~29.6%/yr) is derived from those two league-average figures and applied
  to all four teams — rather than giving each team its own historical
  growth rate. An earlier version did use per-team rates, but that broke
  down with the Florida Panthers: their Stanley Cup run inflated their
  valuation enough that projecting their own historical growth forward
  implied an unrealistic future number. A shared, league-wide rate is a
  more defensible assumption.
- **Decay**: the growth rate tapers by 8% each year rather than staying
  flat through 2030, since the 2022-2025 stretch was an unusually strong
  period for the league (following the Four Nations Face-Off and the NHL's return to Olympic
  hockey) and isn't likely to continue at the same pace indefinitely.

## 2030 projections

| Team | 2025 valuation | 2030 projection |
|---|---|---|
| Toronto Maple Leafs | $4.30B | $13.24B |
| Edmonton Oilers | $2.76B | $8.50B |
| Florida Panthers | $1.89B | $5.82B |
| Columbus Blue Jackets | $1.40B | $4.31B |

## Limitations

- This is a directional model, not a professional valuation forecast
- Per-team historical data before 2025 is estimated, not independently sourced
- The 8% decay rate is an assumption, not derived from real data
- The model doesn't account for team-specific catalysts (new arenas, media
  deals,
