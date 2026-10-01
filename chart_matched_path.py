"""Matched-market scenario chart: if Minnesota's legal flower market moves through the same price/throughput relationship
Michigan's did, what path would Minnesota's adult-use flower price take? Model: matched_model.py. Sensitivity tests:
matched_sensitivity.py. This is an illustrative scenario, not a causal estimate or a forecast.
Outputs: charts/10_matched_path.png, chart_matched_path.csv (also the tracking sheet), matched_path_sensitivity.csv, matched_path_adverse.csv"""
import csv, os, textwrap, datetime as dt
import matched_model as M
import matched_sensitivity as S
from supply_model import D, add, SURF, INK, INK2, GRID, plt, md, FuncFormatter, Line2D
from common import LAUNCH, add_months

OUT = M.SM.OUT
MI_BLUE, BAND = '#2a78d6', '#e3e2dc'
MON = lambda p: dt.date(int(p[:4]), int(p[5:7]), 1).strftime('%b %Y')
R = M.scenario()                          # base: adult-use + medical flower on both sides
A = M.scenario(basis='adult_use')         # same rule, adult-use flower only on both sides
proj = [p for p in M.months if p >= M.START]

# ---- sensitivity runs: every test in matched_sensitivity.py, both measures; the band is their monthly low and high
RUNS = [M.scenario(basis=b, **kw) for _, _, kw in S.TESTS for b in ('combined', 'adult_use')]
LO = {p: min(r['price'][p][0] for r in RUNS) for p in proj}
HI = {p: max(r['price'][p][0] for r in RUNS) for p in proj}
S.write(S.run(), 'matched_path_sensitivity.csv')
S.write(S.run_combos(), 'matched_path_adverse.csv')            # adverse combinations: reported separately, not part of the band

# ---- data file (also the tracking sheet: compare each row with the dashboard as months are published)
with open(os.path.join(OUT, 'chart_matched_path.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Month', 'Projected 12-month flower ounces, adult-use + medical (OCM card)', 'Projected 12-month flower ounces, adult-use only',
                'Legal flower sold per adult, 12-month average, adult-use + medical (g/month)', 'Legal flower sold per adult, 12-month average, adult-use only (g/month)',
                'Michigan month matched (adult-use + medical)', 'Scenario price, adult-use + medical measure ($/g, Aug 2026 $)',
                'Michigan month matched (adult-use only)', 'Scenario price, adult-use-only measure ($/g, Aug 2026 $)',
                'Lowest price across sensitivity tests', 'Highest price across sensitivity tests',
                'Trailing 12-month proxy: volume-weighted average of scenario price', 'Trailing 12-month proxy: volume-weighted median of monthly scenario prices'])
    for p in M.months:
        t, ta = M.ttm_oz(R, p), M.ttm_oz(R, p, 'au')
        pr, m = R['price'].get(p, (None, None)); pa, ma = A['price'].get(p, (None, None))
        avg, med = M.rolling(R, p) if p >= M.START else (None, None)
        rd = lambda v, k=2: round(v, k) if v is not None else None
        w.writerow([p, round(t) if t else None, round(ta) if ta else None, rd(R['X12'][p], 3), rd(A['X12'][p], 3),
                    m, rd(pr), ma, rd(pa), rd(LO.get(p)), rd(HI.get(p)), rd(avg), rd(med)])

# ---- chart
fig = plt.figure(figsize=(9.7, 9.4), dpi=150); fig.patch.set_facecolor(SURF)
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.5], hspace=0.3, left=0.09, right=0.8, top=0.855, bottom=0.16)
fig.text(0.06, 0.972, 'If Minnesota\'s price follows Michigan\'s as its legal flower sales grow', fontsize=14.5, weight='bold', color=INK, va='top')
sub = ('Illustrative matched-market scenario, not a forecast. Minnesota\'s price holds at its latest 12-month median until it sells as much flower '
       'per adult as Michigan did at month 10, then tracks Michigan\'s price at equal flower sold per adult.')
fig.text(0.06, 0.94, '\n'.join(textwrap.wrap(sub, 132)), fontsize=9.3, color=INK2, va='top')
src = (f'Source: MN OCM Cannabis Market Monitor (plants, harvests, 12-month flower volume, 12-month adult-use median price) and license data; MI CRA (flower sold, '
       f'harvests, adult-use ounce-weighted average price); U.S. Census ACS adults 21+; BLS Midwest CPI. Minnesota flower sold = harvested plants x {R["gpp"]:.0f} g '
       f'(calibrated to OCM\'s 12-month volume; Michigan sold about 94 g per harvested plant), selling over 12 months (the best fit to Michigan\'s harvest and sales '
       f'records); assumes the historical plant-to-sales relationship holds and added flower sells on that schedule. The starting level is OCM\'s trailing 12-month '
       f'median, not a July shelf price; only Michigan\'s percentage changes are used. Declines limited to {M.MAX_MONTHLY_FALL:.0%} a month, the steepest five-month '
       f'fall in any comparison state ({M.STATE_NAME[M.STEEPEST[1]]}, from {MON(M.STEEPEST[2])}). Flower sold is a market outcome, not supply alone. Analysis by Tanner Berris.')
fig.text(0.06, 0.012, '\n'.join(textwrap.wrap(src, 158)), fontsize=7.2, color=INK2, va='bottom')

def style(ax):
    ax.set_facecolor(SURF)
    for sp in ('top', 'right', 'left'): ax.spines[sp].set_visible(False)
    ax.spines['bottom'].set_color(INK2); ax.grid(axis='y', color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(colors=INK2, labelsize=9, length=0)
    ax.set_xlim(dt.date(2025, 8, 1), dt.date(2030, 1, 1))
    ax.xaxis.set_major_locator(md.YearLocator()); ax.xaxis.set_major_formatter(md.DateFormatter('%Y'))

# top: 12-month average legal flower sold per adult (adult-use + medical)
a1 = fig.add_subplot(gs[0]); style(a1)
X12 = R['X12']; MI12 = M.MI12['combined']
OBS12 = M.TTM_OZ / 12 * M.G_PER_OZ / M.POP
a1.plot([D(p) for p in proj], [X12[p] for p in proj], color=INK, lw=2, ls=(0, (4, 2)))
mi_same = [(add('2025-09', k), add_months(LAUNCH['MI'], k)) for k in range(0, 60)]
mi_same = [(p, q) for p, q in mi_same if q in MI12 and p <= M.END]
a1.plot([D(p) for p, _ in mi_same], [MI12[q] for _, q in mi_same], color=MI_BLUE, lw=1.8)
for k in (12, 24, 36, 48):
    p, q = add('2025-09', k), add_months(LAUNCH['MI'], k)
    if q in MI12 and p <= M.END:
        a1.plot([D(p)], [MI12[q]], 'o', color=MI_BLUE, ms=5, zorder=5)
        a1.annotate(f'Michigan, {MON(q)}\n(year {k // 12})', (D(p), MI12[q]), xytext=(6, 14) if k == 12 else (-6, 8), textcoords='offset points', ha='left' if k == 12 else 'right', fontsize=7.5, color=INK2)
a1.axhline(R['hold'], color=MI_BLUE, lw=0.9, ls=(0, (2, 2)), zorder=1)
a1.text(D('2029-12'), R['hold'] + 0.12, f'Michigan at month 10 (Oct 2020): {R["hold"]:.2f} g, the anchoring point', fontsize=7.5, color=INK2, ha='right', va='bottom')
a1.plot([D(M.START)], [OBS12], 'o', color=INK, ms=7, zorder=6)
a1.annotate(f'Minnesota, observed\n{OBS12:.2f} g (July 2026)', (D(M.START), OBS12), xytext=(D('2025-09'), 2.3), textcoords='data', fontsize=7.8, color=INK,
            arrowprops=dict(arrowstyle='-', color=INK, lw=0.7))
a1.set_ylim(0, max(max(v for v in X12.values() if v), max(MI12[q] for _, q in mi_same)) * 1.18)
a1.set_ylabel('Grams per adult 21+ per month', color=INK2, fontsize=9)
a1.text(0.0, 1.05, 'Legal flower sold per adult each month (adult-use + medical), 12-month average', transform=a1.transAxes, fontsize=10.5, weight='bold', color=INK)
a1.legend(handles=[Line2D([], [], color=INK, lw=2, ls=(0, (4, 2)), label='Minnesota, projected (current licensing pace)'),
                   Line2D([], [], color=INK, lw=0, marker='o', ms=6, label='Minnesota, observed (OCM 12-month total)'),
                   Line2D([], [], color=MI_BLUE, lw=1.8, marker='o', ms=5, label='Michigan at the same months since launch')],
          loc='upper left', frameon=True, facecolor=SURF, edgecolor=GRID, fontsize=8, labelcolor=INK2)

# bottom: price
a2 = fig.add_subplot(gs[1], sharex=a1); style(a2)
a2.fill_between([D(p) for p in proj], [LO[p] for p in proj], [HI[p] for p in proj], step='post', color=BAND, lw=0, zorder=1)
a2.plot([D(p) for p in proj], [R['price'][p][0] for p in proj], color=INK, lw=2.2, drawstyle='steps-post', zorder=4)
a2.plot([D(p) for p, _ in M.MN_OBS], [v for _, v in M.MN_OBS], color=INK, lw=1.2, ls=(0, (1, 1.5)), zorder=4)
a2.plot([D(p) for p, _ in M.MN_OBS], [v for _, v in M.MN_OBS], 'o', color=INK, ms=7, zorder=5)
for p, v in M.MN_OBS:
    a2.annotate(f'\\${v:.2f}', (D(p), v), xytext=(0, -16), textcoords='offset points', ha='center', fontsize=8, color=INK)
a2.annotate(f'Stays at the latest 12-month median until flower\nsold per adult reaches Michigan\'s month-10 level ({MON(R["hold_end"])})',
            (D('2026-10'), M.MN_LEVEL), xytext=(D('2026-08'), 16.2), textcoords='data', fontsize=7.5, color=INK2, ha='left', va='bottom')
a2.text(D('2025-08') + dt.timedelta(days=10), 12.2, 'Minnesota, published\n12-month medians', fontsize=8.3, color=INK, weight='bold', ha='left', va='top')
for p, word in (('2027-07', 'about \\$9'), ('2028-01', 'about \\$5'), ('2029-01', 'about \\$3')):
    v = R['price'][p][0]
    a2.annotate(f'{word} ({MON(p)})', (D(p), v), xytext=(5, 9), textcoords='offset points', ha='left', fontsize=8, color=INK, weight='bold')
a2.set_ylim(0, 18); a2.yaxis.set_major_locator(plt.MultipleLocator(3))
a2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'${v:,.0f}'))
a2.set_ylabel('Adult-use flower price per gram, pre-tax\n(August 2026 dollars)', color=INK2, fontsize=9); a2.set_xlabel('Year', color=INK2, fontsize=9)
a2.text(0.0, 1.03, 'Price per gram if Minnesota follows Michigan at the same flower sold per adult', transform=a2.transAxes, fontsize=10.5, weight='bold', color=INK)
a2.legend(handles=[Line2D([], [], color=INK, lw=2.2, label='Minnesota, illustrative matched-market scenario'),
                   plt.Rectangle((0, 0), 1, 1, color=BAND, lw=0, label=f'Range across base + {len(S.TESTS) - 1} one-at-a-time\nsensitivity tests, incl. adult-use-only runs'),
                   Line2D([], [], color=INK, lw=1.2, ls=(0, (1, 1.5)), marker='o', ms=6, label='Minnesota, published 12-month medians')],
          loc='lower left', frameon=True, facecolor=SURF, edgecolor=GRID, fontsize=8, labelcolor=INK2)
plt.setp(a1.get_xticklabels(), visible=False)
fig.savefig(os.path.join(OUT, 'charts', '10_matched_path.png'), facecolor=SURF)

if __name__ == '__main__':
    print('grams per harvested plant', round(R['gpp'], 1), 'anchor', R['anchor'], 'hold level', round(R['hold'], 3), 'observed MN 12-mo avg', round(OBS12, 3))
    for p in ('2026-07', '2026-10', '2027-01', '2027-03', '2027-04', '2027-07', '2027-10', '2028-01', '2028-07', '2029-01', '2029-07', '2029-12'):
        pr, m = R['price'][p]; pa, ma = A['price'][p]; avg, med = M.rolling(R, p)
        print(p, 'x12', round(R['X12'][p], 2), 'MI', m, 'price', round(pr, 2), '| AU', ma, round(pa, 2), '| band', round(LO[p], 2), round(HI[p], 2),
              '| trailing avg', round(avg, 2), 'median', round(med, 2), '| card oz', round(M.ttm_oz(R, p)))
