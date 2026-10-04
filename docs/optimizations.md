# Deep Dive: Optimization Techniques

## 1. Memory-First Strategy
Disk access is the "Death Valley" of performance. By moving the entire active dataset into RAM (Redis), we reduce access time from milliseconds to microseconds. 

## 2. The UUID Advantage
Using sequential IDs requires the system to know the "last ID used," creating a synchronization bottleneck across clusters. 
**Solution:** Use 122-bit UUIDs. The probability of collision is so low that you can generate IDs independently on 100 different servers without any communication between them.

## 3. Redis Clustering & Sharding
A single Redis process is single-threaded. To scale:
- **Sharding:** Split the keyspace across $N$ nodes.
- **Hashing:** Use consistent hashing to determine which node holds a specific key.
- **Read Replicas:** Offload read traffic from masters to replicas.

## 4. Avoiding $O(N)$ in SQL
Common mistakes that kill performance:
- `ORDER BY RANDOM()`: Forces the DB to scan the entire table.
- `COUNT(*)` on huge tables: Scans all rows.
- **Correct Approach:** Maintain a separate counter in Redis or use indexed lookups for random selection.
