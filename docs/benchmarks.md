# Performance Benchmarks

## Framework Comparison (Based on `system-design-journey` and YouTube Data)
| Framework | Avg RPS | CPU Utilization | Note |
| :--- | :--- | :--- | :--- |
| Express.js | ~18k | Low/Medium | High overhead, slow |
| Fastify | ~66k | Medium | Highly efficient |
| Cpeak (Custom) | ~73k | Medium | Near raw Node performance |
| C++ (Drogon) | 1M+ | Optimized | Extreme performance, low latency |

## Storage Comparison (Real-world tests)
| Storage Type | Avg RPS | Bottleneck | Cost |
| :--- | :--- | :--- | :--- |
| PostgreSQL (SSD) | ~35k-66k | Disk I/O (IOPS) | Very High (per IOPS) |
| Redis (Standalone) | ~100k-200k | Single-threaded CPU | Medium |
| Redis (Cluster) | 1M+ | Network Bandwidth | Scalable |

## Hardware Scaling Impact
- **Local/Basic:** Limited by CPU/RAM.
- **AWS C8i:** High compute, but hits 50Gbps network ceiling.
- **AWS C8gn:** Reaches 600Gbps, allowing 1M+ RPS with heavy payloads.
