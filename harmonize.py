"""Step 1: harmonize, deflate and index every state's monthly retail flower price.
Writes harmonized_prices.csv (read by chart_same_age.py).
  - Comparison states: one primary retail flower price series per state (src/common.py, primary_series), in nominal $/g,
    deflated to the latest published BLS CPI-U Midwest month (August 2026 dollars).
  - Minnesota: OCM's trailing 12-month adult-use flower medians, deflated by the average CPI over the adult-use months in
    each window (a 12-month median mixes prices from across the window).
Massachusetts April 2020 (COVID retail closure) is omitted."""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'src'))
from common import LAUNCH, CPI, CPI_BASE_MONTH, add_months, msl, primary_series, index_series, rd

OUT = os.path.abspath(os.path.join(HERE, '..'))
STATES = ['MA', 'MI', 'IL', 'CT', 'OH']
I = index_series(primary_series())
rows = []
for st in STATES:
    for m, (p, nom, rl, ix) in sorted(I[st].items()):
        rows.append([st, p, m, round(nom, 4), round(rl, 4), round(ix, 2)])
obs = []
for r in rd('mn_prices.csv'):
    if r['market'] != 'adult_use': continue
    end = r['period']; m_end = msl('MN', end)
    months = [add_months(LAUNCH['MN'], k) for k in range(max(0, m_end - 11), m_end + 1)]   # adult-use portion of the 12-month window
    cpi_avg = sum(CPI[p] for p in months) / len(months)
    obs.append((m_end, end, float(r['value']), float(r['value']) * CPI[CPI_BASE_MONTH] / cpi_avg))
obs.sort(); base = obs[0][3]
for m, p, nom, rl in obs:
    rows.append(['MN', p, m, nom, round(rl, 4), round(100 * rl / base, 2)])
with open(os.path.join(OUT, 'harmonized_prices.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['state', 'period', 'months_since_launch', 'nominal_usd_per_g', f'real_usd_per_g_{CPI_BASE_MONTH}', 'index_m0to2_eq_100'])
    w.writerows(rows)
print('harmonized_prices.csv:', len(rows), 'rows; prices in', CPI_BASE_MONTH, 'dollars')
