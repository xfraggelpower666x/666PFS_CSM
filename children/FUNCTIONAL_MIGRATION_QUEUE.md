# Functional Child Migration Queue

PRIORITY=ALL_EXISTING_CHILDREN_TO_REPO_BEFORE_NEW_CHILD_CREATION
DATE=2026-10-05

## Active migration progress
REGISTERED_ACTIVE=23
READY_OR_VERIFIED_BOUND=19
NEWLY_MIGRATED_RUNTIME_PAYLOADS_THIS_UPDATE=16
PREEXISTING_READY_OR_BOUND=3

## Remaining active work
- PHG-3001 — source v2.13.0 VERIFIED; repeated h2 binary-transfer failure — WRITE_BLOCKED_TRANSFER
- CTIO-7001 — SOURCE_DISCOVERY_OPEN
- DISCORD-14001 — source package VERIFIED (~98 MB) — LARGE_BINARY_TRANSFER_PENDING
- CURES-16001 — v0.1.0 runtime plus v0.1.1 semantic/purpose authority — RECONCILIATION_REQUIRED

## Preservation / backup work
- SOUNDWAVE-34001 — v1.18.0 evidence found — payload migration pending
- LIGHT-35001 — repo metadata verified; runtime not independently verified
- WEBLYVRA-36001 — 14.1 MB backup package found — payload migration pending
- LYVRAPLUGIN-37001 — existing child identity recovered; metadata migrated; binaries/refresh pending

## Historical / reconciliation work
- LYVRA-DOLMETSCHER-13001, UDF-19001, ASMIF-20001, ARCHEON-20001, GIFT-21001, CGF-31001 remain re-audit/quarantine as applicable.
- URLMD-15001 and ISQF-24001 require registry reconciliation.

## Rules
SOURCE_FOUND != PAYLOAD_MIGRATED
PAYLOAD_MIGRATED != READY
READY requires direct repository readback.
NO_GENUINELY_NEW_CHILD_CREATION_UNTIL_EXISTING_MIGRATION_COMPLETE=TRUE
