# Matched-market scenario: assumption ledger

Chart: `charts/10_matched_path.png`. Tracking sheet: `chart_matched_path.csv`. Sensitivity tables: `matched_path_sensitivity.csv` (one at a time), `matched_path_adverse.csv` (adverse combinations). Michigan checks: `michigan_harvest_fit.csv`.
Code: `code/matched_model.py` (the rule), `code/chart_matched_path.py`, `code/matched_sensitivity.py`, `code/michigan_harvest_fit.py`, `code/supply_model.py`.
Prepared 2026-09-30. Prices are pre-tax, per gram of adult-use flower, in August 2026 dollars (BLS CPI-U Midwest).

## What this is

An illustrative matched-market scenario, not a forecast and not a causal estimate. It asks one question: if Minnesota's legal flower market moves through the same price/throughput relationship Michigan's did, what path would Minnesota's adult-use flower price take?

The throughput measure is legal flower sold per adult. That is a market outcome, shaped by production, demand, price, legal-market capture, store access, tourism, hemp and the illicit market together. Lower Michigan prices also drew more buying into its legal market, so part of Michigan's curve is price moving quantity, not quantity moving price. The scenario borrows the relationship; it does not claim to have measured how supply alone sets price.

## The price statistics

This is part of the method, not a footnote.

| Item | What it is | Consequence |
|---|---|---|
| Minnesota's starting level | OCM's 12-month adult-use flower median through July 2026: $14.29, or $14.59 in August 2026 dollars | It is a trailing median, not a July shelf price. Minnesota publishes no monthly price series |
| What the two published medians say about recent prices | OCM's July 2026 window contains every adult-use sale in its December 2025 window ($13.54). If both medians are defined the same way, at most half of January-July 2026 sales were below $14.29 | Recent sales were not running below the trailing figure. Caveat: OCM's glossary now classes prerolls outside flower; whether the December figure included them is not stated |
| Michigan's price | CRA ounce-weighted average: flower dollars / flower weight, adult-use only | Only its percentage changes are used, applied to Minnesota's own level. Michigan's lower price level never carries over |
| Do percentage changes carry across the two statistics? | Over December 2019-September 2020, the only months CRA printed both, Michigan's adult-use median fell 22.3% and its weighted average fell 22.2%. Monthly changes correlate at 0.62 | Evidence that the two statistics move together over a 22% decline. It does not cover the steeper 2021-22 fall |
| What OCM will publish | A trailing 12-month median | The scenario gives a monthly price level. The tracking sheet gives two trailing proxies built from it: a volume-weighted average, and a volume-weighted median of monthly prices (every sale in a month at that month's price). Neither is OCM's median; together they give two reference estimates for how the trailing statistic may respond |

## The rule

1. **Throughput.** On both sides: legal flower sold per adult 21+ per month, averaged over the trailing 12 months (Michigan's first year: months since launch). Base measure: adult-use plus medical, the same scope as OCM's 12-month flower card. A second run uses adult-use flower only on both sides.
2. **Anchoring point.** Michigan at month 10 (October 2020): 0.44 g per adult per month, about 800,000 oz on OCM's 12-month card. Minnesota's latest data are at the same market age. Until Minnesota's throughput reaches that level, the scenario price stays at $14.59. There is no claimed universal threshold; 0.44 g is where the comparison starts, chosen by market age, and the sensitivity table moves it.
3. **Matching.** After that, each month the scenario price = $14.59 × (Michigan's price in the first month from October 2020 on when its throughput reached Minnesota's) ÷ (Michigan's price in October 2020, $18.18).
4. **Speed limit.** The scenario price may not fall more than 9.9% in a month, the pace of the steepest five-month fall in any comparison state's published real prices. Any decline beyond that carries into later months. The limit is a modeling choice drawn from observed data, not a law; the sensitivity table replaces it with none, 5% and 15%.

## Every assumption and what it rests on

| Assumption | Value | What it rests on | How we will know if it is wrong |
|---|---|---|---|
| Starting level | $14.59 (OCM's $14.29 12-month median) | OCM Cannabis Market Monitor; BLS CPI-U Midwest. See the price statistics above | Fixed. Replaced by each new OCM median |
| Throughput measure | Adult-use + medical (base); adult-use only (second run) | The combined measure matches OCM's card and is the more conservative of the two: the adult-use-only run leaves the hold three months earlier, runs about 19% lower through January 2028, and converges by 2029 | OCM's card reports both components, so both runs can be tracked |
| Minnesota medical sales (adult-use-only run) | Held at 15,405 oz a month, the observed 12-month level | OCM medical sales ran $6.3 million to $10.0 million a month from January 2024 to July 2026 with no break at the adult-use launch; medical plant starts ran 9,000 to 13,000 a month through 2026 | Medical ounces on OCM's card |
| Anchoring point | Michigan month 10 (0.44 g combined, 0.18 g adult-use only) | Same market age as Minnesota's latest data. Michigan's own price was flat from month 6 to month 10 ($18.40 to $18.18) while its throughput rose from 0.33 to 0.44 g, so any anchor on that plateau gives the same answer (tested at months 6 and 8). Minnesota's own two medians held flat (+4%) at 0.20 g. Massachusetts stayed between $18.48 and $19.38 while its throughput rose from 0.02 to 0.67 g in its first two years. Michigan's earlier fall, $23.77 to $18.40 from month 0 to month 6, came while its stores went from 26 to 123 | OCM's median falls before the card passes about 800,000 oz |
| Michigan as the comparison | Michigan's post-month-10 path | Minnesota's growth comes from uncapped microbusinesses with storefronts. Minnesota has 5.4 retail sites per 100,000 adults at month 12; Michigan reached 5.8 at month 24 (OCM, CRA) | Store count stalls, or the median holds as the card passes 800,000 oz |
| Speed limit | 9.9% a month at most | Steepest five-month real price falls: Michigan 41% (from March 2022), Massachusetts 34%, Ohio 31%, Connecticut 22%, Illinois 15%. Michigan's window starts at March 2022, a month whose reported flower weight fell 25% from February before more than doubling in April, which lifted that month's average. Michigan's next-steepest window, December 2020 to May 2021, is 39% (9.5% a month), so the limit barely depends on that month. The limit applies in most months from March 2027 to April 2028 in the base run | Minnesota's median falls faster than 10% a month |
| Plant starts through July 2026 | 37,000 to 212,000 a month | OCM Market Monitor, Cultivation tab (observed) | Revised by OCM |
| Harvest lag | 4 months | Typical clone-to-harvest cycle; tested at 3 and 5 | Harvest counts in October and November 2026 |
| Share of started plants harvested | 63% | OCM: May-July 2026 harvests over January-March 2026 starts. Only three months of data, so tested at 40% and 80% | Each new harvest month |
| Harvest-to-sales relationship stays stable | 83 g of flower sold per harvested plant | Calibrated so the model's August 2025-July 2026 total equals OCM's 12-month card (357,129 oz). It absorbs yield, waste, flower sent to processing and unsold stock; it does not assume every gram grown is sold. Outside check: fitted the same way, Michigan sold about 94 g per harvested plant (2022-2026 sales) | OCM's 12-month card each month |
| Added flower clears on the sell-through schedule | Each harvest sells evenly over 12 months, starting 1 month after harvest | Fitted directly to Michigan's harvest and sales records, not inferred from inventory. In levels, a 12-month spread explains 78% of the variation in Michigan's monthly flower sales (June 2022-August 2026), but both series trend upward, so that overstates the fit. On stricter checks 12 months still wins: lowest out-of-sample error (12.6% of mean sales, against 13.0% for 11 months, 13.9% for 13, 20.4% for 18 and 25.4% for 6), lowest rolling one-step error (10.3%), and the best fit after removing the common trend. That detrended fit is modest (R² 0.24), so the spread is identified loosely, and the 6- and 18-month tests stay in the table. **Not yet in Minnesota's data.** If only three-quarters of the added flower sells, the hold ends April 2027 and January 2028 is $6.50; if half, June 2027 and $7.55 | OCM's 12-month card: about 440,000 oz by October 2026, 650,000 by January 2027 and 855,000 by March 2027 |
| Future plant starts per site | 2026 rate by calendar month (534 a site outside the growing season) | OCM 2026 plant starts divided by OCM licensed cultivation sites; tested at half the outdoor-season rate | Plant starts in 2027 |
| Licensing pace | 20 microbusiness, 2.4 mezzobusiness, 2.2 cultivator licenses a month until March 2029; 41% of microbusinesses grow | OCM license counts, December 2025 to September 2026; 112 of 276 microbusinesses hold a cultivation site; 18-month conversion window plus up to 12 months of extensions (SF 4401); tested at half and all approvals | OCM license counts monthly |
| Demand per adult comparable to Michigan's | Same flower sold per adult means the same price position | **Uncertain; Minnesota demand may be lower.** OCM's 2025 demand study found median spending of $40 a month against $75.50 in comparison states, but the study itself says there is no validated method for setting a supply-to-demand ratio and that the hemp market makes total demand unknowable for now. Lower spending could mean Minnesota saturates at less flower per adult (prices fall sooner), or it could reflect pre-launch availability, prices, illicit and hemp purchasing, or product mix | Minnesota's median moves well before or well after the card passes 800,000 oz |
| No floor | Michigan's actual prices | Michigan's own data | n/a |

## Validation checks

- **Plants in the ground.** The supply model implies about 469,000 live plants in mid-September 2026. OCM reported 486,720 plants in inventory across 102 license holders (release of September 15, 2026), 3.6% more. This checks the plant flow (starts, harvest share, lag). It does not check grams per plant, which is calibrated.
- **Grams per plant.** Minnesota's calibrated 83 g sits 11% below Michigan's fitted 94 g, in the same range.
- **Sell-through.** Michigan's harvest and sales records favor a 12-month spread on every check: in-sample fit, out-of-sample error, rolling one-step error and the fit after removing the common trend. The detrended fit is modest (R² 0.24), so this pins the spread down loosely. Full grid in `michigan_harvest_fit.csv`.

## Results

| Month | Flower sold per adult (g/month) | Michigan month matched | Scenario price | Adult-use-only measure | Trailing 12-month proxy (average / median) | OCM 12-month card (oz) |
|---|---|---|---|---|---|---|
| Jul 2026 | 0.197 | Hold | $14.59 | $14.59 | $14.59 / $14.59 | 357,129 |
| Oct 2026 | 0.243 | Hold | $14.59 | $14.59 | $14.59 / $14.59 | 439,816 |
| Jan 2027 | 0.361 | Hold | $14.59 | $11.84 | $14.59 / $14.59 | 652,652 |
| Mar 2027 | 0.473 | Dec 2020 (limit applies) | $13.14 | $9.61 | $14.32 / $14.59 | 854,819 |
| Jul 2027 | 0.772 | May 2021 (limit applies) | $8.66 | $7.03 | $12.10 / $11.84 | 1,396,207 |
| Oct 2027 | 1.066 | Oct 2021 | $6.97 | $5.85 | $10.24 / $9.61 | 1,928,064 |
| Jan 2028 | 1.455 | Feb 2022 | $5.35 | $4.34 | $8.11 / $7.69 | 2,632,262 |
| Jul 2028 | 2.247 | Sep 2022 | $3.51 | $3.27 | $5.03 / $4.34 | 4,065,231 |
| Jan 2029 | 2.919 | Dec 2022 | $2.91 | $2.55 | $3.48 / $3.27 | 5,281,331 |

Public labels round these: about $9 in July 2027, about $5 in January 2028, about $3 in January 2029.

## Sensitivity

Each row changes one assumption at a time. This is one-at-a-time sensitivity analysis, not a joint uncertainty range; the adverse combinations below test assumptions moving together. "Hold ends" is the month throughput reaches the anchoring point.

| Assumption | Test | Hold ends | Jul 2027 | Jan 2028 | Jan 2029 | Adult-use only: hold ends | Jul 2027 | Jan 2028 | Jan 2029 |
|---|---|---|---|---|---|---|---|---|---|
| Base | Base | Mar 2027 | $8.66 | $5.35 | $2.91 | Dec 2026 | $7.03 | $4.34 | $2.55 |
| Anchor | Michigan month 6 (Jun 2020) | Jan 2027 | $8.59 | $5.29 | $2.87 | Aug 2026 | $6.95 | $4.29 | $2.52 |
| Anchor | Michigan month 8 (Aug 2020) | Feb 2027 | $8.67 | $5.34 | $2.90 | Nov 2026 | $7.02 | $4.33 | $2.54 |
| Anchor | Michigan month 12 (Dec 2020) | Apr 2027 | $9.61 | $6.09 | $3.31 | Jan 2027 | $8.00 | $4.94 | $2.90 |
| Anchor | Michigan month 14 (Feb 2021) | May 2027 | $11.92 | $8.09 | $4.40 | Feb 2027 | $10.64 | $6.57 | $3.86 |
| Speed limit | None | Mar 2027 | $7.79 | $5.35 | $2.91 | Dec 2026 | $7.03 | $4.23 | $2.55 |
| Speed limit | 5% a month | Mar 2027 | $11.29 | $8.30 | $4.48 | Dec 2026 | $9.68 | $7.11 | $3.84 |
| Speed limit | 15% a month | Mar 2027 | $7.79 | $5.35 | $2.91 | Dec 2026 | $7.03 | $4.23 | $2.55 |
| Share of started plants harvested | 40% | May 2027 | $10.67 | $7.69 | $3.90 | Dec 2026 | $7.79 | $6.50 | $3.74 |
| Share of started plants harvested | 80% | Feb 2027 | $7.81 | $5.11 | $2.75 | Dec 2026 | $6.50 | $3.74 | $2.75 |
| Harvest lag | 3 months | Mar 2027 | $8.66 | $5.66 | $3.04 | Nov 2026 | $7.03 | $4.60 | $2.91 |
| Harvest lag | 5 months | Apr 2027 | $9.61 | $5.66 | $2.62 | Dec 2026 | $7.69 | $4.60 | $2.72 |
| Sale lag | 0 months | Feb 2027 | $8.17 | $6.29 | $2.91 | Nov 2026 | $7.03 | $5.11 | $2.55 |
| Sale lag | 2 months | Apr 2027 | $9.61 | $5.66 | $2.62 | Dec 2026 | $7.69 | $4.60 | $2.72 |
| Sell-through | 6 months | Feb 2027 | $7.81 | $5.10 | $2.91 | Nov 2026 | $6.50 | $3.91 | $2.62 |
| Sell-through | 18 months | Apr 2027 | $9.61 | $6.28 | $2.91 | Dec 2026 | $7.55 | $5.10 | $2.62 |
| Outdoor-season planting | Half the 2026 rate | Mar 2027 | $8.66 | $5.66 | $3.51 | Dec 2026 | $7.03 | $5.67 | $3.27 |
| Licensing | Half of approvals | Mar 2027 | $8.66 | $5.66 | $3.27 | Dec 2026 | $7.03 | $4.60 | $3.04 |
| Licensing | All approvals | Mar 2027 | $8.66 | $6.29 | $2.72 | Dec 2026 | $7.03 | $4.34 | $2.73 |
| Share of added flower that sells | 75% | Apr 2027 | $9.61 | $6.50 | $3.51 | Dec 2026 | $7.55 | $5.35 | $3.27 |
| Share of added flower that sells | 50% | Jun 2027 | $11.84 | $7.55 | $5.11 | Jan 2027 | $7.88 | $6.97 | $3.90 |

**What holds.** Across the tested scenarios (the base and 20 one-at-a-time tests, for both measures), the hold ends between August 2026 and June 2027, and January 2028 is between $3.74 and $8.30, 43% to 74% below $14.59. January 2029 is between $2.52 and $5.11. The chart's gray band shows this range.

**What moves it.** Four tests move January 2028 by more than $2: anchoring after Michigan's first drop began (month 14: $8.09), a 5% speed limit ($8.30), a 40% harvest share ($7.69) and half the added flower selling ($7.55). The anchor result follows from Michigan's data: its price was flat from month 6 to 10 and fell 34% from month 10 to month 14, so an anchor at month 14 assumes Minnesota skips that first drop.

**Why some single months look backwards.** More supply can show a higher price in one month (all approvals: $6.29 in January 2028 against $5.66 for half). Michigan's March 2022 reading ($7.84, between $6.67 in February and $5.45 in April) is the matched month in those runs. Michigan's monthly prices are used as published, so any single-month value can move by about $1; the rounded labels and the ranges carry the result.

## Adverse combinations

The one-at-a-time tests do not show what happens when several assumptions go wrong together. These combinations pair logically separate assumptions that each push toward a later or smaller decline. The last row stacks every adverse test at once as a stress case; it double-counts related effects on purpose. These runs are reported here, not in the chart's band.

| Combination | Settings | Hold ends | 25% below $14.59 by | Jul 2027 | Jan 2028 | Jan 2029 | Adult-use only: 25% below by | Jan 2028 |
|---|---|---|---|---|---|---|---|---|
| Base | Base | Mar 2027 | May 2027 | $8.66 | $5.35 | $2.91 | Feb 2027 | $4.34 |
| Later anchor + slow price adjustment | Michigan month 14 anchor, 5% speed limit | May 2027 | Nov 2027 | $12.57 | $9.48 | $5.12 | Jul 2027 | $8.17 |
| Fewer plants harvested + weaker sales | 40% harvested, 75% of added flower sells | Jun 2027 | Aug 2027 | $11.84 | $7.88 | $5.35 | Mar 2027 | $7.03 |
| Fewer plants harvested + slower planting | 40% harvested, half the outdoor-season rate | May 2027 | Jul 2027 | $10.67 | $7.55 | $5.35 | Mar 2027 | $6.97 |
| Fewer plants harvested + fewer licenses | 40% harvested, half of approvals | May 2027 | Jul 2027 | $10.67 | $7.55 | $4.37 | Mar 2027 | $6.50 |
| Slow price adjustment + weak sales | 5% speed limit, 50% of added flower sells | Jun 2027 | Nov 2027 | $13.17 | $9.68 | $5.68 | Jun 2027 | $7.49 |
| Slow supply chain | 5-month harvest lag, 2-month sale lag, 18-month sell-through | May 2027 | Jul 2027 | $10.67 | $6.97 | $2.91 | Apr 2027 | $5.66 |
| Weak production and sales | 40% harvested, half outdoor rate, half of approvals, 75% sells | Jun 2027 | Sep 2027 | $11.84 | $8.74 | $7.03 | Mar 2027 | $7.55 |
| Stress case: every adverse test at once | Month 14 anchor, 5% limit, 40% harvested, 50% sells, half outdoor rate, half of approvals, slow chain | May 2028 | Not by Dec 2029 | $14.59 | $14.59 | $11.94 | Mar 2029 | $13.23 |

**What survives.** In all seven combinations the scenario price is at least 25% below $14.59 by November 2027, and January 2028 is between $6.97 and $9.68, 34% to 52% below today. Only the stress case pushes meaningful compression past 2028: its hold lasts to May 2028, and on the combined measure the price is still $11.64 in December 2029, 20% below today.

## How we will know within six months

By the end of March 2027, OCM will have published data through about January 2027:

1. **Is the planting surge reaching harvest?** 71,000 to 133,000 plants harvested a month in October and November 2026, against 21,200 in July.
2. **Is the harvest turning into sales?** OCM's 12-month flower card at about 440,000 oz for October 2026 and 650,000 oz for January 2027, up from 357,129. A card well below that path moves the result toward the 75% and 50% rows.
3. **When should the price move?** Once the card passes about 800,000 oz (base: March 2027), or the adult-use portion passes about 320,000 oz (adult-use-only run: December 2026). The 12-month median should begin to turn down in the spring 2027 readings; the two trailing proxies are around $12 (real) by July 2027.
4. **What would break the scenario?** The median falling well before the card passes 800,000 oz (the hold is wrong; the adult-use-only run fits better), or the card passing 1.4 million oz by July 2027 with the median still near $14 (Michigan's relationship does not transfer).
