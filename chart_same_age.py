"""'If Minnesota followed X': each state's real price change after its own month 10, applied to Minnesota's month-10 price.
No thresholds, no supply model, no floor. Reads harmonized_prices.csv (written by harmonize.py).
Outputs: charts/7_same_age_paths.png + chart_same_age_paths.csv (per gram, pre-tax) and
charts/8_same_age_eighth.png + chart_same_age_eighth.csv (out-the-door eighth)."""
import csv, os, textwrap, datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib.ticker import FuncFormatter

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SURF, INK, INK2, GRID = '#fcfcfb', '#0b0b0b', '#52514e', '#e6e5e0'
COL = {'MI': '#2a78d6', 'MA': '#eb6834', 'IL': '#eda100'}
NAME = {'MI': 'Michigan', 'MA': 'Massachusetts', 'IL': 'Illinois'}
STATES = ('MI', 'MA', 'IL')
START, YEARS = 10, 3            # Minnesota's latest reading is month 10 (12 months through July 2026)
END = START + 12 * YEARS        # month 46 = July 2029
MN_LAUNCH = (2025, 9)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})

S = {}
for r in csv.DictReader(open(os.path.join(OUT, 'harmonized_prices.csv'))):
    S.setdefault(r['state'], {})[int(r['months_since_launch'])] = (float(r['real_usd_per_g_2026-08']), r['period'])

def mdate(m):
    y, mo = MN_LAUNCH[0] + (MN_LAUNCH[1] - 1 + m) // 12, (MN_LAUNCH[1] - 1 + m) % 12 + 1
    return dt.date(y, mo, 1)

def src_month(s, m):
    y, mo = map(int, S[s][0][1].split('-')); k = mo - 1 + m
    return f'{y + k // 12:04d}-{k % 12 + 1:02d}'

mn = sorted((m, v) for m, (v, p) in S['MN'].items())
level = dict(mn)[START]
paths = {s: {m: level * S[s][m][0] / S[s][START][0] for m in range(0, END + 1) if m in S[s]} for s in STATES}  # monthly data as published, no smoothing; months 0-9 are each state's own first months, same scale

def draw(K, tag, png, unit_sub, ylab, ytick, dec, title_note='', title='If Minnesota follows the states that came before it'):
    # ---- data file
    P = {s: {m: v * K for m, v in paths[s].items()} for s in STATES}
    MNs = [(m, v * K) for m, v in mn]
    fmt = (lambda v: f'${v:,.{dec}f}')
    with open(os.path.join(OUT, f'chart_same_age_{tag}.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Month', 'Minnesota months since launch', f'Minnesota published ({ylab})'] +
                   [f'If Minnesota follows {NAME[s]}' for s in STATES] + [f'{NAME[s]} source month' for s in STATES] + ['Range low', 'Range high'])
        for m in range(0, END + 1):
            vals = [P[s].get(m) for s in STATES]
            w.writerow([mdate(m).strftime('%Y-%m'), m, round(dict(MNs)[m], 2) if m in dict(MNs) else None] +
                       [round(v, 2) if v is not None else None for v in vals] +
                       [src_month(s, m) if m >= START else None for s in STATES] +
                       ([round(min(v for v in vals if v is not None), 2), round(max(v for v in vals if v is not None), 2)] if m >= START else [None, None]))

    # ---- chart
    fig, ax = plt.subplots(figsize=(9.7, 6.0), dpi=150)
    fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
    fig.text(0.06, 0.955, title, fontsize=14.5, weight='bold', color=INK, va='top')
    sub = (unit_sub + ' Each line applies what happened to a state\'s price after its own '
           'tenth month of legal sales to Minnesota\'s price at its tenth month (July 2026). Faded lines: each state\'s first ten months.')
    fig.text(0.06, 0.908, '\n'.join(textwrap.wrap(sub, 128)), fontsize=9.5, color=INK2, va='top')
    src = ('Source: MN OCM (12-month median); MI CRA (ounce-weighted average), MA CCC (average), IL CROO (flower average); BLS Midwest CPI. '
           'State lines use each month\'s published price and percentage changes, not price levels; Massachusetts April 2020 (COVID closure) is omitted. The band spans the three lines; it is not a forecast range. '
           'Minnesota\'s dashed line joins its two published readings; the months between are not published.' + title_note + ' Analysis by Tanner Berris.')
    fig.text(0.06, 0.018, '\n'.join(textwrap.wrap(src, 150)), fontsize=7.5, color=INK2, va='bottom')

    xs = [mdate(m) for m in range(START, END + 1)]
    lo = [min(P[s][m] for s in STATES if m in P[s]) for m in range(START, END + 1)]
    hi = [max(P[s][m] for s in STATES if m in P[s]) for m in range(START, END + 1)]
    NAN = float('nan')
    ax.fill_between(xs, lo, hi, color='#8a8983', alpha=0.12, lw=0)
    DY = {'MI': 0, 'IL': 1.0, 'MA': -1.0}  # keep the Illinois and Massachusetts end labels apart
    mon = lambda p: dt.date(int(p[:4]), int(p[5:7]), 1).strftime('%b %Y')
    for s in STATES:
        early = [P[s].get(m, NAN) for m in range(0, START + 1)]
        ax.plot([mdate(m) for m in range(0, START + 1)], early, color=COL[s], lw=1.6, alpha=0.4)
        ys = [P[s].get(m, NAN) for m in range(START, END + 1)]  # a missing month breaks the line
        ax.plot(xs, ys, color=COL[s], lw=2)
        ax.plot([xs[-1]], [ys[-1]], 'o', color=COL[s], ms=4)
        lab = f'If it follows {NAME[s]}: {fmt(ys[-1])}\nData: {mon(src_month(s, 0))} to {mon(src_month(s, END))}'.replace('$', r'\$')
        ax.text(xs[-1] + dt.timedelta(days=25), ys[-1] + DY[s] * K, lab, color=INK2, fontsize=8, va='center', linespacing=1.3)
    # Minnesota's two published 12-month medians, joined by a thin dashed line (months between are not published)
    ax.plot([mdate(m) for m, _ in MNs], [v for _, v in MNs], color=INK, lw=1.2, ls=(0, (3, 2)), zorder=4)
    ax.plot([mdate(m) for m, _ in MNs], [v for _, v in MNs], 'o', color=INK, ms=7, zorder=5)
    for m, v in MNs:
        ax.annotate(fmt(v).replace('$', r'\$'), (mdate(m), v), xytext=(0, -16), textcoords='offset points', ha='center', fontsize=8, color=INK)
    ax.text(mdate(MNs[0][0]) + dt.timedelta(days=100), MNs[0][1] - 2.4 * K, 'Minnesota, published\n12-month medians', fontsize=8.5, color=INK, weight='bold', ha='center', va='top')
    # key: which color is which state (Illinois and Massachusetts end close together)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], color=COL[x], lw=2.5, label=f'If it follows {NAME[x]}') for x in ('MA', 'IL', 'MI')]
    handles.append(Line2D([], [], color=INK, lw=1.2, ls=(0, (3, 2)), marker='o', ms=6, label='Minnesota, published'))
    leg = ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.0, 0.93), frameon=True, fontsize=8.5, labelcolor=INK2,
                    handlelength=2.2, borderpad=0.7, facecolor=SURF, edgecolor=GRID)
    leg.get_frame().set_linewidth(0.8)
    # year markers along the paths
    for k in (1, 2, 3):
        m = START + 12 * k
        ax.axvline(mdate(m), color=GRID, lw=0.8, zorder=0)
        ax.text(mdate(m), 20.3 * K, f'{k} year{"s" if k > 1 else ""} on', fontsize=8, color=INK2, ha='center', va='bottom')

    for sp in ('top', 'right', 'left'): ax.spines[sp].set_visible(False)
    ax.spines['bottom'].set_color(INK2)
    ax.grid(axis='y', color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(colors=INK2, labelsize=9, length=0)
    ax.set_ylim(0, 21.2 * K); ax.set_xlim(dt.date(2025, 8, 1), dt.date(2029, 9, 1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(ytick)); ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'${v:,.0f}'))
    ax.xaxis.set_major_locator(md.YearLocator()); ax.xaxis.set_major_formatter(md.DateFormatter('%Y'))
    ax.set_xlabel('Year', color=INK2, fontsize=9)
    ax.set_ylabel(ylab, color=INK2, fontsize=9)
    plt.subplots_adjust(left=0.08, right=0.78, top=0.79, bottom=0.17)
    fig.savefig(os.path.join(OUT, 'charts', png), facecolor=SURF); plt.close(fig)
    for s in STATES:
        print(tag, NAME[s], {k: round(P[s][START + 12 * k], 2) for k in (1, 2, 3)}, 'source months', src_month(s, START), '->', src_month(s, END))

OTD = 1 + 0.15 + 0.06875   # 15% cannabis tax + 6.875% state sales tax
draw(1.0, 'paths', '7_same_age_paths.png',
     'Minnesota flower price per gram, pre-tax, in August 2026 dollars.', 'Price per gram, pre-tax (August 2026 dollars)', 3, 2)
draw(3.5 * OTD, 'eighth', '8_same_age_eighth.png',
     'Price of an eighth (3.5 grams) with the 15% cannabis tax and 6.875% sales tax, in August 2026 dollars.',
     'Price of an eighth, with tax (August 2026 dollars)', 15, 0,
     ' Eighth = 3.5 x gram price x 1.21875; Minneapolis adds about 2%.', title='What an eighth could cost if Minnesota follows other states')
