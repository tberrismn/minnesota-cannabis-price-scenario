"""Checks two supply-model parameters against Michigan's own records (CRA monthly reports: plants harvested, flower sold by weight).
  1. Sell-through: which spread of each month's harvest over later months best reproduces Michigan's monthly flower sales?
     Model form (the same as Minnesota's): sold(p) = g x mean(harvested plants in months p-lag-11 ... p-lag) for a window of w months.
  2. Grams of flower sold per harvested plant, the fitted g, as an outside check on Minnesota's calibrated figure.
Because harvests and sales both trend upward, the in-sample R-squared in levels overstates how well the spread is identified.
Three stricter checks are reported for each window:
  - out-of-sample error: g fitted on the first half of the sample (sales Jun 2022 - Jun 2024), error on the second half,
    as RMSE in % of mean sales;
  - rolling one-step error: for each month from the 19th on, g fitted on all earlier months, error on that month (RMSE %);
  - detrended fit: R-squared between the two series after removing a linear time trend from each (the share of
    month-to-month variation around the trend that harvest timing explains).
Sample: Michigan sales Jun 2022 - Aug 2026 (every window up to 18 months with lag up to 2 has harvest data; CRA's monthly
harvest counts start Oct 2020, adult-use + medical). Output: michigan_harvest_fit.csv"""
import csv, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'src'))
from common import rd, add_months, G_PER_LB

d = {}
for r in rd('supply_MI.csv'):
    if r['period_type'] == 'month' and r['variable'] in ('plants_harvested_adult_use', 'plants_harvested_medical', 'flower_sold_lbs_adult_use', 'flower_sold_lbs_medical'):
        d.setdefault(r['variable'], {})[r['period']] = float(r['value'])
H = {p: d['plants_harvested_adult_use'][p] + d['plants_harvested_medical'][p] for p in d['plants_harvested_medical'] if p in d['plants_harvested_adult_use']}
S = {p: (d['flower_sold_lbs_adult_use'][p] + d['flower_sold_lbs_medical'][p]) * G_PER_LB for p in d['flower_sold_lbs_medical']}
FIRST_SALE = '2022-06'

def fit(lag, w):
    ps = [p for p in sorted(S) if p >= FIRST_SALE and all(add_months(p, -lag - j) in H for j in range(w))]
    x = np.array([sum(H[add_months(p, -lag - j)] for j in range(w)) / w for p in ps]); y = np.array([S[p] for p in ps]); n = len(y)
    slope = lambda a, b: (a @ b) / (a @ a)                                  # least squares through the origin
    g = slope(x, y)
    r2 = 1 - ((y - g * x) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    k = n // 2; gk = slope(x[:k], y[:k])
    oos = np.sqrt(np.mean((y[k:] - gk * x[k:]) ** 2)) / y[k:].mean() * 100
    err = [y[i] - slope(x[:i], y[:i]) * x[i] for i in range(18, n)]
    roll = np.sqrt(np.mean(np.square(err))) / y[18:].mean() * 100
    T = np.c_[np.ones(n), np.arange(n)]
    dt = lambda v: v - T @ np.linalg.lstsq(T, v, rcond=None)[0]
    rd_ = np.corrcoef(dt(x), dt(y))[0, 1]
    return float(g), float(r2), n, float(oos), float(roll), float(max(rd_, 0.0) ** 2)

rows = [(lag, w) + fit(lag, w) for lag in (0, 1, 2) for w in range(1, 19)]
if __name__ == '__main__':
    with open(os.path.join(HERE, '..', 'michigan_harvest_fit.csv'), 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['Months from harvest to first sale', 'Months each harvest sells over', 'Grams sold per harvested plant (fitted)', 'R-squared (levels)',
                     'Months of sales fitted', 'Out-of-sample RMSE, second half (% of mean sales)', 'Rolling one-step RMSE (% of mean sales)', 'R-squared after removing linear trend'])
        for lag, w, g, r2, n, oos, roll, dr2 in rows: wr.writerow([lag, w, round(g, 1), round(r2, 3), n, round(oos, 1), round(roll, 1), round(dr2, 3)])
    best = max(rows, key=lambda r: r[3])
    print('best overall: lag', best[0], 'window', best[1], 'g', round(best[2], 1), 'R2', round(best[3], 3))
    for lag, w, g, r2, n, oos, roll, dr2 in rows:
        if lag == 1 and w in (5, 6, 8, 11, 12, 13, 18): print('lag 1 window', w, 'g', round(g, 1), 'R2', round(r2, 3), 'oos', round(oos, 1), 'roll', round(roll, 1), 'detrended', round(dr2, 3), 'n', n)
    for lag in (0, 1, 2):
        sub = [r for r in rows if r[0] == lag]
        print('lag', lag, 'best by oos', min(sub, key=lambda r: r[5])[1], 'by rolling', min(sub, key=lambda r: r[6])[1], 'by detrended', max(sub, key=lambda r: r[7])[1])
