# Rehydration — BRIDGEGEN-43001

ENTRY_ID=BRIDGEGEN-43001
SYSTEM_ID=666PFS-BRIDGEGEN-001
VERSION=1.0.0
STATE=VERIFIED_READY_V1.0.0

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read RUNTIME_CONTRACT.md.
4. Read DASHBOARD_CARD.md.
5. Read README.md.
6. Treat this child as a general binary repository bridge generator only.
7. Prefer direct complete binary repository transport when available.
8. Use bridge mode only when direct binary transport or required direct repository byte readback is genuinely blocked.
9. Require verified source identity, SHA-256, size, publication permission and unambiguous target.
10. Capture remote HEAD before work and recheck immediately before push.
11. No force push, no pointer mutation, no PFS-state mutation, no plugin mutation and no deployment from the bridge.
12. Require independent fresh remote readback and a machine-readable receipt before PASS.
13. Candidate/reference payloads may never be silently promoted to Current.
14. CHILD_AUTOLOAD remains forbidden.

CHILD_AUTOLOAD=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN
