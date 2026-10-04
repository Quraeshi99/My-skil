# Security Hardening

## Multi-tenancy & Data Isolation
- **Strict Scoping:** Every single database query for tenant-owned data MUST include `organization_id` in the WHERE clause.
- **Verification:** Integration tests must prove that User A cannot access User B's data by changing IDs in the URL (IDOR Prevention).

## Infrastructure Email Security
- **Authentication:** Configure SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and DMARC (Domain-based Message Authentication, Reporting, and Conformance) to prevent email spoofing and ensure high deliverability.