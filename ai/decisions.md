# Architecture Decision Records (ADR)
Chronological record of technical choices. These are universal patterns applicable to any high-performance stack.

## ADR 001: High Performance Core
- **Decision:** Use a high-performance systems language and a distributed caching layer.
- **Why:** Target throughput of 1M RPS requires minimal runtime overhead and a shared, distributed state for low-latency access.
- **Source:** High-scale system design principles.

## ADR 002: Project Lifecycle
- **Decision:** Mindset -> Architecture -> Build -> Visual Verification -> Security Hardening -> Optimization -> Operate.
- **Why:** Ensures a blueprint exists before coding and verification happens before hardening, regardless of the language used.
- **Source:** User Direction & Professional SaaS Playbook.
