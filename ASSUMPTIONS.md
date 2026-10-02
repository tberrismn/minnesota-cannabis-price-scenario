# Matched-market scenario: assumption ledger

Chart: `charts/10_matched_path.png`. Tracking sheet: `chart_matched_path.csv`. Sensitivity tables: `matched_path_sensitivity.csv` (one at a time), `matched_path_adverse.csv` (adverse combinations). Michigan checks: `michigan_harvest_fit.csv`.
Code: `code/matched_model.py` (the rule), `code/chart_matched_path.py`, `code/matched_sensitivity.py`, `code/michigan_harvest_fit.py`, `code/supply_model.py`.
Updated 2026-10-01 with OCM data through August 2026 (dashboard extracted Oct. 1, 2026). Prices are pre-tax, per gram of adult-use flower, in August 2026 dollars (BLS CPI-U Midwest).

## What this is

An illustrative matched-market scenario, not a forecast and not a causal estimate. It asks one question: if Minnesota's legal flower market moves through the same price/throughput relationship Michigan's did, what path would Minnesota's adult-use flower price take?

The throughput measure is legal flower sold per adult. That is a market outcome, shaped by production, demand, price, legal-market capture, store access, tourism, hemp and the illicit market together. Lower Michigan prices also drew more buying into its legal market, so part of Michigan's curve is price moving quantity, not quantity moving price. The scenario borrows the relationship; it does not claim to have measured how supply alone sets price.

## First checkpoint

The previous version (Sept. 30, built on data through July) projected 378,821 oz for OCM's 12-month flower card through August. OCM's Oct. 1 release reported 380,610 oz (197,008 adult-use, 183,602 medical), +0.5%. Eleven of the twelve months in that window were already in the July card (357,129 oz), so this mainly tests one month: the model projected a rise of 21,692 oz and the card rose 23,481 (+8%). The same release showed more growing than the model expected: 289,493 plants started in August against 95,217 assumed, and 45,835 plants harvested against 29,434 projected.

## The price statistics

This is part of the method, not a footnote.

| Item | What it is | Consequence |
|---|---|---|
| Minnesota's starting level | OCM's 12-month adult-use flower median through August 2026: $14.23, or $14.50 in August 2026 dollars | It is a trailing median, not a shelf price. Minnesota publishes no monthly price series |
| What the three published medians say about recent prices | $13.54 (Dec 2025), $14.29 (Jul 2026), $14.23 (Aug 2026). Each later window contains every adult-use sale in the earlier ones. If the definitions match, at most half of January-July 2026 sales were below $14.29, and at least half of August 2026 sales were at or below $14.23 | Prices ran at or slightly above the trailing figure through July; August's sales came in a little below it. Too small a move to call a turn. Caveat: OCM now classes prerolls outside flower, and whether the December figure included them is not stated |
| Michigan's price | CRA ounce-weighted average: flower dollars / flower weight, adult-use only | Only its percentage changes are used, applied to Minnesota's own level. Michigan's lower price level never carries over |
| Do percentage changes carry across the two statistics? | Over December 2019-September 2020, the only months CRA printed both, Michigan's adult-use median fell 22.3% and its weighted average fell 22.2%. Monthly changes correlate at 0.62 | Evidence that the two statistics move together over a 22% decline. It does not cover the steeper 2021-22 fall |
| What OCM will publish | A trailing 12-month median | The scenario gives a monthly price level. The tracking sheet gives two trailing proxies built from it: a volume-weighted average, and a volume-weighted median of monthly prices (every sale in a month at that month's price). Neither is OCM's median; together they give two reference estimates for how the trailing statistic may respond |

## The rule

1. **Throughput.** On both sides: legal flower sold per adult 21+ per month, averaged over the trailing 12 months (Michigan's first year: months since launch). Base measure: adult-use plus medical, the same scope as OCM's 12-month flower card. A second run uses adult-use flower only on both sides.
2. **Anchoring point.** Michigan at month 10 (October 2020): 0.44 g per adult per month, about 798,630 oz on OCM's 12-month card. Minnesota's data were at month 10 when the scenario was set (July 2026), and the anchor stays fixed as new months arrive so the scenario can be checked rather than re-fit. Anchoring at month 11 instead gives $4.85 in January 2028 against $4.58. Until Minnesota's throughput reaches the anchoring level, the scenario price stays at the latest median. There is no claimed universal threshold; 0.44 g is where the comparison starts, chosen by market age, and the sensitivity table moves it.
3. **Matching.** After that, each month the scenario price = $14.50 × (Michigan's price in the first month from October 2020 on when its throughput reached Minnesota's) ÷ (Michigan's price in October 2020, $18.18).
4. **Speed limit.** The scenario price may not fall more than 9.9% in a month, the pace of the steepest five-month fall in any comparison state's published real prices. Any decline beyond that carries into later months. The limit is a modeling choice drawn from observed data, not a law; the sensitivity table replaces it with none, 5% and 15%.
5. **End of Michigan's record.** Michigan's highest 12-month level is 6.8 g per adult (combined). A run that passes it stops there instead of extrapolating.

## Every assumption and what it rests on

| Assumption | Value | What it rests on | How we will know if it is wrong |
|---|---|---|---|
| Starting level | $14.50 (OCM's $14.23 12-month median) | OCM Cannabis Market Monitor; BLS CPI-U Midwest. See the price statistics above | Replaced by each new OCM median |
| Throughput measure | Adult-use + medical (base); adult-use only (second run) | The combined measure matches OCM's card and is the more conservative of the two: the adult-use-only run leaves the hold Nov 2026 instead of Feb 2027 and runs about 24% lower through January 2028 | OCM's card reports both components, so both runs can be tracked |
| Minnesota medical sales (adult-use-only run) | Held at 15,300 oz a month, the observed 12-month level | OCM medical sales ran $6.3 million to $10.0 million a month from January 2024 to July 2026 with no break at the adult-use launch; medical plant starts ran 8,700 to 14,200 a month from February to August 2026 | Medical ounces on OCM's card |
| Anchoring point | Michigan month 10 (0.44 g combined, 0.18 g adult-use only) | Same market age as Minnesota's data when the scenario was set. Michigan's own price was flat from month 6 to month 10 ($18.40 to $18.18) while its throughput rose from 0.33 to 0.44 g, so any anchor on that plateau gives nearly the same answer (tested at months 6 and 8). Minnesota's three medians have stayed between $14.02 and $14.59 (real). Massachusetts stayed between $18.48 and $19.38 in its first two years while its monthly flower sold per adult rose from 0.02 to 0.67 g (0.54 g on the 12-month average). Michigan's earlier fall, $23.77 to $18.40 from month 0 to month 6, came while its stores went from 26 to 123 | OCM's median falls well before the card passes about 800,000 oz |
| Michigan as the comparison | Michigan's post-month-10 path | Minnesota's growth comes from uncapped microbusinesses with storefronts. Minnesota has 223 adult-use retail sites, 5.2 per 100,000 adults, at month 12; Michigan had 5.8 at month 24 (OCM, CRA; both counts adult-use only) | Store count stalls, or the median holds as the card passes 800,000 oz |
| Speed limit | 9.9% a month at most | Steepest five-month real price falls: Michigan 41% (from March 2022), Massachusetts 34%, Ohio 31%, Connecticut 22%, Illinois 15%. Michigan's window starts at March 2022, a month whose reported flower weight fell 25% from February before more than doubling in April, which lifted that month's average. Michigan's next-steepest window, December 2020 to May 2021, is 39% (9.5% a month), so the limit barely depends on that month. The limit applies in most months from Feb 2027 to Jun 2028 in the base run, so the pace of the decline rests on it | Minnesota's median falls faster than 10% a month |
| Plant starts through August 2026 | 30,000 to 289,493 a month | OCM Market Monitor, Cultivation tab (observed; exact values from February 2026) | Revised by OCM |
| Harvest lag | 4 months | Typical clone-to-harvest cycle; tested at 3 and 5 | Harvest counts each month |
| Share of started plants harvested | 74% | OCM: May-August 2026 harvests over January-April 2026 starts. August's 45,835 harvests nearly equal April's 47,161 starts, which lifted this from 63%: either survival is higher than the first three months showed or some plants finish faster than four months (the 3-month lag test). Tested at 40% and 80% | September to December 2026 harvests |
| Harvest-to-sales relationship stays stable | 85 g of flower sold per harvested plant | Calibrated so the model's 12-month total through August 2026 equals OCM's card (380,610 oz). It absorbs yield, waste, flower sent to processing and unsold stock; it does not assume every gram grown is sold. Outside check: fitted the same way, Michigan sold about 94 g per harvested plant (2022-2026 sales) | OCM's 12-month card each month |
| Added flower clears on the sell-through schedule | Each harvest sells evenly over 12 months, starting 1 month after harvest | Fitted directly to Michigan's harvest and sales records, not inferred from inventory. In levels, a 12-month spread explains 78% of the variation in Michigan's monthly flower sales (June 2022-August 2026), but both series trend upward, so that overstates the fit. On stricter checks 12 months still wins: lowest out-of-sample error (12.6% of mean sales, against 13.0% for 11 months, 13.9% for 13, 20.4% for 18 and 25.4% for 6), lowest rolling one-step error (10.3%), and the best fit after removing the common trend. That detrended fit is modest (R² 0.24), so the spread is identified loosely, and the 6- and 18-month tests stay in the table. **Not yet in Minnesota's data.** If only three-quarters of the added flower sells, the hold ends Feb 2027 and January 2028 is $4.79; if half, Apr 2027 and $6.46 | OCM's 12-month card: about 453,000 oz by October 2026 and 754,000 by January 2027 |
| Future plant starts per site | 2026 rate by calendar month; months with no 2026 data yet (September-December) use the January-April average (532 a site) | OCM 2026 plant starts divided by OCM licensed cultivation sites. August 2026 is now observed at 1,742 a site, against the 532 assumed before it was published. Tested at half the outdoor-season rate | Plant starts in 2027 |
| Licensing pace | 20 microbusiness, 2.4 mezzobusiness, 2.2 cultivator licenses a month until March 2029, from 168 sites (Sept. 25, 2026); 41% of microbusinesses grow | OCM license counts, December 2025 to September 2026; 112 of 276 microbusinesses hold a cultivation site; 18-month conversion window plus up to 12 months of extensions (SF 4401); tested at half and all approvals | OCM license counts monthly |
| Demand per adult comparable to Michigan's | Same flower sold per adult means the same price position | **Uncertain; Minnesota demand may be lower.** OCM's 2025 demand study found median spending of $40 a month against $75.50 in comparison states, but the study itself says there is no validated method for setting a supply-to-demand ratio and that the hemp market makes total demand unknowable for now. Lower spending could mean Minnesota saturates at less flower per adult (prices fall sooner), or it could reflect pre-launch availability, prices, illicit and hemp purchasing, or product mix | Minnesota's median moves well before or well after the card passes 800,000 oz |
| No floor | Michigan's actual prices | Michigan's own data | n/a |

## Validation checks

- **First checkpoint.** Projected 378,821 oz for the 12 months through August 2026; OCM reported 380,610 (+0.5%). A one-month test: the projected rise was 21,692 oz, the actual 23,481.
- **Plants in the ground.** Counting every plant started in the four months before mid-September 2026 as alive gives about 675,000; if the 26% never harvested are lost early, about 499,000. OCM reported 486,720 plants in inventory across 102 license holders (release of September 15, 2026), at the low end, which fits most losses happening early. This checks the plant flow, not grams per plant, which is calibrated.
- **Grams per plant.** Minnesota's calibrated 85 g sits 9% below Michigan's fitted 94 g, in the same range.
- **Sell-through.** Michigan's harvest and sales records favor a 12-month spread on every check: in-sample fit, out-of-sample error, rolling one-step error and the fit after removing the common trend. The detrended fit is modest (R² 0.24), so this pins the spread down loosely. Full grid in `michigan_harvest_fit.csv`.

## Results

| Month | Flower sold per adult (g/month) | Michigan month matched | Scenario price | Adult-use-only measure | Trailing 12-month proxy (average / median) | OCM 12-month card (oz) |
|---|---|---|---|---|---|---|
| Aug 2026 | 0.210 | Hold | $14.50 | $14.50 | $14.50 / $14.50 | 380,610 |
| Oct 2026 | 0.251 | Hold | $14.50 | $14.50 | $14.50 / $14.50 | 453,400 |
| Jan 2027 | 0.417 | Hold | $14.50 | $11.10 | $14.50 / $14.50 | 753,908 |
| Mar 2027 | 0.599 | Mar 2021 (limit applies) | $11.77 | $9.01 | $13.66 / $14.50 | 1,082,692 |
| Jul 2027 | 1.065 | Oct 2021 (limit applies) | $7.76 | $5.94 | $11.14 / $10.61 | 1,926,481 |
| Oct 2027 | 1.501 | Mar 2022 | $6.25 | $4.35 | $9.31 / $8.61 | 2,714,988 |
| Jan 2028 | 2.051 | Aug 2022 (limit applies) | $4.58 | $3.48 | $7.22 / $6.30 | 3,711,094 |
| Jul 2028 | 3.147 | Jan 2023 | $2.53 | $2.71 | $4.20 / $3.71 | 5,693,546 |
| Jan 2029 | 4.077 | May 2023 | $2.81 | $2.76 | $2.96 / $2.73 | 7,375,797 |

Public labels round these: about $8 in July 2027, about $5 in January 2028, about $3 in January 2029.

## Sensitivity

Each row changes one assumption at a time. This is one-at-a-time sensitivity analysis, not a joint uncertainty range; the adverse combinations below test assumptions moving together. "Hold ends" is the month throughput reaches the anchoring point.

| Assumption | Test | Hold ends | Jul 2027 | Jan 2028 | Jan 2029 | Adult-use only: hold ends | Jul 2027 | Jan 2028 | Jan 2029 |
|---|---|---|---|---|---|---|---|---|---|
| Base | Base | Feb 2027 | $7.76 | $4.58 | $2.81 | Nov 2026 | $5.94 | $3.48 | $2.76 |
| Anchor | Michigan month 6 (Jun 2020) | Dec 2026 | $7.69 | $4.52 | $2.78 | Aug 2026 | $5.87 | $3.44 | $2.73 |
| Anchor | Michigan month 8 (Aug 2020) | Jan 2027 | $7.77 | $4.56 | $2.81 | Oct 2026 | $5.93 | $3.48 | $2.75 |
| Anchor | Michigan month 12 (Dec 2020) | Feb 2027 | $7.91 | $5.21 | $3.20 | Dec 2026 | $6.62 | $3.96 | $3.14 |
| Anchor | Michigan month 14 (Feb 2021) | Mar 2027 | $10.49 | $6.92 | $4.25 | Jan 2027 | $8.81 | $5.27 | $4.17 |
| Speed limit | None | Feb 2027 | $6.93 | $3.71 | $2.81 | Nov 2026 | $5.12 | $3.48 | $2.76 |
| Speed limit | 5% a month | Feb 2027 | $10.66 | $7.84 | $4.23 | Nov 2026 | $9.14 | $6.72 | $3.63 |
| Speed limit | 15% a month | Feb 2027 | $6.93 | $3.84 | $2.81 | Nov 2026 | $5.49 | $3.48 | $2.76 |
| Share of started plants harvested | 40% | Mar 2027 | $8.69 | $6.46 | $3.48 | Dec 2026 | $7.65 | $5.32 | $3.25 |
| Share of started plants harvested | 80% | Feb 2027 | $7.76 | $4.15 | $3.04 | Nov 2026 | $5.94 | $3.25 | $2.90 |
| Harvest lag | 3 months | Feb 2027 | $7.76 | $4.32 | $2.71 | Nov 2026 | $6.46 | $3.86 | $2.72 |
| Harvest lag | 5 months | Feb 2027 | $7.76 | $4.15 | $2.71 | Dec 2026 | $6.30 | $3.37 | $2.71 |
| Sale lag | 0 months | Jan 2027 | $6.99 | $3.74 | $2.73 | Nov 2026 | $5.68 | $3.71 | $2.81 |
| Sale lag | 2 months | Feb 2027 | $8.12 | $4.35 | $2.76 | Dec 2026 | $6.30 | $3.48 | $3.04 |
| Sell-through | 6 months | Jan 2027 | $6.99 | $4.12 | $2.73 | Nov 2026 | $5.68 | $3.25 | $2.73 |
| Sell-through | 18 months | Mar 2027 | $8.61 | $4.61 | $2.81 | Dec 2026 | $6.93 | $4.58 | $2.76 |
| Outdoor-season planting | Half the 2026 rate | Feb 2027 | $7.76 | $4.58 | $2.71 | Nov 2026 | $5.94 | $3.71 | $2.72 |
| Licensing | Half of approvals | Feb 2027 | $7.76 | $4.15 | $2.72 | Nov 2026 | $5.94 | $3.48 | $2.72 |
| Licensing | All approvals | Feb 2027 | $7.76 | $4.15 | $3.08 | Nov 2026 | $5.94 | $3.35 | $3.08 |
| Share of added flower that sells | 75% | Feb 2027 | $8.12 | $4.79 | $2.53 | Dec 2026 | $6.93 | $3.89 | $2.71 |
| Share of added flower that sells | 50% | Apr 2027 | $9.56 | $6.46 | $3.48 | Dec 2026 | $7.51 | $5.32 | $3.25 |

**What holds.** Across the tested scenarios (the base and 20 one-at-a-time tests, for both measures), the hold ends between Aug 2026 and Apr 2027, and January 2028 is between $3.25 and $7.84, 46% to 78% below $14.50. January 2029 is between $2.53 and $4.25. The chart's gray band shows this range.

**What moves it.** Four tests move January 2028 by nearly $2 or more: a 5% speed limit ($7.84), anchoring after Michigan's first drop began (month 14: $6.92), a 40% harvest share ($6.46) and half the added flower selling ($6.46). Because the speed limit binds through most of 2027, the pace of the decline rests on it: with no limit or a 15% limit, January 2028 is $3.71 or $3.84 and July 2027 is $6.93. The anchor result follows from Michigan's data: its price was flat from month 6 to 10, then fell 34% from month 10 to month 14, so an anchor at month 14 assumes Minnesota skips that first drop.

**Why some single months look backwards.** Less supply can show a lower price in one month (three-quarters of added flower selling: $2.53 in January 2029 against $2.81 in the base). Michigan's real price bounced between about $2.50 and $3.20 through 2023, and its March 2022 reading sits above both neighbors. Michigan's monthly prices are used as published, so any single month can move by about $1; the rounded labels and the ranges carry the result.

## Adverse combinations

The one-at-a-time tests do not show what happens when several assumptions go wrong together. These combinations pair logically separate assumptions that each push toward a later or smaller decline. The last row stacks every adverse test at once as a stress case; it double-counts related effects on purpose. These runs are reported here, not in the chart's band.

| Combination | Settings | Hold ends | 25% below today by | Jul 2027 | Jan 2028 | Jan 2029 | Adult-use only: 25% below by | Jan 2028 |
|---|---|---|---|---|---|---|---|---|
| Base | Base | Feb 2027 | Apr 2027 | $7.76 | $4.58 | $2.81 | Feb 2027 | $3.48 |
| Later anchor + slow price adjustment | Michigan month 14 anchor, 5% speed limit | Mar 2027 | Aug 2027 | $11.28 | $8.29 | $4.48 | Jun 2027 | $7.44 |
| Fewer plants harvested + weaker sales | 40% harvested, 75% of added flower sells | Apr 2027 | Jun 2027 | $9.56 | $7.65 | $4.20 | Feb 2027 | $6.46 |
| Fewer plants harvested + slower planting | 40% harvested, half the outdoor-season rate | Mar 2027 | May 2027 | $8.69 | $6.93 | $3.88 | Feb 2027 | $5.63 |
| Fewer plants harvested + fewer licenses | 40% harvested, half of approvals | Mar 2027 | May 2027 | $8.69 | $6.93 | $3.88 | Feb 2027 | $5.63 |
| Slow price adjustment + weak sales | 5% speed limit, 50% of added flower sells | Apr 2027 | Sep 2027 | $11.81 | $8.68 | $4.69 | May 2027 | $7.07 |
| Slow supply chain | 5-month harvest lag, 2-month sale lag, 18-month sell-through | Mar 2027 | May 2027 | $8.61 | $4.61 | $3.01 | Mar 2027 | $3.71 |
| Weak production and sales | 40% harvested, half outdoor rate, half of approvals, 75% sells | Apr 2027 | Jun 2027 | $9.56 | $7.27 | $6.46 | Feb 2027 | $6.93 |
| Stress case: every adverse test at once | Month 14 anchor, 5% limit, 40% harvested, 50% sells, half outdoor rate, half of approvals, slow chain | Jan 2028 | Jun 2029 | $14.50 | $13.78 | $11.36 | Aug 2028 | $11.28 |

**What survives.** In all seven combinations the scenario price is at least 25% below $14.50 by September 2027, and January 2028 is between $4.61 and $8.68, 40% to 68% below today. Only the stress case pushes meaningful compression past 2028: its hold lasts to January 2028, and on the combined measure the price is still $9.77 in December 2029, 33% below today. The slow supply chain run passes Michigan's highest level on both measures in November 2029 and stops there. Its late volumes run high because a slower chain calibrates to more flower per harvested plant (100 g against 85 g) to match the same observed card.

## How we will know within six months

By the end of March 2027, OCM will have published data through about January 2027:

1. **Is the planting surge reaching harvest?** About 52,000 plants harvested in September, 83,000 in October, 165,000 in November and 214,000 in December 2026, against 45,835 in August.
2. **Is the harvest turning into sales?** OCM's 12-month flower card at about 453,000 oz for October 2026 and 754,000 oz for January 2027, up from 380,610. A card well below that path moves the result toward the 75% and 50% rows.
3. **When should the price move?** Once the card passes about 800,000 oz (base: February 2027), or the adult-use portion passes about 320,000 oz (adult-use-only run: November 2026). The 12-month median should begin to turn down in the early 2027 readings; the two trailing proxies are around $11 (real) by July 2027.
4. **What would break the scenario?** The median falling well before the card passes 800,000 oz (the hold is wrong; the adult-use-only run fits better), or the card passing 1.9 million oz by July 2027 with the median still near $14 (Michigan's relationship does not transfer).
