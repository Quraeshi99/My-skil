# System Architecture: The Road to 1M RPS

## High-Level Data Flow
`Client` $ightarrow$ `Network Load Balancer` $ightarrow$ `C++/Node.js Cluster` $ightarrow$ `Redis Cluster` $ightarrow$ `PostgreSQL (Background Sync)`

## Component Breakdown

### 1. The Entry Point (NLB)
- Operates at Layer 4 (TCP).
- Bypasses HTTP overhead for maximum throughput.
- Distributes traffic across multiple compute nodes.

### 2. The Compute Layer (The Beast Server)
- **Language:** C++ (Drogon) for the core handler.
- **Concurrency:** Multi-threaded, asynchronous I/O.
- **JSON Parsing:** RapidJSON for near-instant serialization.

### 3. The Cache Layer (Redis Cluster)
- **Sharding:** Data is hashed across multiple master nodes.
- **Availability:** Replicas handle read-heavy loads and provide failover.
- **Latency:** Sub-millisecond access times.

### 4. The Persistence Layer (PostgreSQL)
- Acts as the "Source of Truth."
- Not in the critical path of the request/response cycle.
- Updated via asynchronous batch writes from the Redis queue.
