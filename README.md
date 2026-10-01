# When will cannabis get cheaper in Minnesota? Data and code

Data and code behind Tanner Berris's Substack article on Minnesota cannabis flower prices.

The article asks one question: if Minnesota's legal flower market follows the path Michigan's did, when do prices fall, and how far? This package rebuilds all three charts in the article from public data. Run it again when the Minnesota Office of Cannabis Management (OCM) publishes new numbers to check the scenario against what actually happened.

It is an illustrative scenario, not a forecast. The methods are in [METHODS.md](METHODS.md). Every assumption, and what would show it wrong, is in [ASSUMPTIONS.md](ASSUMPTIONS.md).

## The three charts

| Chart | File | Data | Built by |
|---|---|---|---|
| If Minnesota follows the states that came before it | `charts/7_same_age_paths.png` | `chart_same_age_paths.csv` | `code/chart_same_age.py` |
| How much cannabis Minnesota could grow as licenses convert | `charts/9_supply_scenarios_yearly.png` | `chart_supply_yearly.csv` (monthly: `chart_supply_scenarios.csv`) | `code/chart_supply_scenarios.py` |
| If Minnesota's price follows Michigan's as its legal flower sales grow | `charts/10_matched_path.png` | `chart_matched_path.csv` | `code/chart_matched_path.py` |

The scripts also draw an eighth-price version of the first chart (`charts/8_same_age_eighth.png`) and a monthly version of the supply chart (`charts/9_supply_scenarios.png`).

## Other files

| File | What it is |
|---|---|
| `METHODS.md` | How each chart was built, the price statistics, validation checks and limits |
| `ASSUMPTIONS.md` | Every assumption in the price scenario, what it rests on, and how we will know if it is wrong. Includes the results, sensitivity tests and six-month checkpoints |
| `matched_path_sensitivity.csv` | The scenario with each assumption changed one at a time (base plus 20 tests), counting adult-use and medical flower and adult-use flower only |
| `matched_path_adverse.csv` | Combinations of unfavorable assumptions, plus a stress case with all of them at once |
| `michigan_harvest_fit.csv` | Checks the harvest-to-sales timing and grams sold per harvested plant against Michigan's records |
| `harmonized_prices.csv` | Every state's monthly retail flower price, nominal and in August 2026 dollars |
| `chart_matched_path.csv` | Also the tracking sheet: projected OCM 12-month flower volume and price by month, to compare with each new OCM release |

## How to rerun

You need Python 3.9 or newer, numpy and matplotlib (built with Python 3.11, numpy 2.4 and matplotlib 3.10).

```
pip install numpy matplotlib
python3 code/run_all.py
```

`run_all.py` runs five steps in order: `harmonize.py`, `chart_same_age.py`, `chart_supply_scenarios.py`, `michigan_harvest_fit.py` and `chart_matched_path.py`. The model behind the price scenario is in `code/matched_model.py` and the plant and licensing model in `code/supply_model.py`. No step uses randomness, so reruns reproduce the CSVs exactly.

## Data

All inputs are in `code/data/`. Every row in the price and supply files carries its source name, URL, access date and notes. Values are as published, transcribed from a published dashboard or chart, or computed from published figures, and the notes say which.

| File | Source |
|---|---|
| `mn_prices.csv`, `mn_supply.csv` | Minnesota Office of Cannabis Management: [Cannabis Market Monitor](https://mn.gov/ocm/data-reports/dashboards/cannabis-market-monitor.jsp), [Summary Application Data](https://mn.gov/ocm/data-reports/application-data/index.jsp), [licensed-business workbook](https://mn.gov/ocm/assets/MN_OCM_licensed_businesses_091426_tcm1202-714418.xlsx), news releases of [Jan. 15, 2026](https://content.govdelivery.com/accounts/MNOCM/bulletins/4048e26) and [Sept. 15, 2026](https://content.govdelivery.com/accounts/MNOCM/bulletins/42aab6d), [2025 Market Analysis Report](https://www.lrl.mn.gov/docs/2026/mandated/260064.pdf) |
| `prices_MI.csv`, `supply_MI.csv` | Michigan Cannabis Regulatory Agency, [monthly statistical reports](https://www.michigan.gov/cra/resources/cannabis-regulatory-agency-licensing-reports/cannabis-regulatory-agency-statistical-report) |
| `prices_MA.csv`, `supply_MA.csv` | Massachusetts Cannabis Control Commission, [open data](https://masscannabiscontrol.com/resource/a_sales_au_price_per_gram.csv) |
| `prices_IL.csv` | Illinois Cannabis Regulation Oversight Officer, [sales figures](https://cannabis.illinois.gov/research-and-data/sales-figures.html) |
| `prices_CT.csv` | Connecticut Department of Consumer Protection, [cannabis sales data](https://data.ct.gov/api/views/ybjg-7wfn/rows.csv?accessType=DOWNLOAD) |
| `prices_OH.csv`, `supply_OH.csv` | Ohio Division of Cannabis Control, [product data](https://dam.assets.ohio.gov/image/upload/com.ohio.gov/DCC/DCC_Product_Data_-_Non-Medical.pdf) |
| `pop21.csv` | U.S. Census Bureau, American Community Survey 1-year, [table B01001](https://api.census.gov/data/2024/acs/acs1) (adults 21 and older) |
| `cpi_midwest_CUUR0200SA0.csv` | Bureau of Labor Statistics CPI-U Midwest, all items, [via FRED](https://fred.stlouisfed.org/series/CUUR0200SA0), accessed Sept. 25, 2026 |

Things to know about the data:

- **OCM's dashboard can't be exported.** Minnesota values from the Cannabis Market Monitor were transcribed from the dashboard. Rows note where values were read off a chart and how precise they are.
- **Minnesota's price is a 12-month median.** OCM publishes no monthly price. The scenario starts from the latest 12-month median.
- **Michigan's price is an average.** It is an ounce-weighted average (flower dollars divided by flower weight). The model borrows only its percentage changes, never its dollar level.
- **Michigan, January 2024 to February 2026.** Prices for these months are computed from the same reports' flower sales and pounds. That identity matches the printed price to the cent in every month where both appear.
- **Two gaps are omitted, not filled.** Massachusetts April 2020 (COVID retail closure) is left out. Illinois prices after May 2025 are not used, because the state's switch to a new tracking system changed how sales are counted.
- **One CPI month is computed.** BLS published no October 2025 CPI. The code uses the average of September and November 2025 for that month, the only computed value in the package.

## Updating with new OCM data

When OCM publishes a new month, add the rows to `code/data/mn_supply.csv` and `code/data/mn_prices.csv` in the same format and rerun. To check the scenario, compare OCM's new 12-month flower volume and median with the matching row of `chart_matched_path.csv`. `ASSUMPTIONS.md` lists what each checkpoint should show.

## License

Be Kind, People Don't Own Information.
