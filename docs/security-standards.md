# Modern Security Standards (October 2026)

This document defines the security guardrails that must be applied to every high-performance system to prevent catastrophic failures.

## 🛡 1. Zero Trust Architecture
- **Assumption:** Assume the network is already compromised.
- **Principle:** Every request, even internal, must be authenticated and authorized.
- **Implementation:** Use mTLS (Mutual TLS) for service-to-service communication.

## 🔑 2. Authentication & Identity
- **Modern Auth:** Deprecate legacy passwords. Move to **Passkeys (WebAuthn)** and **OAuth 2.1**.
- **JWT Hardening:** 
  - Use strong signing algorithms (EdDSA/RS256).
  - Short-lived Access Tokens + Rotated Refresh Tokens.
  - Implement strict claim validation to prevent "Claim Confusion" attacks.

## 🚧 3. Application Layer Defense
- **Input Validation:** 
  - Use strict schema validation (e.g., Zod, JSON Schema).
  - Sanitize all inputs to prevent SQLi, XSS, and Command Injection.
- **Rate Limiting:** 
  - Implement multi-layered limiting: Global (NLB) $ightarrow$ Per-IP $ightarrow$ Per-User.
  - Use a sliding window counter in Redis to prevent "Burst" attacks.
- **Request Smuggling:** Ensure strict HTTP parsing to prevent Request Normalization/Smuggling attacks.

## ☁️ 4. Infrastructure & Cloud Security
- **Least Privilege:** Use IAM roles with the absolute minimum permissions needed.
- **Network Isolation:** Place databases and internal services in private subnets.
- **K8s Hardening:** 
  - Use Pod Security Admissions.
  - Prevent container escapes by running non-root users.
  - Network Policies to restrict inter-pod traffic.

## 📦 5. Supply Chain & Dependency Security
- **SCA (Software Composition Analysis):** Continuously scan dependencies for known CVEs.
- **Pinned Versions:** Never use `latest` tags; use specific hashes (sha256) for images and packages.
- **SBOM:** Maintain a Software Bill of Materials for all production deployments.

## 🕵️ 6. Monitoring & Response
- **Observability:** Log all security-critical events (Auth failures, privilege escalations).
- **Real-time Alerting:** Set up alerts for abnormal traffic spikes (potential DDoS) or repeated 403/401 errors.
- **Automatic Revocation:** Ability to revoke all sessions for a compromised user instantly.
