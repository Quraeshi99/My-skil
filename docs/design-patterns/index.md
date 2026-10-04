# System Design Pattern Library

This directory contains the blueprints for 28+ complex systems. Use these as references during the 'Architectural Design' phase.

## 🟢 Core Fundamentals
- **Scaling:** Vertical vs Horizontal scaling strategies.
- **Estimation:** Back-of-the-envelope calculation techniques.
- **Framework:** Standard steps for designing any system.

## 🟡 Component-Level Patterns
- **Rate Limiter:** Token Bucket, Leaking Bucket, Sliding Window.
- **Consistent Hashing:** Hash rings, virtual nodes for load distribution.
- **Key-Value Store:** CAP theorem, Gossip Protocol, Quorum Consensus, Merkle Trees.
- **Unique-ID Generator:** Ticket servers, Snowflake IDs, UUIDs.

## 🔵 System-Level Blueprints
- **Content Delivery:** URL Shorteners, Web Crawlers, S3-like Object Storage.
- **Communication:** Notification Systems, Chat Systems (Websockets/Long Polling), Distributed Message Queues.
- **Social/Discovery:** News Feed, Search Autocomplete, Proximity Services (Geohashing, Quadtrees), Google Maps.
- **Media:** Youtube (Transcoding, DAG scheduler, CDN).
- **Enterprise:** Google Drive (Delta sync), Hotel Reservation (Locking), Payment Systems (Idempotency), Digital Wallets (Saga pattern, 2PC), Stock Exchanges (Lmax Disruptor style).

## 🔴 Monitoring & Maintenance
- **Observability:** Metrics Monitoring and Alerting Systems.
- **Aggregation:** Ad Click Event Aggregation (Lambda/Kappa architecture).
