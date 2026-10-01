"""Sensitivity tables for the matched-market scenario, for both the combined (adult-use + medical) and adult-use-only
throughput measures.
  TESTS:  every rule and parameter varied one at a time (base + 20 tests). Output: matched_path_sensitivity.csv
  COMBOS: deliberately adverse combinations of logically separate assumptions, each pushing toward a later or smaller decline.
          The last one stacks every adverse test at once as a stress case; it double-counts related effects on purpose.
          Output: matched_path_adverse.csv"""
import csv, os
import matched_model as M

TESTS = [
    ('Base', 'Base', {}),
    ('Anchor', 'Michigan month 6 (Jun 2020)', {'anchor_k': 6}),
    ('Anchor', 'Michigan month 8 (Aug 2020)', {'anchor_k': 8}),
    ('Anchor', 'Michigan month 12 (Dec 2020)', {'anchor_k': 12}),
    ('Anchor', 'Michigan month 14 (Feb 2021)', {'anchor_k': 14}),
    ('Speed limit', 'None', {'cap': None}),
    ('Speed limit', '5% a month', {'cap': 0.05}),
    ('Speed limit', '15% a month', {'cap': 0.15}),
    ('Share of started plants harvested', '40%', {'surv': 0.40}),
    ('Share of started plants harvested', '80%', {'surv': 0.80}),
    ('Harvest lag', '3 months', {'lag': 3}),
    ('Harvest lag', '5 months', {'lag': 5}),
    ('Sale lag', '0 months', {'sale_lag': 0}),
    ('Sale lag', '2 months', {'sale_lag': 2}),
    ('Sell-through', '6 months', {'sell': 6}),
    ('Sell-through', '18 months', {'sell': 18}),
    ('Outdoor-season planting', 'Half the 2026 rate', {'outdoor_mult': 0.5}),
    ('Licensing', 'Half of approvals', {'scen': 'Half'}),
    ('Licensing', 'All approvals', {'scen': 'All preliminary approvals'}),
    ('Share of added flower that sells', '75%', {'absorb': 0.75}),
    ('Share of added flower that sells', '50%', {'absorb': 0.5}),
]
CHECKS = ('2027-07', '2028-01', '2029-01')

COMBOS = [
    ('Later anchor + slow price adjustment', 'Michigan month 14 anchor, 5% speed limit', {'anchor_k': 14, 'cap': 0.05}),
    ('Fewer plants harvested + weaker sales', '40% harvested, 75% of added flower sells', {'surv': 0.40, 'absorb': 0.75}),
    ('Fewer plants harvested + slower planting', '40% harvested, half the outdoor-season rate', {'surv': 0.40, 'outdoor_mult': 0.5}),
    ('Fewer plants harvested + fewer licenses', '40% harvested, half of approvals', {'surv': 0.40, 'scen': 'Half'}),
    ('Slow price adjustment + weak sales', '5% speed limit, 50% of added flower sells', {'cap': 0.05, 'absorb': 0.5}),
    ('Slow supply chain', '5-month harvest lag, 2-month sale lag, 18-month sell-through', {'lag': 5, 'sale_lag': 2, 'sell': 18}),
    ('Weak production and sales', '40% harvested, half outdoor rate, half of approvals, 75% sells', {'surv': 0.40, 'outdoor_mult': 0.5, 'scen': 'Half', 'absorb': 0.75}),
    ('Stress case: every adverse test at once', 'Month 14 anchor, 5% limit, 40% harvested, 50% sells, half outdoor rate, half of approvals, slow chain',
     {'anchor_k': 14, 'cap': 0.05, 'surv': 0.40, 'absorb': 0.5, 'outdoor_mult': 0.5, 'scen': 'Half', 'lag': 5, 'sale_lag': 2, 'sell': 18}),
]
COMBO_CHECKS = ('2027-07', '2028-01', '2029-01', '2029-12')

def first_below(r, share=0.75):
    """First month the scenario price is at least 25% below the starting level."""
    return next((p for p in sorted(r['price']) if r['price'][p][0] is not None and r['price'][p][0] <= M.MN_LEVEL * share), None)

def run_combos():
    rows = []
    for name, detail, kw in [('Base', 'Base', {})] + COMBOS:
        row = {'Combination': name, 'Settings': detail}
        for b, tag in (('combined', 'Combined'), ('adult_use', 'Adult-use only')):
            r = M.scenario(basis=b, **kw)
            row[f'{tag}: hold ends'] = r['hold_end']
            row[f'{tag}: first month 25% below $14.59'] = first_below(r)
            for p in COMBO_CHECKS:
                v = r['price'][p][0]
                row[f'{tag}: {p} ($/g)'] = round(v, 2) if v is not None else None
        rows.append(row)
    return rows

def run():
    rows = []
    for group, label, kw in TESTS:
        row = {'Assumption': group, 'Test': label}
        for b, tag in (('combined', 'Combined'), ('adult_use', 'Adult-use only')):
            r = M.scenario(basis=b, **kw)
            row[f'{tag}: hold ends (reaches the anchoring point)'] = r['hold_end']
            for p in CHECKS:
                v = r['price'][p][0]
                row[f'{tag}: {p} ($/g)'] = round(v, 2) if v is not None else None
        rows.append(row)
    return rows

def write(rows, name):
    with open(os.path.join(M.SM.OUT, name), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

if __name__ == '__main__':
    write(run_combos(), 'matched_path_adverse.csv')
    for r in run_combos(): print(r['Combination'][:40].ljust(40), [r[k] for k in list(r)[2:]])
    rows = run()
    with open(os.path.join(M.SM.OUT, 'matched_path_sensitivity.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    for r in rows: print(r['Assumption'][:22].ljust(22), r['Test'][:28].ljust(28), [r[k] for k in list(r)[2:]])
