# High-Performance & Secure System Engineering Framework

This project is a comprehensive master-skill for building world-class, high-scale, and hardened systems. It integrates behavioral discipline, architectural depth, extreme performance optimization, and modern security standards.

## 🛠 The Engineering Lifecycle (The Golden Path)
To build a system that handles 1M+ RPS and remains secure against modern threats, we follow this strict sequence:

### Phase 1: Behavioral Alignment (The Mindset)
Apply **Karpathy Guidelines**: Think before coding, prioritize simplicity, make surgical changes, and define verifiable goals.

### Phase 2: Architectural Design (The Blueprint)
Leverage the **System Design Library**: Define QPS/Latency targets, select the right patterns (Consistent Hashing, Rate Limiting), and perform capacity planning.

### Phase 3: Security Hardening (The Shield)
Before implementation, define the **Security Guardrails**:
- **Zero Trust Architecture:** Never trust, always verify.
- **Defense in Depth:** Layered security from the Network to the Application layer.
- **Secure-by-Design:** Implement modern auth, input validation, and supply-chain security.

### Phase 4: Baseline Implementation
Build the functional system using the selected architecture and security standards.

### Phase 5: Extreme Optimization (The 1M RPS Journey)
Systematically remove bottlenecks:
- **Compute:** Express $ightarrow$ Fastify $ightarrow$ C++ (Drogon).
- **Scaling:** Single-threaded $ightarrow$ Cluster Mode $ightarrow$ Horizontal Scaling.
- **Storage:** Disk $ightarrow$ RAM (Redis) $ightarrow$ Redis Clustering.
- **Network:** 10Gbps $ightarrow$ 600Gbps NICs (AWS C8gn).

## 📂 Project Structure
- `SKILL.md`: The Master SOP for AI Agents.
- `README.md`: High-level roadmap.
- `docs/governance.md`: Behavioral standards (Karpathy).
- `docs/architecture.md`: High-level system design principles.
- `docs/design-patterns/`: Library of 28+ system design blueprints.
- `docs/security-standards.md`: Modern security guidelines (October 2026).
- `docs/benchmarks.md`: Real-world performance data.
- `docs/optimizations.md`: Deep-dive scaling techniques.

## ⚖️ The Philosophy
Performance without security is a liability; security without performance is a bottleneck. We build systems that are **Fast, Simple, and Unstoppable**.
