# Results

## Assessing performance of a snooping based cache coherence protocol (3 points)

| CPU cores | CPI (mean) | CPI (std dev) | L1 miss ratio (mean) | L1 miss ratio (std dev) | L3 upgrade requests | Snoop traffic |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| 2 | 1.632603 | 0.0188359 | 0.0662630 | 0.00068984 | 57613 | 6057600 |
| 4 | 1.7655655 | 0.0585164 | 0.0634096 | 0.0020406 | 27551 | 10108736 |
| 8 | 1.7081445 | 0.1098592 | 0.0434088 | 0.0042796 | 15347 | 10597312 |
| 16 | 1.5530083 | 0.1144708 | 0.0232634 | 0.0058058 | 16170 | 14334144 |

## Assessing the impact of false sharing on performance (4 points)

### Without false sharing
| CPU cores | CPI (mean) | CPI (std dev) | Execution time (simSeconds) | Invalidations | Loads (I) | Loads (S) | Loads (E) | Loads (M) | L2 GETS | L2 GETX | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| 2 | 6.1920160 | 3.3451694 | 0.001054 | 556 | 10 | 65624 | 106540 | 571507 | 4191 | 91 | 1188 | 17526 | 1088 |
| 4 | 11.2813025 | 4.9507919 | 0.000541 | 727 | 20 | 70862 | 75834 | 608524 | 4291 | 207 | 1634 | 16168 | 1234 |
| 8 | 21.0251564 | 6.8567865 | 0.000299 | 1756 | 59 | 74196 | 121817 | 582236 | 4515 | 436 | 3832 | 18666 | 1532 |
| 16 | 36.3256251 | 8.8074021 | 0.000200 | 3110 | 183 | 88164 | 104264 | 672247 | 4961 | 986 | 7054 | 25296 | 1908 |

### With false sharing
| CPU cores | CPI (mean) | CPI (std dev) | Execution time (simSeconds) | Invalidations | Loads (I) | Loads (S) | Loads (E) | Loads (M) | L2 GETS | L2 GETX | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| 2 | 7.5842410 | 3.3485027 | 0.001439 | 30375 | 29920 | 95485 | 82047 | 532824 | 35097 | 33355 | 182152 | 198724 | 1136 |
| 4 | 13.0854872 | 5.0978384 | 0.000760 | 52528 | 49048 | 85177 | 80996 | 527596 | 55102 | 109519 | 235586 | 250478 | 1284 |
| 8 | 26.2885862 | 7.1924559 | 0.000622 | 103273 | 64883 | 71642 | 106762 | 512500 | 244206 | 261312 | 337872 | 352978 | 1602 |
| 16 | 42.7491048 | 10.0075764 | 0.000354 | 100336 | 64525 | 83055 | 112452 | 562595 | 234557 | 251182 | 332520 | 353076 | 1828 |

## Assessing the performance of interconnection network (3 points)

### Crossbar Network
| CPU cores | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|
| 2 | | | |
| 4 | | | |
| 8 | | | |
| 16 | | | |

### Ring Network
| CPU cores | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|
| 2 | | | |
| 4 | | | |
| 8 | | | |
| 16 | | | |

### Point-to-Point Network
| CPU cores | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|
| 2 | | | |
| 4 | | | |
| 8 | | | |
| 16 | | | |