# Rehydration — CURSORFRAME-42001

ENTRY_ID=CURSORFRAME-42001
SYSTEM_ID=666PFS-CURSORFRAME-001
VERSION=0.3.0
STATE=REGISTERED_PARTIAL_BINARY_IMPORT_PENDING

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read DASHBOARD_CARD.md.
4. Read README.md.
5. Treat this child as the general offline cursor-generator framework only.
6. Do not bind or merge it with CURSORGEN-41001 or CURES-16001.
7. Preserve offline-only architecture: no Cloudflare, no account, no telemetry, no server dependency.
8. Preserve non-destructive project handling, CUR/ANI processing, Windows activation, backup, restore and readback design.
9. Keep READY promotion blocked until repository binary import and remote byte readback pass.
10. CHILD_AUTOLOAD remains forbidden.

CHILD_AUTOLOAD=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN
