"""Supply model shared by chart_supply_scenarios.py and chart_matched_path.py.
Licensed cultivation sites under four licensing scenarios, and plants started and harvested per month.
Every rate comes from Minnesota's own 2026 OCM data; see the ASSUMPTIONS block."""
import csv, os, textwrap, datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DATA = os.path.join(OUT, 'code', 'data')
SURF, INK, INK2, GRID = '#fcfcfb', '#0b0b0b', '#52514e', '#e6e5e0'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})

def ym(p): return int(p[:4]), int(p[5:7])
def add(p, k):
    y, m = ym(p); t = y * 12 + m - 1 + k; return f'{t // 12:04d}-{t % 12 + 1:02d}'
def D(p): y, m = ym(p); return dt.date(y, m, 1)

V = {}; SNAP = {}
for r in csv.DictReader(open(os.path.join(DATA, 'mn_supply.csv'))):
    if not r['value']: continue
    if r['period_type'] == 'month': V.setdefault(r['variable'], {})[r['period']] = float(r['value'])
    if r['period_type'] == 'snapshot': SNAP[(r['variable'], r['period'], r['source_name'])] = float(r['value'])
au, med, H, sites = V['plants_started_adult_use'], V['plants_started_medical'], V['plants_harvested'], V['licensed_cultivation_sites_recon']

# ---------------- ASSUMPTIONS (all from OCM data unless noted)
LAG = 4                                          # months from planting to harvest
hm = [p for p in sorted(H) if add(p, -LAG) in au]
SURV = sum(H[p] for p in hm) / sum(au[add(p, -LAG)] + med[add(p, -LAG)] for p in hm)   # harvested / started, May-Jul 2026
rate = {ym(p)[1]: au[p] / sites[p] for p in au}  # adult-use starts per licensed cultivation site, by calendar month (Jan-Jul 2026)
INDOOR = sum(rate[i] for i in (1, 2, 3, 4)) / 4
for i in range(8, 13): rate[i] = INDOOR          # Aug-Dec: no published data; Jan-Apr (indoor-season) average
MED = sum(med.values()) / len(med)               # medical starts per month, 2026 average
SAS = 'OCM Summary Application Data'
MICRO_SHARE = 112 / SNAP[('licensed_microbusinesses', '2026-09', SAS)]   # 112 of 276 microbusinesses hold a cultivation site (163 sites - 24 cultivator - 24 mezzo - 3 med combo)
POOL = {'micro': SNAP[('prelim_approvals_microbusiness', '2026-09', SAS)], 'mezzo': SNAP[('prelim_approvals_mezzobusiness', '2026-09', SAS)],
        'cult': SNAP[('prelim_approvals_cultivator', '2026-09', SAS)]}
# current pace: licenses issued Dec 2025 -> Sep 2026 (9 months)
MAR = '2025 Market Analysis Report'
def snap(v, p, src): return next(val for (vv, pp, ss), val in SNAP.items() if vv == v and pp == p and src in ss)
PACE = {'micro': (snap('licensed_microbusinesses', '2026-09', SAS) - snap('licensed_microbusinesses', '2025-12', MAR)) / 9,
        'mezzo': (snap('licenses_issued_mezzobusiness', '2026-09', SAS) - snap('licenses_issued_mezzobusiness', '2025-12', MAR)) / 9,
        'cult': (snap('licensed_cultivators', '2026-09', SAS) - snap('licensed_cultivators', '2025-12', MAR)) / 9}
SITES_NOW, NOW = 163, '2026-09'                  # OCM workbook, September 2026
FIRST, WINDOW = '2026-10', 30                    # conversions from Oct 2026 over 18 months plus up to 12 months of extensions (to Mar 2029)
END = '2029-12'

def site_path(frac=None):
    """Licensed cultivation sites by month. frac=None: current pace until each pool runs out."""
    s, left, out, p = SITES_NOW, dict(POOL), {NOW: SITES_NOW}, FIRST
    k = 0
    while p <= END:
        add_sites = 0.0
        for t in POOL:
            if frac is None: n = min(PACE[t], left[t]) if k < WINDOW else 0.0   # approvals expire after the window, as in the other scenarios
            else: n = POOL[t] * frac / WINDOW if k < WINDOW else 0.0
            left[t] -= n
            add_sites += n * (MICRO_SHARE if t == 'micro' else 1.0)
        s += add_sites; out[p] = s; p = add(p, 1); k += 1
    return out

def starts(p, sp):
    if p in au: return au[p] + med[p]
    n = sites.get(p, sp.get(p))
    return rate[ym(p)[1]] * n + MED

def harvest(p, sp):
    return H[p] if p in H else SURV * starts(add(p, -LAG), sp)

SCEN = [('All preliminary approvals', 1.0, '#154f99'), ('Three-quarters', 0.75, '#2a78d6'),
        ('Current pace', None, '#7a7872'), ('Half', 0.5, '#8fbbee')]
SP = {name: site_path(f) for name, f, _ in SCEN}
months = []; p = '2024-01'
while p <= END: months.append(p); p = add(p, 1)
months = [q for q in months if q >= '2024-01']
HV = {name: {p: harvest(p, SP[name]) for p in months if p > max(H)} for name, _, _ in SCEN}

