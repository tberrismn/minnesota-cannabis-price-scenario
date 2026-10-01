"""Minnesota supply scenarios from licenses and OCM plant data. No prices, no thresholds.
Top: licensed cultivation sites. Bottom: plants harvested per month (the OCM dashboard measure) and per year.
The model itself is in supply_model.py. Outputs: charts/9_supply_scenarios.png, charts/9_supply_scenarios_yearly.png,
chart_supply_scenarios.csv, chart_supply_yearly.csv"""
from supply_model import *
from supply_model import os, csv, textwrap, dt, plt, md, FuncFormatter, Line2D

# ---------------- data file
with open(os.path.join(OUT, 'chart_supply_scenarios.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Month', 'Observed licensed cultivation sites', 'Observed plants harvested'] +
               [f'Sites: {n}' for n, _, _ in SCEN] + [f'Plants harvested: {n}' for n, _, _ in SCEN] + ['Harvest basis'])
    for p in months:
        basis = 'observed' if p in H else ('published plant starts' if add(p, -LAG) in au else 'projected starts')
        w.writerow([p, sites.get(p, SITES_NOW if p == NOW else None), H.get(p)] +
                   [round(SP[n][p], 1) if p in SP[n] else None for n, _, _ in SCEN] +
                   [round(HV[n][p]) if p in HV[n] else None for n, _, _ in SCEN] + [basis])

# ---------------- chart
fig = plt.figure(figsize=(9.7, 8.4), dpi=150); fig.patch.set_facecolor(SURF)
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.9], hspace=0.3, left=0.09, right=0.8, top=0.83, bottom=0.135)
fig.text(0.06, 0.965, 'How much cannabis Minnesota could grow as licenses convert', fontsize=14.5, weight='bold', color=INK, va='top')
sub = ('Licensed cultivation sites and plants harvested per month under four licensing scenarios for the 975 microbusiness, 48 mezzobusiness '
       'and 19 cultivator preliminary approvals. Harvests through November 2026 come from plants already started, so every scenario matches until then.')
fig.text(0.06, 0.93, '\n'.join(textwrap.wrap(sub, 137)), fontsize=9.3, color=INK2, va='top')
src = (f'Source: MN OCM Cannabis Market Monitor (plants started and harvested), OCM license workbook and Summary Application Data (Sept. 21, 2026). '
       f'Assumptions from Minnesota\'s 2026 data: {MICRO_SHARE:.0%} of microbusinesses hold a cultivation site; each site starts plants at the 2026 rate for that '
       f'calendar month (Aug-Dec: January-April average, {INDOOR:.0f} per site); {SURV:.0%} of started plants are harvested {LAG} months later. Fractions convert '
       f'evenly Oct 2026-Mar 2029 (18 months plus 12 of extensions); current pace = {PACE["micro"]:.0f} microbusiness, {PACE["mezzo"]:.1f} mezzobusiness and '
       f'{PACE["cult"]:.1f} cultivator licenses a month (the Dec 2025-Sep 2026 rate) until Mar 2029. Approval dates are not published, so all scenarios assume the same deadline. Not a forecast. Analysis by Tanner Berris.')
fig.text(0.06, 0.012, '\n'.join(textwrap.wrap(src, 155)), fontsize=7.3, color=INK2, va='bottom')

def style(ax):
    ax.set_facecolor(SURF)
    for sp in ('top', 'right', 'left'): ax.spines[sp].set_visible(False)
    ax.spines['bottom'].set_color(INK2); ax.grid(axis='y', color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(colors=INK2, labelsize=9, length=0)
    ax.set_xlim(dt.date(2025, 1, 1), dt.date(2030, 1, 1))
    ax.xaxis.set_major_locator(md.YearLocator()); ax.xaxis.set_major_formatter(md.DateFormatter('%Y'))

DEADLINE = add(FIRST, WINDOW)   # first month with no conversions: April 2029
def deadline(ax, ytext):
    x = D(DEADLINE)
    ax.axvline(x, color=INK2, lw=1, ls=(0, (2, 2)), zorder=1)
    ax.text(x - dt.timedelta(days=12), ytext, 'Approvals expire:\n18-month window plus\n12 months of extensions\nends March 2029', fontsize=7.3, color=INK2, ha='right', va='top')

def endlab(ax, x, y, text, dy=0):
    ax.text(x + dt.timedelta(days=30), y + dy, text, fontsize=8, color=INK2, va='center')

# top: sites
a1 = fig.add_subplot(gs[0]); style(a1)
obs = sorted(sites.items()) + [(NOW, SITES_NOW)]
a1.plot([D(p) for p, _ in obs], [v for _, v in obs], color=INK, lw=2.2)
for name, f_, col in SCEN:
    pts = sorted(SP[name].items())
    a1.plot([D(p) for p, _ in pts], [v for _, v in pts], color=col, lw=1.8, ls=(0, (4, 2)) if name != 'Current pace' else (0, (1.5, 1.5)))
    endlab(a1, D(pts[-1][0]), pts[-1][1], f'{name}: {pts[-1][1]:.0f}', dy={'Three-quarters': 22, 'Current pace': -22}.get(name, 0))
a1.set_ylabel('Licensed cultivation sites', color=INK2, fontsize=9); deadline(a1, 250)
a1.text(dt.date(2026, 3, 1), SITES_NOW + 40, f'{SITES_NOW} sites\n(Sept. 2026)', fontsize=8, color=INK, ha='center')
a1.set_ylim(0, max(max(v.values()) for v in SP.values()) * 1.15)
a1.text(0.0, 1.06, 'Licensed cultivation sites', transform=a1.transAxes, fontsize=10.5, weight='bold', color=INK)

# bottom: harvests
a2 = fig.add_subplot(gs[1], sharex=a1); style(a2)
a2.axvspan(D('2026-08'), D('2026-12'), color=INK2, alpha=0.08, lw=0)
ymax = max(max(v.values()) for v in HV.values()) * 1.1
a2.text(D('2026-10'), ymax * 0.36, 'Already\nplanted', fontsize=8, color=INK2, ha='center', va='top')
ho = sorted(H.items())
a2.plot([D(p) for p, _ in ho], [v for _, v in ho], color=INK, lw=2.2)
last = max(H)
for name, f_, col in SCEN:
    pts = [(last, H[last])] + sorted(HV[name].items())
    a2.plot([D(p) for p, _ in pts], [v for _, v in pts], color=col, lw=1.6, ls=(0, (4, 2)) if name != 'Current pace' else (0, (1.5, 1.5)))
a2.annotate(f'Observed\n{H[last]:,.0f} (July 2026)', (D(last), H[last]), xytext=(-70, 40), textcoords='offset points', fontsize=8, color=INK,
            arrowprops=dict(arrowstyle='-', color=INK, lw=0.8))
a2.set_ylim(0, ymax)
a2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v/1000:,.0f}k' if v else '0'))
a2.set_ylabel('Plants harvested per month', color=INK2, fontsize=9); a2.set_xlabel('Year', color=INK2, fontsize=9)
a2.text(0.0, 1.03, 'Plants harvested per month', transform=a2.transAxes, fontsize=10.5, weight='bold', color=INK)
handles = [Line2D([], [], color=INK, lw=2.2, label='Observed')] + \
          [Line2D([], [], color=c, lw=1.8, ls=(0, (4, 2)) if n != 'Current pace' else (0, (1.5, 1.5)), label=n + (f' (about {min(1, PACE["micro"] * WINDOW / POOL["micro"]):.0%} of microbusinesses)' if n == 'Current pace' else '')) for n, _, c in SCEN]
a2.legend(handles=handles, loc='upper left', bbox_to_anchor=(0.01, 0.99), frameon=True, facecolor=SURF, edgecolor=GRID, fontsize=8.3, labelcolor=INK2, handlelength=2.4)
plt.setp(a1.get_xticklabels(), visible=False)
fig.savefig(os.path.join(OUT, 'charts', '9_supply_scenarios.png'), facecolor=SURF)

print('survival', round(SURV, 3), 'indoor/site', round(INDOOR), 'med', round(MED), 'micro share', round(MICRO_SHARE, 3), 'pace', {k: round(v, 2) for k, v in PACE.items()})
for n, _, _ in SCEN:
    print(n, 'sites', {q: round(SP[n][q]) for q in ('2027-06', '2027-12', '2028-12', '2029-12')},
          'harvest', {q: round(HV[n][q]) for q in ('2026-11', '2027-03', '2027-10', '2028-10', '2029-10')})

# ================= yearly version: plants harvested per calendar year (sums of the monthly figures above)
YEARS = list(range(2024, 2030))
ORDER = ['Half', 'Current pace', 'Three-quarters', 'All preliminary approvals']
CC = {n: c for n, _, c in SCEN}
def year_total(y, name):
    obs = sum(v for p, v in H.items() if p.startswith(str(y)))
    proj = sum(v for p, v in HV[name].items() if p.startswith(str(y)))
    return obs, proj
YT = {n: {y: year_total(y, n) for y in YEARS} for n in ORDER}
with open(os.path.join(OUT, 'chart_supply_yearly.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Year', 'Scenario', 'Observed plants harvested', 'Projected plants harvested', 'Total', 'Licensed cultivation sites at year end'])
    for y in YEARS:
        for n in ORDER:
            o, pr = YT[n][y]; se = SP[n].get(f'{y}-12', sites.get(f'{y}-12'))
            w.writerow([y, n if pr else 'Observed', round(o), round(pr), round(o + pr), round(se) if se else None])

fig = plt.figure(figsize=(9.7, 8.4), dpi=150); fig.patch.set_facecolor(SURF)
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.7], hspace=0.34, left=0.09, right=0.8, top=0.83, bottom=0.135)
fig.text(0.06, 0.965, 'How much cannabis Minnesota could grow as licenses convert', fontsize=14.5, weight='bold', color=INK, va='top')
sub = ('Licensed cultivation sites and plants harvested per year under four licensing scenarios for the 975 microbusiness, 48 mezzobusiness '
       'and 19 cultivator preliminary approvals. 2026 is largely settled: harvests through November come from plants already started.')
fig.text(0.06, 0.93, '\n'.join(textwrap.wrap(sub, 137)), fontsize=9.3, color=INK2, va='top')
fig.text(0.06, 0.012, '\n'.join(textwrap.wrap(src.replace('Not a forecast.', 'Yearly bars are sums of monthly harvests. Not a forecast.'), 155)), fontsize=7.3, color=INK2, va='bottom')

a1 = fig.add_subplot(gs[0]); style(a1)
a1.plot([D(p) for p, _ in obs], [v for _, v in obs], color=INK, lw=2.2)
for name, f_, col in SCEN:
    pts = sorted(SP[name].items())
    a1.plot([D(p) for p, _ in pts], [v for _, v in pts], color=col, lw=1.8, ls=(0, (4, 2)) if name != 'Current pace' else (0, (1.5, 1.5)))
    endlab(a1, D(pts[-1][0]), pts[-1][1], f'{name}: {pts[-1][1]:.0f}', dy={'Three-quarters': 22, 'Current pace': -22}.get(name, 0))
a1.text(dt.date(2026, 3, 1), SITES_NOW + 40, f'{SITES_NOW} sites\n(Sept. 2026)', fontsize=8, color=INK, ha='center')
a1.set_ylim(0, max(max(v.values()) for v in SP.values()) * 1.15)
a1.set_ylabel('Licensed cultivation sites', color=INK2, fontsize=9); deadline(a1, 250)
a1.text(0.0, 1.06, 'Licensed cultivation sites', transform=a1.transAxes, fontsize=10.5, weight='bold', color=INK)
a1.set_xlabel('Year', color=INK2, fontsize=9)
# line the years up with the bar chart below: each year spans the same width, labeled at mid-year, ending with 2029
a1.set_xlim(dt.date(2024, 1, 1), dt.date(2030, 1, 1))
a1.set_xticks([dt.date(y, 7, 1) for y in YEARS]); a1.set_xticklabels([str(y) for y in YEARS])
for y in YEARS[1:]: a1.axvline(dt.date(y, 1, 1), color=GRID, lw=0.6, zorder=0)

a2 = fig.add_subplot(gs[1]); a2.set_facecolor(SURF)
for sp in ('top', 'right', 'left'): a2.spines[sp].set_visible(False)
a2.spines['bottom'].set_color(INK2); a2.grid(axis='y', color=GRID, lw=0.8); a2.set_axisbelow(True)
a2.tick_params(colors=INK2, labelsize=9, length=0)
BW, GAP = 0.19, 0.02
for i, y in enumerate(YEARS):
    o, pr = YT['Half'][y]
    if pr == 0 or y == 2026:   # observed years, and 2026 (identical in every scenario): one bar
        a2.bar(i, o, width=0.5, color=INK)
        if pr: a2.bar(i, pr, bottom=o, width=0.5, color=SURF, edgecolor=INK, hatch='////', lw=1)
        a2.text(i, o + pr, f'{(o + pr) / 1000:,.0f}k', ha='center', va='bottom', fontsize=8, color=INK)
        continue
    for j, n in enumerate(ORDER):
        o, pr = YT[n][y]; x = i + (j - 1.5) * (BW + GAP)
        a2.bar(x, o + pr, width=BW, color=CC[n], edgecolor=CC[n])
        a2.text(x, o + pr, f'{(o + pr) / 1e6:.1f}M' if o + pr >= 1e6 else f'{(o + pr) / 1000:,.0f}k', ha='center', va='bottom', fontsize=6.8, color=INK2)
a2.set_xlim(-0.5, len(YEARS) - 0.5); a2.set_xticks(range(len(YEARS))); a2.set_xticklabels([str(y) for y in YEARS])
a2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: (f'{v/1e6:.1f}M' if v >= 1e6 else f'{v/1000:,.0f}k') if v else '0'))
a2.set_ylabel('Plants harvested per year', color=INK2, fontsize=9); a2.set_xlabel('Year', color=INK2, fontsize=9)
a2.text(0.0, 1.03, 'Plants harvested per year', transform=a2.transAxes, fontsize=10.5, weight='bold', color=INK)
import matplotlib.patches as mpatches
h2 = [mpatches.Patch(color=INK, label='Observed'), mpatches.Patch(facecolor=SURF, edgecolor=INK, hatch='////', label='2026: from plants already started\nand the current sites (same in all scenarios)')] + \
     [mpatches.Patch(color=CC[n], label=n + (f' (about {min(1, PACE["micro"] * WINDOW / POOL["micro"]):.0%} of microbusinesses)' if n == 'Current pace' else '')) for n in ORDER]
a2.legend(handles=h2, loc='upper left', bbox_to_anchor=(0.01, 0.99), frameon=True, facecolor=SURF, edgecolor=GRID, fontsize=8, labelcolor=INK2)
fig.savefig(os.path.join(OUT, 'charts', '9_supply_scenarios_yearly.png'), facecolor=SURF)
for y in YEARS: print(y, {n: round(sum(YT[n][y])) for n in ORDER})
