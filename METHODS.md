# Methods

How the three charts in the article were built: the data, the rules, the tests that try to break them, and the published figures that will show whether the scenario holds. Every assumption, the full sensitivity tables and the six-month checkpoints are in [ASSUMPTIONS.md](ASSUMPTIONS.md).

Prices are pre-tax, per gram of adult-use flower, in August 2026 dollars (BLS CPI-U Midwest) unless marked otherwise.

## The answer

![If Minnesota's price follows Michigan's as its legal flower sales grow](charts/10_matched_path.png)

**If Minnesota's added cultivation turns into legal flower sales, and its market moves through the same price/throughput relationship Michigan's did, serious price compression begins in the first half of 2027 and 2027-28 is the main adjustment.**

In the base scenario a gram of adult-use flower goes from $14.50 to about $8 by July 2027, about $5 by January 2028 and about $3 by January 2029. Across the tested scenarios (the base and 20 one-at-a-time tests, for both measures), the hold ends between August 2026 and April 2027 and January 2028 lands between $3.25 and $7.84, 46% to 78% below today. Seven deliberately adverse combinations of assumptions still put the price at least 25% below today by September 2027. Only a stress case that stacks every adverse assumption at once pushes meaningful compression past 2028.

**Updated October 1, 2026** with OCM data through August 2026. The first checkpoint passed: the previous version projected 378,821 oz for OCM's 12-month flower card through August, and OCM reported 380,610 (+0.5%). The same release showed far more planting than assumed (289,493 plants started in August), which brings the end of the hold forward from March to February 2027.

This is an illustrative scenario, not a forecast. Its value is in the checkpoints: within six months, OCM's dashboard will show whether the added flower is arriving, and the spring 2027 readings will show whether the price responds.

| Month | Scenario price | Adult-use-only measure | Range across tested scenarios | Trailing 12-month proxy (median / average) | Eighth at the register* |
|---|---|---|---|---|---|
| Aug 2026 (latest published) | $14.50 | $14.50 | $14.50 to $14.51 | $14.50 / $14.50 | $62 |
| Jan 2027 | $14.50 | $11.10 | $9.08 to $14.52 | $14.50 / $14.50 | $62 |
| Jul 2027 | $7.76 | $5.94 | $5.12 to $10.66 | $10.61 / $11.14 | $33 |
| Jan 2028 | $4.58 | $3.48 | $3.25 to $7.84 | $6.30 / $7.22 | $20 |
| Jan 2029 | $2.81 | $2.76 | $2.53 to $4.25 | $2.73 / $2.96 | $12 |

\*3.5 grams at the scenario price plus Minnesota's 15% cannabis tax and 6.875% state sales tax (× 1.21875). Minneapolis adds 2.15% local tax. The trailing proxies are built from the scenario to sit alongside OCM's published 12-month median; neither is OCM's median.

## Reading the chart

**Top panel.** Grams of legal flower sold per adult 21+ per month, adult-use plus medical, averaged over the past 12 months: the same scope as OCM's 12-month flower card. The black dot is Minnesota today (0.21 g). The dashed line is Minnesota projected from plant data. The blue line is Michigan at the same months since its launch. The dotted blue line is the anchoring point: Michigan at its month 10 (October 2020), 0.44 g.

**Bottom panel.** The black step line is the scenario price level. It starts from OCM's trailing 12-month median, holds until Minnesota's flower sold per adult reaches the anchoring point, then follows Michigan's price changes at matching flower sold per adult. The gray band is the lowest and highest scenario price each month across the base and 20 one-at-a-time sensitivity tests, including runs that count adult-use flower only. It shows how far single assumptions move the answer; it is not a joint uncertainty range. The dots are OCM's published medians (December 2025, July 2026 and August 2026).

## The price statistics

Minnesota and Michigan publish different price statistics, and neither is a monthly shelf price for Minnesota. This decides how the scenario is built and how it can be checked.

| Item | What it is | What follows |
|---|---|---|
| Minnesota's starting level | OCM's 12-month adult-use flower median through August 2026: $14.23, or $14.50 in August 2026 dollars | A trailing median, not a shelf price. Minnesota publishes no monthly price series |
| What the three medians say about recent prices | $13.54 (Dec 2025), $14.29 (Jul 2026), $14.23 (Aug 2026). Each later window contains every adult-use sale in the earlier ones. If the definitions match, at most half of January to July 2026 sales were below $14.29, and at least half of August 2026 sales were at or below $14.23 | Prices ran at or slightly above the trailing figure through July; August's sales came in a little below it. Too small a move to call a turn. Caveat: OCM now classes prerolls outside flower, and whether the December figure included them is not stated |
| Michigan's price | CRA ounce-weighted average (flower dollars ÷ flower weight), adult-use only | Only its percentage changes are used, applied to Minnesota's own level. Michigan's lower price level never carries over |
| Do percentage changes carry across the two statistics? | From December 2019 to September 2020, the only months CRA printed both, Michigan's adult-use median fell 22.3% and its weighted average 22.2%. Monthly changes correlate at 0.62 | The two moved together over a 22% decline. That test does not reach the steeper 2021-22 fall |
| What OCM will publish | A trailing 12-month median | Two proxies built from the scenario: a volume-weighted average, and a volume-weighted median of monthly prices (each month's sales at that month's price). Neither is OCM's median; together they give two reference estimates for how the trailing statistic may respond |

## How the scenario is built

1. **Measure flower sold the same way in both states.** Legal flower sold per adult 21+ per month, averaged over the trailing 12 months. Minnesota's current figure comes straight from OCM's 12-month card: 380,610 oz ÷ 12 months ÷ 4,273,685 adults = 0.21 g. Michigan's comes from CRA monthly sales by weight and Census ACS population; in its first year, the average covers the months since launch. The base run counts adult-use plus medical flower on both sides. A second run counts adult-use flower only on both sides (Minnesota today: 197,008 oz, or 0.109 g), with Minnesota's medical sales held at their observed level.
2. **Project Minnesota's flower sales from plants in the ground.** OCM publishes plants started and harvested each month. Starts through August 2026 are observed (47,161 in April, 289,493 in August). Each started plant is harvested four months later at the observed rate of 74%. Each month's harvest sells evenly over the following 12 months, starting a month after harvest, the spread that best fits Michigan's own harvest and sales records. Grams sold per harvested plant (85 g) is set so the model reproduces OCM's actual 12-month flower total. Starts after August 2026 come from licensed cultivation sites (168 today) growing at the current licensing pace, each planting at Minnesota's 2026 rate for that calendar month.
3. **Anchor at Michigan's month 10.** Minnesota's data were at month 10 of adult-use sales when the scenario was set (July 2026), so the comparison starts at Michigan's month 10 (October 2020, 0.44 g per adult per month, about 800,000 oz on OCM's card). The anchor stays fixed as new months arrive, so the scenario can be checked rather than re-fit. Until Minnesota reaches that level the scenario price stays at the latest median, $14.50. This is an anchoring point chosen by market age, not a claimed universal threshold. Michigan's own price was flat from month 6 to month 10 ($18.40 to $18.18) while its flower sold per adult rose from 0.33 to 0.44 g, so anchors anywhere on that plateau give the same answer.
4. **Match each later month to Michigan at the same flower sold per adult.** For each month after that, find the first month from October 2020 on when Michigan sold as much flower per adult as Minnesota is projected to sell. The scenario price changes by the same percentage Michigan's price changed between its month 10 and that month. Michigan's monthly prices are used as published, with no smoothing and no floor. Michigan's record tops out at 6.8 g per adult; a run that passes it stops there rather than extrapolating.
5. **Apply a speed limit, and test it.** The steepest five-month real price fall in any comparison state is 41% (Michigan, from March 2022), or 9.9% a month. The scenario may not fall faster; any extra decline carries into later months. This is a modeling choice drawn from observed data, not a law, so the sensitivity tests run it at none, 5% and 15%.
6. **Build trailing proxies for tracking.** For comparison with OCM's 12-month median, the scenario is rolled into two trailing 12-month proxies, weighted by adult-use volume and starting at the September 2025 launch as OCM's window does.

### Worked example: July 2027

```
Minnesota flower sold per adult, projected .. 1.065 g a month (12-month average)
First Michigan month at or above 1.065 g ...... October 2021 (1.130 g)
Michigan price, October 2021 .................. $8.69
Michigan price, October 2020 (month 10) ....... $18.18
Change from Michigan's month 10 ............... 8.69 ÷ 18.18 = 0.478
Michigan-matched price ........................ $14.50 × 0.478 = $6.93
Speed limit: June 2027 price × 0.901 .......... $8.61 × 0.901 = $7.76
Scenario price ................................ $7.76 (the higher of the two)
```

The limit also applies in January 2028: 2.051 g matches Michigan in August 2022 (2.162 g, $4.66), a matched price of $14.50 × 4.66 ÷ 18.18 = $3.71, but the limit holds it at $5.08 × 0.901 = $4.58. Because the limit binds through most of 2027, the pace of the decline rests on it; with no limit, January 2028 is $3.71.

### Month by month

| Minnesota month | MN flower sold per adult (g) | OCM 12-month card (oz) | Michigan month | MI flower sold per adult (g) | MI price | Matched price | Scenario price | Adult-use-only measure | Trailing proxy (median / average) |
|---|---|---|---|---|---|---|---|---|---|
| Aug 2026 | 0.210 | 380,610 | Hold | | | $14.50 | $14.50 | $14.50 | $14.50 / $14.50 |
| Oct 2026 | 0.251 | 453,400 | Hold | | | $14.50 | $14.50 | $14.50 | $14.50 / $14.50 |
| Jan 2027 | 0.417 | 753,908 | Hold | | | $14.50 | $14.50 | $11.10 | $14.50 / $14.50 |
| Mar 2027 | 0.599 | 1,082,692 | Mar 2021 | 0.644 | $11.38 | $9.08 | $11.77 | $9.01 | $14.50 / $13.66 |
| Apr 2027 | 0.701 | 1,267,886 | Apr 2021 | 0.722 | $10.90 | $8.69 | $10.61 | $8.12 | $13.07 / $13.07 |
| Jul 2027 | 1.065 | 1,926,481 | Oct 2021 | 1.130 | $8.69 | $6.93 | $7.76 | $5.94 | $10.61 / $11.14 |
| Oct 2027 | 1.501 | 2,714,988 | Mar 2022 | 1.510 | $7.84 | $6.25 | $6.25 | $4.35 | $8.61 / $9.31 |
| Jan 2028 | 2.051 | 3,711,094 | Aug 2022 | 2.162 | $4.66 | $3.71 | $4.58 | $3.48 | $6.30 / $7.22 |
| Jul 2028 | 3.147 | 5,693,546 | Jan 2023 | 3.170 | $3.18 | $2.53 | $2.53 | $2.71 | $3.71 / $4.20 |
| Jan 2029 | 4.077 | 7,375,797 | May 2023 | 4.083 | $3.52 | $2.81 | $2.81 | $2.76 | $2.73 / $2.96 |
| Dec 2029 | 5.415 | 9,794,864 | Nov 2024 | 5.417 | $2.70 | $2.16 | $2.16 | $2.16 | $2.76 / $2.66 |

Flower sold in grams per adult 21+ per month, 12-month average, adult-use plus medical. Michigan prices are CRA adult-use ounce-weighted averages per gram in August 2026 dollars; only their percentage change from October 2020 ($18.18) is used. Where the scenario price sits above the matched price, the speed limit applies. Every month is in [chart_matched_path.csv](chart_matched_path.csv).

### Inputs

| Input | Value | Source |
|---|---|---|
| Minnesota adult-use flower median, 12 months to Dec 2025 / Jul 2026 / Aug 2026 | $13.54 / $14.29 / $14.23 ($14.02 / $14.59 / $14.50 real) | OCM news release (Jan 15, 2026); OCM Cannabis Market Monitor |
| Minnesota flower sold, 12 months to Aug 2026 | 380,610 oz (197,008 adult-use, 183,602 medical) | OCM Cannabis Market Monitor (extracted Oct 1, 2026) |
| Minnesota medical sales, monthly | $6.3M to $10.0M, Jan 2024 to Jul 2026 | OCM Cannabis Market Monitor |
| Minnesota adults 21+ | 4,273,685 | Census ACS 1-year 2024, table B01001 |
| Plants started, Jan to Aug 2026 (adult-use + medical) | 37k, 30k, 31k, 47k, 71k, 112k, 223k, 289k | OCM Cannabis Market Monitor, Cultivation tab |
| Plants harvested, Aug 2026 | 45,835 | OCM Cannabis Market Monitor, Cultivation tab |
| Plants in inventory, mid-Sep 2026 | 486,720 across 102 license holders | OCM news release, Sep 15, 2026 |
| Licensed cultivation sites | 168 (Sep 25, 2026) | OCM Cannabis Market Monitor |
| Preliminary approvals | 975 micro, 48 mezzo, 19 cultivator | OCM Summary Application Data, Sep 21, 2026 |
| Licenses issued per month, Dec 2025 to Sep 2026 | 20 micro, 2.4 mezzo, 2.2 cultivator | OCM 2025 Market Analysis Report; Summary Application Data |
| Michigan flower sold, plants harvested, adult-use average price, monthly | Dec 2019 to Aug 2026 (harvests from Oct 2020) | Michigan CRA monthly statistical reports |
| Michigan adult-use median price, monthly | Dec 2019 to Sep 2020 only | Michigan CRA monthly statistical reports |
| Inflation adjustment | CPI-U Midwest, base Aug 2026 | BLS series CUUR0200SA0, via FRED |

## Validation checks

- **First checkpoint: 378,821 oz projected vs 380,610 reported.** The September 30 version projected OCM's 12-month flower card through August 2026 from data through July. OCM's October 1 release came in +0.5% from it. Eleven of the twelve months were already in the July card (357,129 oz), so this mainly tests one month: a projected rise of 21,692 oz against an actual 23,481.
- **Plants in the ground: 499,000 to 675,000 vs 486,720.** Live plants the model implies for mid-September 2026: 675,000 if every plant started in the four months before survives until harvest, 499,000 if the 26% never harvested are lost early. OCM reported 486,720 in inventory across 102 license holders, at the low end, which fits most losses happening early. This checks the plant flow, not grams per plant.
- **Grams per harvested plant: 85 g vs 94 g.** Minnesota's calibrated figure against Michigan's, fitted the same way to its 2022-2026 harvest and sales records: 9% lower, same range.
- **Sell-through: 12 months, best on all four checks.** The harvest spread that best reproduces Michigan's monthly flower sales in sample, out of sample, month by month, and after removing the common trend. Short spreads fail: Michigan's sales do not follow its fall harvest peaks.

| Each harvest sells over | R² in levels | Out-of-sample error | Rolling one-step error | R² after removing trend | Fitted grams sold per harvested plant |
|---|---|---|---|---|---|
| 5 months | -0.69 | 29.3% | 30.5% | 0.00 | 85 g |
| 6 months | -0.27 | 25.4% | 26.4% | 0.01 | 86 g |
| 8 months | 0.29 | 18.7% | 19.6% | 0.03 | 89 g |
| 11 months | 0.74 | 13.0% | 11.6% | 0.15 | 92 g |
| **12 months** | 0.78 | 12.6% | 10.3% | 0.24 | 94 g |
| 13 months | 0.75 | 13.9% | 10.8% | 0.21 | 94 g |
| 18 months | 0.57 | 20.4% | 15.2% | 0.10 | 98 g |

Michigan sales June 2022 to August 2026 (51 months), sales starting one month after harvest. Harvests and sales both trend upward, so the R² in levels overstates the fit; the next three columns are stricter. Out-of-sample error: grams per plant fitted on June 2022 to June 2024, error on July 2024 to August 2026. Rolling one-step error: each month predicted from a fit on all earlier months. Errors are RMSE as a share of mean sales. 12 months wins on every column, but the detrended fit is modest (R² 0.24): harvest timing explains about a quarter of the variation around the trend, so the spread is pinned down loosely, and the 6- and 18-month tests stay in the sensitivity tables. A negative R² means the fit is worse than a flat average. Full grid in [michigan_harvest_fit.csv](michigan_harvest_fit.csv).

## Sensitivity, adverse combinations and checkpoints

The full tables are in [ASSUMPTIONS.md](ASSUMPTIONS.md), [matched_path_sensitivity.csv](matched_path_sensitivity.csv) and [matched_path_adverse.csv](matched_path_adverse.csv). In short:

- **One at a time.** Across the base and 20 tests, for both measures, the hold ends between August 2026 and April 2027 and January 2028 is between $3.25 and $7.84. Four tests move January 2028 by nearly $2 or more: a 5% speed limit ($7.84), anchoring at Michigan's month 14 ($6.92), a 40% harvest share ($6.46) and half the added flower selling ($6.46).
- **Adverse combinations.** In all seven, the price is at least 25% below $14.50 by September 2027, and January 2028 is between $4.61 and $8.68. A stress case with every adverse test at once holds the price until January 2028 and leaves it at $9.77 in December 2029.
- **Checkpoints.** OCM's 12-month flower total should reach about 453,000 oz in the October 2026 data and 754,000 oz in the January 2027 data. Monthly harvests should run about 52,000 plants in September, 83,000 in October, 165,000 in November and 214,000 in December 2026. Once the total passes about 800,000 oz (base: February 2027), OCM's 12-month median should begin to turn down; the two trailing proxies are around $11 by July 2027. A median still near $14 with the total near 1.9 million oz in July 2027 would mean Michigan's relationship does not transfer.

## The other two charts

### If Minnesota follows the states that came before it

![If Minnesota follows the states that came before it](charts/7_same_age_paths.png)

Data: [chart_same_age_paths.csv](chart_same_age_paths.csv). Code: [code/chart_same_age.py](code/chart_same_age.py).

- **Prices.** Each state's monthly retail flower price as published, in dollars per gram, adjusted to August 2026 dollars with BLS CPI-U Midwest. Michigan: CRA ounce-weighted average. Massachusetts: CCC average price per gram. Illinois: CROO flower average, through May 2025. No smoothing and no floor. Massachusetts April 2020 (COVID retail closure) is omitted.
- **The rule.** Each line is Minnesota's July 2026 level, its month 10 ($14.59), times the state's price in a given month divided by its price in its own month 10. States are matched by months since adult-use sales began, not by sales volume. Faded lines show each state's first ten months on the same scale. Minnesota's later readings (August 2026: $14.50) are plotted as published.
- **Result.** Three years on (July 2029): $3.02 following Michigan, $8.06 following Massachusetts, $8.26 following Illinois. The shaded area spans the three lines; it is not a forecast range.
- **Why it differs from the main chart.** This chart matches by age, so its Michigan line falls at once. The main chart matches by flower sold per adult, so Minnesota waits until it sells as much as Michigan did at month 10.

### How much cannabis Minnesota could grow as licenses convert

![How much cannabis Minnesota could grow as licenses convert](charts/9_supply_scenarios_yearly.png)

Data: [chart_supply_yearly.csv](chart_supply_yearly.csv) (monthly: [chart_supply_scenarios.csv](chart_supply_scenarios.csv)). Code: [code/chart_supply_scenarios.py](code/chart_supply_scenarios.py) and [code/supply_model.py](code/supply_model.py).

- **Sites.** 168 licensed cultivation sites on September 25, 2026 (OCM Cannabis Market Monitor). New sites come from preliminary approvals: 975 microbusinesses, 48 mezzobusinesses and 19 cultivators (OCM Summary Application Data, September 21, 2026). 41% of microbusinesses hold a cultivation site (112 of 276, from the OCM licensed-business workbook of September 14, 2026).
- **Four scenarios.** Half, three-quarters or all approvals convert evenly from October 2026 to March 2029: the 18-month window plus up to 12 months of extensions under SF 4401. Current pace: 20 microbusiness, 2.4 mezzobusiness and 2.2 cultivator licenses a month, the December 2025 to September 2026 rate, until March 2029.
- **Plantings.** Observed through August 2026. After that, each site plants at Minnesota's 2026 rate for that calendar month, plus medical plantings at their 2026 average. September to December have no 2026 data yet and use the January to April average (532 plants a site). August's observed rate was 1,742 a site.
- **Harvests.** 74% of started plants are harvested four months later (OCM: May to August 2026 harvests over January to April starts). 2026 is mostly settled by plants already growing: about 690,000 harvested. 2027: 1.8 to 2.2 million. 2029: 3.1 to 4.7 million.

## What this does not show

- Flower sold is a market outcome. Lower Michigan prices also pulled buying into its legal market, so the relationship is borrowed, not a measured effect of supply on price.
- Minnesota's starting level rests on trailing medians. OCM does not publish monthly prices.
- Michigan's average and median moved together over a 22% decline in 2019-20. Nothing tests that relationship through the steeper 2021-22 fall.
- Hemp-derived THC products (1,895 retail licenses) and Tribal dispensaries compete for the same buyers; neither has a price or volume series to include.
- The gray band and the adverse combinations are sensitivity analysis, not probabilities. No run is weighted as more likely than another.
- Michigan is one market. Massachusetts and Illinois took slower paths, and the "same age" chart keeps them in view.

## Sources

- Minnesota Office of Cannabis Management, [Cannabis Market Monitor](https://mn.gov/ocm/data-reports/dashboards/cannabis-market-monitor.jsp) (extracted October 1, 2026; Metrc data through August 2026)
- OCM news release, [January 15, 2026](https://content.govdelivery.com/accounts/MNOCM/bulletins/4048e26) (December 2025 median)
- OCM news release, [September 15, 2026](https://content.govdelivery.com/accounts/MNOCM/bulletins/42aab6d) (plant inventory)
- OCM [Summary Application Data](https://mn.gov/ocm/data-reports/application-data/index.jsp) (September 21, 2026)
- OCM [licensed-business workbook](https://mn.gov/ocm/assets/MN_OCM_licensed_businesses_091426_tcm1202-714418.xlsx) (September 14, 2026)
- OCM [summary of 2026 policy changes](https://content.govdelivery.com/attachments/MNOCM/2026/05/26/file_attachments/3663662/Cannabis_Policy_Changes_2026.pdf) (SF 4401)
- OCM [2025 Market Analysis Report](https://www.lrl.mn.gov/docs/2026/mandated/260064.pdf)
- OCM [2025 Cannabis Market Size and Growth Study](https://mn.gov/ocm/assets/OCM_2025_Final_Demand_Report_0115_tcm1202-665241.pdf)
- Michigan Cannabis Regulatory Agency, [monthly statistical reports](https://www.michigan.gov/cra/resources/cannabis-regulatory-agency-licensing-reports/cannabis-regulatory-agency-statistical-report)
- Massachusetts Cannabis Control Commission, [price per gram](https://masscannabiscontrol.com/resource/a_sales_au_price_per_gram.csv)
- Illinois Cannabis Regulation Oversight Officer, [sales figures](https://cannabis.illinois.gov/research-and-data/sales-figures.html)
- U.S. Census Bureau, [ACS 1-year B01001](https://api.census.gov/data/2024/acs/acs1)
- BLS CPI-U Midwest (CUUR0200SA0), [via FRED](https://fred.stlouisfed.org/series/CUUR0200SA0)
