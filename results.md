# Results

## Assessing performance of a snooping based cache coherence protocol (3 points)

| CPU cores | CPI (mean) | CPI (std dev) | L1 miss ratio (mean) | L1 miss ratio (std dev) | L3 upgrade requests | Snoop traffic |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| 2 | 1.632603 | 0.0188359 | 0.0662630 | 1118.64 | 0.0006898 | 6057600 |
| 4 | 1.7655655 | 0.0585164 | 0.0634096 | 0.0020406 | 27551 | 10108736 |
| 8 | 1.7081445 | 0.1098592 | 0.0434088 | 0.0042796 | 15347 | 10597312 |
| 16 | 1.5530083 | 0.1144708 | 0.0232634 | 0.0058058 | 16170 | 14334144 |

## Assessing the impact of false sharing on performance (4 points)

### Without false sharing
| CPU cores | CPI (mean) | CPI (std dev) | Execution time | Invalidations | Loads (I) | Loads (S) | Loads (E) | Loads (M) | L2 GETS | L2 GETX | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| 2 | | | | | | | | | | | | | |
| 4 | | | | | | | | | | | | | |
| 8 | | | | | | | | | | | | | |
| 16 | | | | | | | | | | | | | |

### With false sharing
| CPU cores | CPI (mean) | CPI (std dev) | Execution time | Invalidations | Loads (I) | Loads (S) | Loads (E) | Loads (M) | L2 GETS | L2 GETX | Network traffic (Req) | Network traffic (Resp) | Network traffic (WB) |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| 2 | | | | | | | | | | | | | |
| 4 | | | | | | | | | | | | | |
| 8 | | | | | | | | | | | | | |
| 16 | | | | | | | | | | | | | |

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