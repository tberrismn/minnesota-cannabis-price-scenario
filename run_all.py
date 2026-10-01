"""Rebuild every output in this package, in order. Run from anywhere:  python3 code/run_all.py
Requires Python 3.9+, numpy and matplotlib. Takes under a minute. No step uses randomness, so reruns give identical CSVs."""
import os, runpy, sys
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'src'))
for step in ('harmonize.py', 'chart_same_age.py', 'chart_supply_scenarios.py', 'michigan_harvest_fit.py', 'chart_matched_path.py'):
    print('==', step)
    runpy.run_path(os.path.join(HERE, step), run_name='__main__')
print('Done. CSVs are in the package folder; charts are in charts/.')
