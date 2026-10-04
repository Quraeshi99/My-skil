---
name: high-performance-system-optimization
description: "Master skill for building high-scale, secure systems. Sequence: Behavioral $ightarrow$ Architectural $ightarrow$ Security $ightarrow$ Implementation $ightarrow$ Optimization."
version: 1.3.0
author: Hermes Agent
license: MIT
metadata:
  tags: [system-design, performance, security, scalability, redis, cpp, aws, karpathy]
---

# High-Performance System Optimization Master-Skill

## 🛑 Pre-requisite: Behavioral Core
Regardless of the task, the agent MUST apply these Karpathy Principles:
1. **Think Before Coding:** State assumptions explicitly. Surface tradeoffs.
2. **Simplicity First:** No speculative features. If it can be 50 lines instead of 200, rewrite it.
3. **Surgical Changes:** Touch only what is necessary.
4. **Goal-Driven Execution:** Define success criteria $ightarrow$ Write test $ightarrow$ Implement $ightarrow$ Verify.

## 🏗 Step 1: Architectural Design (The Blueprint)
Refer to `docs/design-patterns/`:
1. **Requirement Analysis:** Define QPS, Latency, and Availability.
2. **Pattern Selection:** Choose the right patterns (e.g., Consistent Hashing for distributed caches).
3. **Capacity Planning:** Perform "Back-of-the-Envelope" estimations for RAM and Network.

## 🛡 Step 2: Security Hardening (The Shield)
Before coding, refer to `docs/security-standards.md`:
1. **Threat Modeling:** Identify potential attack vectors (DDoS, Prompt Injection, SSRF).
2. **Authentication & Authorization:** Implement modern standards (OAuth 2.1, Passkeys, Zero Trust).
3. **Input Validation:** Sanitize all inputs to prevent Injection and Overflow attacks.
4. **Supply Chain Check:** Verify dependencies and use SBOM (Software Bill of Materials).

## 🚀 Step 3: Implementation & Baseline
1. **Framework Selection:** Start with a productive tool (e.g., Fastify).
2. **Secure Implementation:** Apply the security guardrails defined in Step 2.
3. **Baseline Benchmark:** Establish a baseline RPS using `autocannon` or `k6`.

## ⚡ Step 4: Extreme Optimization (The 1M RPS Roadmap)
1. **Compute:** Move to **C++ (Drogon)** and **RapidJSON**. Maximize cores via Cluster Mode.
2. **Storage:** Shift Disk $ightarrow$ **RAM (Redis)** $ightarrow$ **Redis Clustering**.
3. **Algorithmic:** Replace $O(N)$ with $O(1)$. Use **UUID v4** for lock-free IDs.
4. **Infrastructure:** Use AWS C8gn (600Gbps NIC) and Network Load Balancers (NLB).

## Performance & Security Metrics
- **CPU:** Target 0% Idle during peak.
- **Network:** Monitor GB/s vs NIC limit.
- **Security:** Zero critical vulnerabilities in automated scans.
