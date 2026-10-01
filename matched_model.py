"""Matched-market scenario model, shared by chart_matched_path.py and matched_sensitivity.py.

The scenario: if Minnesota's legal flower market moves through the same price/throughput relationship Michigan's did,
what path would Minnesota's adult-use flower price take? It is a scenario, not a causal estimate: the throughput measure is
legal flower SOLD per adult, a market outcome shaped by production, demand and price together.

Rules (all parameters in BASE; every one is varied in matched_sensitivity.py):
  1. Throughput on both sides = average legal flower sold per adult 21+ per month over the trailing 12 months (Michigan's first
     year: months since launch). basis='combined' counts adult-use + medical flower, as OCM's 12-month volume card does;
     basis='adult_use' counts adult-use flower only on both sides, with Minnesota's medical sales held at their observed level.
  2. Anchor: Michigan's month `anchor_k` (base: month 10, Oct 2020), the same market age as Minnesota's latest published data
     (July 2026). Until Minnesota's throughput reaches Michigan's at the anchor, the scenario price stays at Minnesota's
     starting level. This is an anchoring point, not a claimed universal threshold.
  3. After that, each month the scenario price = starting level x Michigan's adult-use price in the first month (from the anchor on)
     its throughput reached Minnesota's / Michigan's price at the anchor. Only Michigan's percentage changes are used.
  4. Optional monthly speed limit `cap` (base: the steepest five-month fall in any comparison state, as a monthly rate).
Starting level: OCM's 12-month adult-use flower median through July 2026 ($14.29), in August 2026 dollars. It is a trailing
median, not a July shelf price; Minnesota publishes no monthly price.
Minnesota flower sold = harvested plants x grams per plant (calibrated to OCM's 12-month flower card), spread over `sell` months
starting `sale_lag` months after harvest. The 12-month spread is the best fit to Michigan's own harvest and sales records
(CRA, sales Jun 2022 - Aug 2026; see michigan_harvest_fit.py)."""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'src'))
import supply_model as SM
from supply_model import add, ym
from common import flower_grams_sold, per_adult, pop21, primary_series, index_series, LAUNCH, add_months, G_PER_OZ, G_PER_LB, rd

POP = pop21('MN', 2024)
START, END = '2026-07', '2029-12'
MN_LEVEL = 14.588064215342042          # OCM 12-month adult-use median through July 2026 ($14.29), August 2026 dollars
MN_OBS = [('2025-12', 14.0189), ('2026-07', MN_LEVEL)]
MAIN = 'Current pace'
months = [add('2025-08', i) for i in range(60) if add('2025-08', i) <= END]
CAL = [add('2025-08', i) for i in range(12)]   # OCM 12-month card window, Aug 2025 - Jul 2026

# ---- Minnesota observed 12-month flower volume (OCM), ounces
TTM = {r['variable']: float(r['value']) for r in csv.DictReader(open(os.path.join(SM.DATA, 'mn_supply.csv')))
       if r['period'] == '2026-07' and r['period_type'] == 'ttm' and r['variable'] in ('flower_sold_oz_adult_use', 'flower_sold_oz_medical')}
TTM_AU, TTM_MED = TTM['flower_sold_oz_adult_use'], TTM['flower_sold_oz_medical']
TTM_OZ = TTM_AU + TTM_MED
MED_G = TTM_MED * G_PER_OZ / 12        # medical flower per month, held at its observed 12-month level (medical sales ran about
                                       # $8M a month in late 2025 and in the year to Sep 2026; medical plant starts 9-13k a month in 2026)

def avg12(series, p, first):
    win = [q for q in (add(p, -j) for j in range(12)) if q >= first]
    return sum(series[q] for q in win) / len(win) if win and all(q in series for q in win) else None

# ---- Michigan: 12-month average legal flower sold per adult, combined and adult-use only; adult-use real price
MI_G = {'combined': flower_grams_sold()['MI'],
        'adult_use': {r['period']: float(r['value']) * G_PER_LB for r in rd('supply_MI.csv')
                      if r['period_type'] == 'month' and r['variable'] == 'flower_sold_lbs_adult_use'}}
MI12 = {}
for b, g in MI_G.items():
    x = per_adult('MI', g)
    MI12[b] = {p: v for p, v in ((p, avg12(x, p, LAUNCH['MI'])) for p in x) if v is not None}
I = index_series(primary_series())
PMI = {v[0]: v[2] for v in I['MI'].values()}   # Michigan adult-use ounce-weighted average, real $/g

def steepest(st, k=5):
    pr = {v[0]: v[2] for v in I[st].values()}
    return min((pr[add(p, k)] / pr[p], st, p) for p in pr if add(p, k) in pr)
STEEPEST = min(steepest(st) for st in ('MI', 'MA', 'IL', 'CT', 'OH'))   # (ratio, state, start month)
MAX_MONTHLY_FALL = 1 - STEEPEST[0] ** (1 / 5)
STATE_NAME = {'MI': 'Michigan', 'MA': 'Massachusetts', 'IL': 'Illinois', 'CT': 'Connecticut', 'OH': 'Ohio'}

BASE = dict(basis='combined', anchor_k=10, cap=MAX_MONTHLY_FALL, surv=None, lag=4, sale_lag=1, sell=12,
            scen=MAIN, outdoor_mult=1.0, absorb=1.0)

def surv_for(lag):
    """Share of started plants harvested: OCM harvests May-Jul 2026 / starts `lag` months earlier."""
    hm = [p for p in sorted(SM.H) if add(p, -lag) in SM.au]
    return sum(SM.H[p] for p in hm) / sum(SM.au[add(p, -lag)] + SM.med[add(p, -lag)] for p in hm)

def mn_sold(scen, surv, lag, sale_lag, sell, outdoor_mult):
    """Minnesota flower sold per month (grams, adult-use + medical) and the calibrated grams per harvested plant."""
    sp = SM.SP[scen]
    rate = dict(SM.rate)
    for k in (5, 6, 7): rate[k] *= outdoor_mult
    def starts(p):
        if p in SM.au: return SM.au[p] + SM.med[p]
        return rate[ym(p)[1]] * SM.sites.get(p, sp.get(p)) + SM.MED
    def harvest(p): return SM.H[p] if p in SM.H else surv * starts(add(p, -lag))
    def sh(p): return sum(harvest(add(p, -sale_lag - j)) for j in range(sell)) / sell
    gpp = TTM_OZ * G_PER_OZ / sum(sh(p) for p in CAL)   # calibration months use observed harvests only
    return gpp, {p: gpp * sh(p) for p in months}

def scenario(**kw):
    o = {**BASE, **kw}
    surv = o['surv'] if o['surv'] is not None else surv_for(o['lag'])
    gpp, sold = mn_sold(o['scen'], surv, o['lag'], o['sale_lag'], o['sell'], o['outdoor_mult'])
    if o['absorb'] != 1.0:
        b = sold[START]; sold = {p: v if p <= START else b + o['absorb'] * (v - b) for p, v in sold.items()}
    au = {p: v - MED_G for p, v in sold.items()}                   # adult-use flower per month
    mn = au if o['basis'] == 'adult_use' else sold
    X12 = {p: avg12({q: mn[q] / POP for q in mn}, p, '2025-08') for p in months}
    mi12 = MI12[o['basis']]
    anchor = add_months(LAUNCH['MI'], o['anchor_k']); hold = mi12[anchor]
    mim = sorted(p for p in mi12 if p in PMI and p >= anchor)
    target, price, prev = {}, {}, MN_LEVEL
    for p in months:
        if p < START: continue
        if X12[p] < hold: t, m = MN_LEVEL, 'hold'
        else:
            m = next((q for q in mim if mi12[q] >= X12[p]), None)
            t = MN_LEVEL * PMI[m] / PMI[anchor] if m else None
        v = (max(t, prev * (1 - o['cap'])) if o['cap'] else t) if t is not None else None
        target[p], price[p] = (t, m), (v, m)
        if v is not None: prev = v
    hold_end = next((p for p in months if p >= START and X12[p] >= hold), None)
    return dict(opts=o, surv=surv, gpp=gpp, sold=sold, au=au, X12=X12, anchor=anchor, hold=hold, hold_end=hold_end,
                target=target, price=price)

def ttm_oz(r, p, which='sold'):
    win = [add(p, -j) for j in range(12)]
    return sum(r[which][q] for q in win) / G_PER_OZ if all(q in r[which] for q in win) else None

def rolling(r, p):
    """What a trailing 12-month figure built from the scenario would show, weighted by adult-use volume.
    Returns (volume-weighted average, volume-weighted median of monthly prices). The median version treats every sale in a
    month as made at that month's scenario price; OCM's median is taken over its own transaction data and will differ."""
    win = [q for q in (add(p, -j) for j in range(12)) if q >= '2025-09']   # adult-use sales began September 2025
    if any(q not in r['au'] for q in win): return None, None
    pr = {q: (r['price'][q][0] if q in r['price'] and r['price'][q][0] else MN_LEVEL) for q in win}
    w = {q: max(r['au'][q], 0.0) for q in win}
    avg = sum(pr[q] * w[q] for q in win) / sum(w.values())
    tot, cum = sum(w.values()), 0.0
    for q in sorted(win, key=lambda q: pr[q]):
        cum += w[q]
        if cum >= tot / 2: return avg, pr[q]
    return avg, None

def summary(r, checks=('2027-07', '2028-01', '2029-01')):
    return [r['hold_end']] + [r['price'][p][0] for p in checks]
