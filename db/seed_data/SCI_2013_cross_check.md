# SCI 2013 cross-check against USDA SNAP retailer data

Comparison snapshots: the archived USDA SNAP retailer export for Georgia dated October 2014 (10,194 rows) and the current USDA-FNS ArcGIS export fetched 2026-07-29 (9,314 GA rows, 610 in the city of Atlanta). Web verification of SNAP-dropout candidates was performed in July 2026.

## Methodology

Each parcel's `SITUS` address was normalized (uppercased, punctuation and unit designators stripped, USPS suffix and directional abbreviations, plus aliases for known Atlanta street renamings: MLK Jr Dr variants, Bankhead Hwy / Donald Lee Hollowell Pkwy, Ralph David Abernathy Blvd) and matched against SNAP retailer addresses in the city of Atlanta plus Fulton/DeKalb counties, in two snapshots: the archived October 2014 `GA-EBT.csv` and the current USDA export.

Rows that had a SNAP retailer at the same normalized address in 2014 but not in the current snapshot were then **individually web-verified** (business listings, Yelp open/closed status, chain store locators, redevelopment news — July 2026; verdicts and evidence recorded in `tools/sci_web_verification.csv`). That sweep showed most SNAP dropouts are stores that left the program while staying open, so SNAP absence alone is never treated as proof of closure. A row is **removed only** when it dropped out of SNAP **and** the web check confirms the store is gone (tier CONFIRMED-CLOSED). Every other row is kept, flagged for human review where status is uncertain.

## Tier counts

| Tier | Rows | Action |
|---|---|---|
| CONFIRMED-CLOSED | 4 | REMOVED |
| OPEN-NOT-SNAP | 20 | keep, flagged |
| SNAP-DROPPED | 2 | keep, flagged |
| ACTIVE | 73 | keep |
| FUZZY | 37 | keep, flagged |
| SERVICE-STATION | 32 | keep, flagged |
| NO-NUMBER | 9 | keep, flagged |
| NEVER-SEEN | 69 | keep, flagged |
| **Total** | **246** | |

## CONFIRMED-CLOSED (4) — REMOVED

Had a SNAP retailer at this exact address in 2014, no longer SNAP-authorized, and a web check confirms the store is gone.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match | Web verification (July 2026) |
|---|---|---|---|---|---|
| 1097 LEE ST SW | CONVENIENCE FOOD MARKET 348 | Oakland City | MARKET PLACE | — | Market Place Grocery closed (Yelp); site planned for the Cresent Center shopping development |
| 112 ORMOND ST SE | SUPERMARKET 347 | Summerhill | Sunny's Market | — | Sunny's Market gone; address is now Talat Market Thai restaurant (Michelin Guide; Yelp July 2026) |
| 1355 RALPH D ABERNATHY BLVD SW | CONVENIENCE FOOD MARKET 348 | West End | GEORGIA FOOD MART | — | Georgia Food Mart marked CLOSED on Yelp (Feb 2026) |
| 288 RALPH D ABERNATHY BLVD SW | CONVENIENCE FOOD MARKET 348 | Mechanicsville | Pit Stop Food Store | — | Pit Stop Foods marked CLOSED on Yelp (Feb 2026); Pit Stop Kitchen restaurant now at address |

## OPEN-NOT-SNAP (20) — keep, flagged

Dropped out of SNAP since 2014 but a web check shows the store still operating.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match | Web verification (July 2026) |
|---|---|---|---|---|---|
| 1241 METROPOLITAN PKWY SW | CONVENIENCE FOOD MARKET 348 | Adair Park | PHILLIPS 66 | — | Quick Stop Food Mart open 24h per Yelp (June 2026) and GasBuddy |
| 1257 MORELAND AVE SE | SUPERMARKET 347 | Woodland Hills | Piggly Wiggly 77 | — | Piggly Wiggly open per Yelp (reviews through spring 2026) and its own store website |
| 1362 BOULEVARD SE | CONVENIENCE FOOD MARKET 348 | Benteen Park | EAST ATLANTA FOOD MART | — | East Atlanta Food Mart listed active and open 24h (Yellow Pages); no closure evidence found |
| 1460 BOULEVARD SE | SUPERMARKET 347 | Benteen Park | Carniceria Y Tienda El Progreso 14 | — | El Progreso carniceria/market open per Yelp (June 2026; 166 reviews) |
| 1469 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Venetian Hills | Marathon Food Mart | — | Maraton (Marathon) Food Mart active per Yelp (March 2026) / Nextdoor / Instagram |
| 1683 LAKEWOOD AVE SE | CONVENIENCE FOOD MARKET 348 | Lakewood Heights | Chevron Food Mart | — | Chevron with convenience store open 24h per Yelp (July 2026) and Foursquare |
| 1974 SYLVAN RD SW | CONVENIENCE FOOD MARKET 348 | Sylvan Hills | Quick Stop 3 | — | Quick Stop store listed on Yelp; companion Texaco listing updated Feb 2026 |
| 1981 JOSEPH E BOONE BLVD NW | CONVENIENCE FOOD MARKET 348 | Grove Park | Ak Food Store | — | A K Food Store per Yelp (May 2026); active Western Union agent location |
| 2050 SYLVAN RD SW | CONVENIENCE FOOD MARKET 348 | Sylvan Hills | CHEVRON FOOD MART | — | Chevron open 24/7 per Yelp / Waze / DoorDash listings (2026) |
| 2060 PEACHTREE RD NW | CONVENIENCE FOOD MARKET 348 | E1 | Peachtree Food & Gas LLC | — | Sunoco open 24h per Yelp (June 2026) and GasBuddy |
| 2118 DEFOORS FERRY RD NW | CONVENIENCE FOOD MARKET 348 | Underwood Hills | Shell Food Mart | — | Shell station with C-store per find.shell.com and Yelp (April 2026) |
| 2176 COUNTY LINE RD SW | CONVENIENCE FOOD MARKET 348 | Elmco Estates | Our Convenience Store | — | Our Convenience Store per Yelp (July 2026) and directory listings |
| 2261 CASCADE RD SW | CONVENIENCE FOOD MARKET 348 | Cascade Avenue/Road | ATLANTA FOOD MART | — | Shell station and Cascade Food Mart listings active (Tripadvisor / Nextdoor / Yellow Pages) |
| 2331 PEACHTREE RD NE | CONVENIENCE FOOD MARKET 348 | Peachtree Hills | Chevron | — | Chevron Food Mart open 24h per Yelp (June 2026) and Foursquare |
| 337 FLETCHER ST SW | CONVENIENCE FOOD MARKET 348 | Pittsburgh | Double O Food Mart | — | Maxing Groceries convenience store operating at address per Yelp (Nov 2025) |
| 345 PHARR RD NE | CONVENIENCE FOOD MARKET 348 | Garden Hills | Pharr Food & Gas | — | Pharr Road Convenience Store (Chevron) open 24h per Yelp (July 2026) |
| 3556 EMPIRE BLVD SW | CONVENIENCE FOOD MARKET 348 | Glenrose Heights | Empire Service Mart LLC | — | Empire Food Mart per Yelp (April 2026); Valero's own site lists this station as active |
| 535 LEE ST SW | CONVENIENCE FOOD MARKET 348 | West End | Lee Street BP 535 | — | Old BP Foodmart listing closed but a Shell operates at the same address open 24h (Yelp July 2026) |
| 639 MOROSGO DR NE | CONVENIENCE FOOD MARKET 348 | Lindbergh/Morosgo | Chevron / Sydney Food Mart 138 | — | Chevron open 24h per Yelp (June 2026) and GasBuddy |
| 834 HANK AARON DR SE | CONVENIENCE FOOD MARKET 348 | Summerhill | STADIUM GROCERY & MORE | — | Stadium Grocery & More has active listings (Yelp Aug 2025; BBB profile); no closure evidence found |

## SNAP-DROPPED (2) — keep, flagged

Dropped out of SNAP since 2014; web evidence of current status is ambiguous.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match | Web verification (July 2026) |
|---|---|---|---|---|---|
| 1990 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Grove Park | Citgo Food Mart | — | Citgo Foodmart marked CLOSED on Yelp (March 2026) but bp.com lists a station at this address |
| 3113 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Southwest | SHELL FOOD MART | — | Shell Food Mart marked CLOSED on Yelp (July 2026) but GA license records list Shiv Food Mart at address |

## ACTIVE (73) — keep

SNAP-authorized food retailer operates at this address today.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match |
|---|---|---|---|---|
| 1001 NORTHSIDE DR NW | CONVENIENCE FOOD MARKET 348 | Home Park | Best For Less | Best For Less |
| 1111 MORELAND AVE SE | CONVENIENCE FOOD MARKET 348 | Ormewood Park | BP Food Shop | Moreland Food Mart |
| 1161 PONCE DE LEON AVE NE | SERVICE STATION WITH BAYS 333 | Poncey-Highland | Exxon Food Mart | Jena Investment Inc |
| 1401 MORELAND AVE SE | CONVENIENCE FOOD MARKET 348 | Custer/McDonough/Guice | Chevron Food Mart 1401 | Ans Three D Inc 0 |
| 1450 DONNELLY AVE SW | SERVICE STATION WITH BAYS 333 | West End | — | Gas Express LLC dba Circle K 142 |
| 1461 MORELAND AVE SE | SUPERMARKET 347 | Custer/McDonough/Guice | Aldi 58 | ALDI 69093 69093 |
| 1521 PEACHTREE ST NE | SERVICE STATION WITH BAYS 333 | Midtown | Chevron Food Mart | Uptown Station Inc |
| 1570 MONROE DR NE | CONVENIENCE FOOD MARKET 348 | Piedmont Heights | — | Monroe Chevron |
| 160 PONCE DE LEON AVE NE | CONVENIENCE FOOD MARKET 348 | Midtown | — | Bp Food Mart |
| 1634 LAKEWOOD AVE SE | CONVENIENCE FOOD MARKET 348 | Lakewood Heights | Good Time Food Mart | Quick Pick Foodmart |
| 1677 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Grove Park | WESTLAKE FOOD MART | Westlake Food Mart |
| 1695 PRYOR RD SW | CONVENIENCE FOOD MARKET 348 | Betmar LaVilla | CJ GROCERY MARKET | 3 Way Grocery |
| 1720 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Mozley Park | MOZLEY PARK FOODMART | Speedzone Shell |
| 1722 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | R1 | CHEVRON FOOD MART | CHEVRON FOOD MART |
| 1790 HOWELL MILL RD NW | CONVENIENCE FOOD MARKET 348 | Underwood Hills | Howell Mill Shell | Shell Food Mart |
| 180 RALPH D ABERNATHY BLVD SW | CONVENIENCE FOOD MARKET 348 | Mechanicsville | SOFIA VENTURES | Abernathy Bp |
| 1850 METROPOLITAN PKWY SW | CONVENIENCE FOOD MARKET 348 | Sylvan Hills | Shell Food Mart | Food Mart |
| 1892 HOWELL MILL RD NW | CONVENIENCE FOOD MARKET 348 | Wildwood (NPU-C) | — | Shell Food Mart |
| 1960 PERKERSON RD SW | SERVICE STATION WITH BAYS 333 | Sylvan Hills | — | Eastpoint Grocery |
| 1970 MOORES MILL RD NW | CONVENIENCE FOOD MARKET 348 | D1 | Maxi Food Mart | Food Mart 0 |
| 1980 DELOWE DR SW | CONVENIENCE FOOD MARKET 348 | Campbellton Road | Delowe Valero | Hungry Mart |
| 2000 DELOWE DR SW | CONVENIENCE FOOD MARKET 348 | Campbellton Road | Delowe Marathon | Food Center |
| 2020 BOLTON RD NW | CONVENIENCE FOOD MARKET 348 | Riverside | Riverside Chevron NO | Chevron Food Mart |
| 2020 HOWELL MILL RD NW | SUPERMARKET 347 | Springlake | PUBLIX 1119; Rite Aid 11793 | PUBLIX 1119; Walgreens 17037 |
| 2099 PEACHTREE RD NE | SUPERMARKET 347 | E1 | The Fresh Market 061 | The Fresh Market 061 |
| 2111 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Adams Park | Quick Pick Campbellton Foodmart | Lucky Food Mart 0 |
| 221 CLEVELAND AVE SW | CONVENIENCE FOOD MARKET 348 | Browns Mill Park | CHEVRON FOOD MART | BP Cleveland |
| 2456 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Harland Terrace | Chevron Food Mart | Mlk Chevron 2456 Llc |
| 2621 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE / FAST FOOD MARKET 326* | Center Hill | PIC 'N' PAY | Pick And Pay |
| 2656 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Collier Heights | Rite Stuff Food Store | Chevron Food Mart |
| 2784 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Collier Heights | — | Hop In Food Mart |
| 29 MORELAND AVE SE | SUPERMARKET 347 | Reynoldstown | — | Texaco Food Mart |
| 2900 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Southwest | — | Big H Food Mart |
| 2989 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Southwest | CITGO FOOD MART | CITGO FOOD MART |
| 3004 PIEDMONT RD NE | CONVENIENCE FOOD MARKET 348 | Garden Hills | — | BP Food Mart |
| 3012 JONESBORO RD SE | CONVENIENCE FOOD MARKET 348 | South River Gardens | Chevron Food Mart | Jones Prime LLC |
| 3015 JONESBORO RD SE | CONVENIENCE FOOD MARKET 348 | Orchard Knob | Pure Food Mart | Pure Food Mart |
| 3102 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | I1 | ZTS Food Mart | ZTS Food Mart |
| 3183 PEACHTREE RD NE | SUPERMARKET 347 | Buckhead Village | Trader Joes 735 | Trader Joe's 735 |
| 3330 M L KING JR DR SW | CONVENIENCE / FAST FOOD MARKET 326* | Adamsville | — | MLK Texaco |
| 336 JOSEPH E LOWERY BLVD NW | SERVICE STATION WITH BAYS 333 | Bankhead | — | Chevron Food Mart 0 |
| 343 JOSEPH E LOWERY BLVD SW | CONVENIENCE FOOD MARKET 348 | Harris Chiles | Lowery | Gas Express LLC dba Circle K 153 |
| 350 MORELAND AVE NE | CONVENIENCE FOOD MARKET 348 | Inman Park | Amoco Little Five Points | Circle K #185 |
| 3535 PEACHTREE RD NE | SUPERMARKET 347 | Lenox | Target Store T-1197 | PUBLIX 664; Target Store 1197 |
| 3550 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Adamsville | — | Quick Stop Food Mart |
| 356 BOULEVARD NE | CONVENIENCE FOOD MARKET 348 | Old Fourth Ward | BP FOOD MART | Blvd Food Mart |
| 3580 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | P2 | Raceway Campbellton | Raceway Campbellton |
| 3640 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | P2 | Citgo Food Mart | Valero Food Mart |
| 3657 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Adamsville | MLK CITGO FOOD MART | Quick Foodmart |
| 3660 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Adamsville | Prime Chevron | Prime Chevron |
| 3669 POWERS FERRY RD NW | CONVENIENCE FOOD MARKET 348 | East Chastain Park | — | Buckhead Shoppe |
| 371 BOULEVARD SE | CONVENIENCE FOOD MARKET 348 | Grant Park | CHEVRON FOOD MART | CHEVRON FOOD MART |
| 372 MORELAND AVE NE | CONVENIENCE FOOD MARKET 348 | Inman Park | Chevron Park and Food 372 | Moreland Food Mart |
| 374 CLEVELAND AVE SW | CONVENIENCE FOOD MARKET 348 | Hammond Park | QUICK SAVE | Quick Save/Shell Food Mart |
| 3750 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | P2 | COUSINS TEXACO | Cousins Texaco |
| 3843 JONESBORO RD SE | CONVENIENCE FOOD MARKET 348 | South River Gardens | Food Mart | Exxon Gas Station |
| 387 HILL ST SE | CONVENIENCE FOOD MARKET 348 | Grant Park | — | Hill Street Shell |
| 388 LUCKIE ST NW | CONVENIENCE FOOD MARKET 348 | Downtown | LUCKIE STREET GROCERY | LUCKIE STREET GROCERY |
| 4341 ROSWELL RD NE | CONVENIENCE FOOD MARKET 348 | North Buckhead | — | Roswell Chevron |
| 4472 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Elmco Estates | — | Family Dollar 10677 |
| 4499 ROSWELL RD NE | SERVICE STATION WITH BAYS 333 | North Buckhead | — | Shell Food Mart |
| 4511 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | P1 | S.S. FOOD MART | Shell Food Mart |
| 486 PONCE DE LEON AVE NE | CONVENIENCE FOOD MARKET 348 | Midtown | Shell Food Mart | Circle K Shell |
| 490 FAIRBURN RD SW | CONVENIENCE FOOD MARKET 348 | Fairburn Mays | — | 490 Fairburn Rd Llc 0 |
| 490 WHITEHALL ST SW | CONVENIENCE FOOD MARKET 348 | Castleberry Hill | — | Whitehall Shell |
| 516 LEE ST SW | SUPERMARKET 347 | West End | HARDY'S SUPERMARKET | Ez Market |
| 575 CHAPPELL RD NW | CONVENIENCE FOOD MARKET 348 | Bankhead | — | Chappell Road Inc |
| 605 BOULEVARD NE | CONVENIENCE / FAST FOOD MARKET 326* | Old Fourth Ward | North Avenue Food Mart | North Avenue Food Mart |
| 655 CLEVELAND AVE SW | SERVICE STATION W/O BAYS 334 | Perkerson | — | Citgo Food Mart |
| 8 CLEVELAND AVE SE | SERVICE STATION WITH BAYS 333 | Browns Mill Park | — | 24/7 Food Mart |
| 807 CONLEY RD SE | CONVENIENCE FOOD MARKET 348 | South River Gardens | CONLEY SUPER STATION | Conley Food Mart |
| 820 JAMES JACKSON PKWY NW | SUPERMARKET 347 | Brookview Heights | BUY LOW SUPERMARKET | BUY LOW SUPERMARKET |
| 902 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | English Avenue | BANKHEAD SHELL | Bankhead Shell |

## FUZZY (37) — keep, flagged

Near match in the current snapshot; address formats differ.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match |
|---|---|---|---|---|
| 1003 MC DANIEL ST SW | SUPERMARKET 347 | Pittsburgh | — | Welcome Foods Mcdaniel |
| 1072 CASCADE AVE SW | CONVENIENCE FOOD MARKET 348 | Cascade Avenue/Road | — | Cascade Food Mart |
| 1117 LEE ST | CONVENIENCE FOOD MARKET 348 | Oakland City | — | Lee Petro |
| 121 CLEVELAND AVE SE | CONVENIENCE FOOD MARKET 348 | Glenrose Heights | — | A Food Mart |
| 1539 PIEDMONT AVE NE | CONVENIENCE FOOD MARKET 348 | Morningside/Lenox Park | — | CVS PHARMACY 4747; Publix 599 |
| 1629 LAKEWOOD AVE SE | CONVENIENCE FOOD MARKET 348 | Lakewood Heights | Express Food Mart | Quick Pick Foodmart |
| 1681 RALPH D ABERNATHY BLVD SW | CONVENIENCE FOOD MARKET 348 | I2 | — | Bp Food Mart |
| 1739 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Mozley Park | — | Speedzone Chevron |
| 180 PONCE DE LEON AVE | CONVENIENCE FOOD MARKET 348 | Midtown | — | Chevron Food Mart |
| 1842 PIEDMONT AVE NE | SERVICE STATION WITH BAYS 333 | Piedmont Heights | — | Sprouts Farmers Market 519 |
| 1888 PEACHTREE RD NW | CONVENIENCE FOOD MARKET 348 | Ardmore | Peachtree Texaco Food Mart | Shell Food Mart |
| 202 ANDERSON AVE NW | SERVICE STATION WITH BAYS 333 | Dixie Hills | — | Anderson Food Mart |
| 2095 METROPOLITAN PKWY SW | CONVENIENCE FOOD MARKET 348 | Sylvan Hills | Cross Road BP | Atlanta Texaco/ Ez Market 0 |
| 2200 MONROE DR NE | SERVICE STATION WITH BAYS 333 | Piedmont Heights | — | Monroe Drive Chevron |
| 2239 CHESHIRE BRIDGE RD | CONVENIENCE FOOD MARKET 348 | Lindridge/Martin Manor | — | Quick Mart |
| 2247 CASCADE RD SW | CONVENIENCE FOOD MARKET 348 | Cascade Avenue/Road | — | CVS Pharmacy 5395 |
| 2319 CHESHIRE BRIDGE RD | CONVENIENCE FOOD MARKET 348 | Lindridge/Martin Manor | — | AAA 2317 Inc |
| 2353 CHESHIRE BRIDGE RD | CONVENIENCE FOOD MARKET 348 | Lindridge/Martin Manor | — | CVS PHARMACY 2186 |
| 241 MEMORIAL DR SE | CONVENIENCE FOOD MARKET 348 | Grant Park | — | Bp Food Mart 0 |
| 2595 M L KING JR DR NW | CONVENIENCE FOOD MARKET 348 | Harland Terrace | — | Mlk Westland Bp Inc. |
| 294 NORTHSIDE DR SW | CONVENIENCE / FAST FOOD MARKET 326* | Castleberry Hill | — | Northside Texaco |
| 3202 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | I1 | — | Discount Food Mart |
| 3235 M L KING JR DR NW | CONVENIENCE FOOD MARKET 348 | I1 | — | EZ Shoper |
| 3255 M L KING JR DR NW | CONVENIENCE FOOD MARKET 348 | I1 | — | Circle K |
| 3260 BANKHEAD HWY NW | CONVENIENCE FOOD MARKET 348 | Bankhead/Bolton | — | Star Chevron Food Mart |
| 3601 M L KING JR DR SW | CONVENIENCE FOOD MARKET 348 | Adamsville | Shell Food Mart | DollarTree 7375 |
| 3749 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Ben Hill Acres | Campbellton Texaco | Cousins Texaco |
| 377 EDGEWOOD AVE SE | SERVICE STATION WITH BAYS 333 | Sweet Auburn | — | Goodr Community Market On Edgewood |
| 400 EDGEWOOD AVE NE | CONVENIENCE FOOD MARKET 348 | Sweet Auburn | — | Edgewood Foodmart Inc. |
| 496 PLASTER AVE NE | CONVENIENCE FOOD MARKET 348 | E1 | — | Plaster Shell & Food |
| 507 JOSEPH E LOWERY BLVD | CONVENIENCE FOOD MARKET 348 | West End | — | Lowery Food Mart |
| 568 CHAPPELL RD | CONVENIENCE FOOD MARKET 348 | Grove Park | — | Big A Food Mart |
| 598 CASCADE AVE SW | SUPERMARKET 347 | West End | — | KROGER 412 |
| 600 SPRING ST NW | CONVENIENCE FOOD MARKET 348 | Downtown | — | BP Gas Station |
| 761 SIDNEY MARCUS BLVD | CONVENIENCE FOOD MARKET 348 | Lindbergh/Morosgo | — | QUIKTRIP 744 |
| 825 M L KING JR DR NW | SUPERMARKET 347 | Vine City | — | Walmart 7601 |
| 840 MC DONOUGH BLVD SE | SERVICE STATION W/O BAYS 334 | Custer/McDonough/Guice | — | Exxon Food Mart 1 |

## SERVICE-STATION (32) — keep, flagged

Gas stations may or may not be SNAP-authorized; SNAP absence proves nothing about the parcel.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match |
|---|---|---|---|---|
| 1043 VIRGINIA AVE NE | SERVICE STATION WITH BAYS 333 | Virginia Highland | — | — |
| 105 MC DONOUGH BLVD SE | SERVICE STATION WITH BAYS 333 | South Atlanta | — | — |
| 1060 JEFFERSON ST NW | SERVICE STATION WITH BAYS 333 | Bankhead | — | — |
| 111 BOULEVARD NE | SERVICE STATION WITH BAYS 333 | Old Fourth Ward | TEXACO BOULEVARD | — |
| 1180 COLLIER RD NW | SERVICE STATION W/O BAYS 334 | Underwood Hills | — | — |
| 1184 SPRING ST NW | SERVICE STATION WITH BAYS 333 | Midtown | — | — |
| 1285 JOSEPH E BOONE BLVD NW | SERVICE STATION W/O BAYS 334 | Bankhead | — | — |
| 1313 WEST PACES FERRY RD NW | SERVICE STATION WITH BAYS 333 | Randall Mill | — | — |
| 1341 METROPOLITAN PKWY SW | SERVICE STATION WITH BAYS 333 | Capitol View | Metro Quik Mart | — |
| 1400 W PACES FERRY RD | SERVICE STATION WITH BAYS 333 | Paces | — | — |
| 1475 CARROLL DR NW | SERVICE STATION W/O BAYS 334 | Hills Park | — | — |
| 1686 JONESBORO RD SE | SERVICE STATION WITH BAYS 333 | Lakewood Heights | — | — |
| 1695 NORTHSIDE DR NW | SERVICE STATION WITH BAYS 333 | Loring Heights | — | — |
| 1811 LAKEWOOD AVE SE | SERVICE STATION W/O BAYS 334 | Lakewood Heights | — | — |
| 2079 BOLTON RD NW | SERVICE STATION WITH BAYS 333 | Riverside | — | — |
| 2220 JONESBORO RD SE | SERVICE STATION WITH BAYS 333 | Norwood Manor | JENKINS SUPERETTE | — |
| 2271 CASCADE RD SW | SERVICE STATION WITH BAYS 333 | Cascade Avenue/Road | — | — |
| 2320 CHESHIRE BRIDGE RD | SERVICE STATION W/O BAYS 334 | Lindridge/Martin Manor | — | — |
| 2324 M L KING JR DR SW | SERVICE STATION WITH BAYS 333 | Florida Heights | — | — |
| 247 MORELANDALS RD | SERVICE STATION W/O BAYS 334 | Reynoldstown | — | — |
| 2500 FAIRBURN RD SW | SERVICE STATION WITH BAYS 333 | Ben Hill Pines | — | — |
| 2716 M L KING JR DR SW | SERVICE STATION WITH BAYS 333 | Harland Terrace | — | — |
| 2836 LAKEWOOD AVE SW | SERVICE STATION WITH BAYS 333 | Sylvan Hills | — | — |
| 2866 METROPOLITAN PKWY SW | SERVICE STATION WITH BAYS 333 | Hammond Park | Haribol Food Market | — |
| 306 MILTON AVE SE | SERVICE STATION W/O BAYS 334 | Chosewood Park | — | — |
| 3639 PEACHTREE RD NE | SERVICE STATION WITH BAYS 333 | Ridgedale Park | — | — |
| 4402 ROSWELL RD NE | SERVICE STATION WITH BAYS 333 | East Chastain Park | — | — |
| 610 METROPOLITAN PKWY SW | SERVICE STATION WITH BAYS 333 | Pittsburgh | — | — |
| 635 LINDBERGH DR NE | SERVICE STATION WITH BAYS 333 | Lindbergh/Morosgo | — | — |
| 664 PRYOR ST SW | SERVICE STATION WITH BAYS 333 | Mechanicsville | — | — |
| 808 DONALD LEE HOLLOWELL PKWY NW | SERVICE STATION WITH BAYS 333 | English Avenue | — | — |
| 900 NORTHSIDE DR NW | SERVICE STATION WITH BAYS 333 | Marietta Street Artery | — | — |

## NO-NUMBER (9) — keep, flagged

SITUS has no street number, so address matching is impossible.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match |
|---|---|---|---|---|
| BROWN MILL RD | CONVENIENCE FOOD MARKET 348 | Glenrose Heights | — | — |
| CLEVELAND AVE SW | CONVENIENCE FOOD MARKET 348 | Perkerson | — | — |
| COLLIER RD | CONVENIENCE FOOD MARKET 348 | C2 | — | — |
| DECATUR ST SE | FOOD STANDS 323 | Downtown | — | — |
| GLENWOOD AVE SE | FOOD STANDS 323 | Grant Park | — | — |
| GREENBRIAR PKWY SW | CONVENIENCE FOOD MARKET 348 | Greenbriar | — | — |
| GREENBRIAR PKWY SW | SUPERMARKET 347 | Greenbriar | — | — |
| HARWELL RD NW | CONVENIENCE FOOD MARKET 348 | I1 | — | — |
| LUCILE AVE SW | FOOD STANDS 323 | Westview | — | — |

## NEVER-SEEN (69) — keep, flagged

Not in the 2014 or current snapshot; cannot distinguish closed from never-SNAP-authorized.

| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match |
|---|---|---|---|---|
| 101 HIGHTOWER RD NW | CONVENIENCE FOOD MARKET 348 | Westhaven | — | — |
| 1023 NORTH HIGHLAND AVE | CONVENIENCE FOOD MARKET 348 | Virginia Highland | — | — |
| 1079 NORTH AVE NE | CONVENIENCE FOOD MARKET 348 | Poncey-Highland | — | — |
| 1085 NORTH AVE NE | CONVENIENCE FOOD MARKET 348 | Poncey-Highland | — | — |
| 1098 RALPH D ABERNATHY BLVD SW | CONVENIENCE FOOD MARKET 348 | West End | — | — |
| 1111 EUCLID AVE NE | SUPERMARKET 347 | Inman Park | — | — |
| 116 SPRING ST SW | FOOD STANDS 323 | Downtown | — | — |
| 1163 METROPOLITAN PKWY SW | CONVENIENCE FOOD MARKET 348 | Adair Park | — | — |
| 1176 NEW CHATTAHOOCHEE AVE NW | CONVENIENCE FOOD MARKET 348 | Underwood Hills | — | — |
| 1371 RALPH D ABERNATHY BLVD SW | FOOD STANDS 323 | Westview | — | — |
| 142 FLAT SHOALS AVE SE | CONVENIENCE FOOD MARKET 348 | Reynoldstown | — | — |
| 1465 BOULEVARD SE | CONVENIENCE FOOD MARKET 348 | Chosewood Park | — | — |
| 150 PINE ST NE | CONVENIENCE / FAST FOOD MARKET 326* | Downtown | — | — |
| 151 CLEVELAND AVE SW | CONVENIENCE FOOD MARKET 348 | Browns Mill Park | — | — |
| 1568 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Grove Park | — | — |
| 1572 PIEDMONT AVE NE | FOOD STANDS 323 | Piedmont Heights | — | — |
| 160 JOHN WESLEY DOBBS | CONVENIENCE FOOD MARKET 348 | Downtown | — | — |
| 1617 JOSEPH E BOONE BLVD NW | CONVENIENCE FOOD MARKET 348 | Grove Park | — | — |
| 1660 JONESBORO RD SE | SUPERMARKET 347 | Lakewood Heights | — | — |
| 1681 JONESBORO RD SE | SUPERMARKET 347 | Lakewood Heights | — | — |
| 180 ELM ST SW | CONVENIENCE FOOD MARKET 348 | Atlanta University Center | — | — |
| 180 UNIVERSITY AVE SW | CONVENIENCE FOOD MARKET 348 | Pittsburgh | — | — |
| 1856 PIEDMONT AVE NE | CONVENIENCE FOOD MARKET 348 | Piedmont Heights | — | — |
| 1867 JONESBORO RD SE | CONVENIENCE FOOD MARKET 348 | Lakewood Heights | — | — |
| 1875 PEACHTREE RD NE | CONVENIENCE FOOD MARKET 348 | Brookwood Hills | — | — |
| 1913 HOLLYWOOD RD NW | SUPERMARKET 347 | Riverside | — | — |
| 1975 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Venetian Hills | — | — |
| 1977 M L KING JR DR NW | CONVENIENCE FOOD MARKET 348 | I2 | — | — |
| 1991 MARIETTA BLV NW | CONVENIENCE FOOD MARKET 348 | Hills Park | — | — |
| 2174 DONALD LEE HOLLOWELL PKWY NW | SUPERMARKET 347 | Grove Park | — | — |
| 2193 PEACHTREE RD NE | CONVENIENCE FOOD MARKET 348 | E1 | — | — |
| 2251 MARIETTA BLV NW | CONVENIENCE FOOD MARKET 348 | D1 | — | — |
| 2448 CHESHIRE BRIDGE RD | CONVENIENCE FOOD MARKET 348 | Lindridge/Martin Manor | — | — |
| 2489 JONESBORO RD SE | CONVENIENCE FOOD MARKET 348 | Browns Mill Park | — | — |
| 2695 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | Southwest | — | — |
| 2755 METROPOLITAN PKWY | CONVENIENCE FOOD MARKET 348 | Hammond Park | — | — |
| 2795 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Brookview Heights | — | — |
| 3 ASHBY ST SW | CONVENIENCE FOOD MARKET 348 | Ashview Heights | — | — |
| 3030 FOUNTAINBLEAU SW | SUPERMARKET 347 | Greenbriar | — | — |
| 3130 CAMPBELLTON RD SW 1 | FOOD STANDS 323 | Southwest | — | — |
| 3170 BANKHEAD HWY NW | CONVENIENCE FOOD MARKET 348 | Collier Heights | — | — |
| 3195 BANKHEAD HWY NW | CONVENIENCE FOOD MARKET 348 | Brookview Heights | — | — |
| 3263 BANKHEAD HWY NW | CONVENIENCE FOOD MARKET 348 | English Park | — | — |
| 329 FOURTEENTH ST NW | CONVENIENCE FOOD MARKET 348 | Home Park | — | — |
| 3300 PIEDMONT RD NE | CONVENIENCE / FAST FOOD MARKET 326* | Buckhead Forest | — | — |
| 332 FLETCHER ST SW | CONVENIENCE FOOD MARKET 348 | Pittsburgh | — | — |
| 334 MC DANIEL ST SW | FOOD STANDS 323 | Castleberry Hill | — | — |
| 345 EDGEWOOD AVE SE | CONVENIENCE FOOD MARKET 348 | Sweet Auburn | — | — |
| 3465 NORTHSIDE PKY NW | CONVENIENCE FOOD MARKET 348 | Randall Mill | — | — |
| 3550 CAMPBELLTON RD SW | CONVENIENCE FOOD MARKET 348 | P2 | — | — |
| 364 HILL ST SE | CONVENIENCE FOOD MARKET 348 | Grant Park | — | — |
| 3819 JONESBORO RD SE | CONVENIENCE FOOD MARKET 348 | South River Gardens | — | — |
| 420 FOURTEENTH ST NW | CONVENIENCE / FAST FOOD MARKET 326* | Home Park | — | — |
| 4454 CAMPBELLTON RD SW | FOOD STANDS 323 | Elmco Estates | — | — |
| 448 BOULEVARD AVE SE | CONVENIENCE FOOD MARKET 348 | Grant Park | — | — |
| 4480 NORTHSIDE DR NW | CONVENIENCE FOOD MARKET 348 | Mt. Paran/Northside | — | — |
| 513 PONCE DE LEON AVE NE | CONVENIENCE FOOD MARKET 348 | Old Fourth Ward | — | — |
| 608 FOURTEENTH ST NW | CONVENIENCE FOOD MARKET 348 | Home Park | — | — |
| 664 CLEBURNE TER NE | SUPERMARKET 347 | Poncey-Highland | — | — |
| 683 ASHBY ST SW | SUPERMARKET 347 | West End | — | — |
| 699 PONCE DE LEON AVE NE | SUPERMARKET 347 | Poncey-Highland | — | — |
| 766 JOSEPH E BOONE BLVD | CONVENIENCE FOOD MARKET 348 | Vine City | — | — |
| 825 MORELAND AVE SE | CONVENIENCE FOOD MARKET 348 | Ormewood Park | — | — |
| 923 LEE ST SW | CONVENIENCE FOOD MARKET 348 | West End | — | — |
| 948 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Bankhead | — | — |
| 949 MAYSON TURNER RD NW | CONVENIENCE FOOD MARKET 348 | Washington Park | — | — |
| 970 SPRING ST NW | CONVENIENCE FOOD MARKET 348 | Midtown | — | — |
| 995 DONALD LEE HOLLOWELL PKWY NW | CONVENIENCE FOOD MARKET 348 | Bankhead | — | — |
| 999 CHATTAHOOCHEE AVE NW | FOOD STANDS 323 | Underwood Hills | — | — |
