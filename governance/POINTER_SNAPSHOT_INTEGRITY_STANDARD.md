# 666PFS Pointer / Snapshot Integrity Standard

STATUS=ACTIVE
VERSION=1.0
DATE=2026-11-14
SYSTEM_ID=666PFS-CORE-001

## Purpose
Prevent pointer-last publication from carrying stale internal blob references or stale cross-surface counters.

## Required pre-freeze gate
Before freeze and before Current Pointer publication:
1. Read fresh branch HEAD.
2. Read Current State, Child Inventory, Migration Queue, Dashboard and Live Circle from that HEAD.
3. Verify semantic counters against the authoritative Child Inventory and explicit ready/bound evidence.
4. Verify that every pointer-carried blob reference equals the fresh blob SHA of its target file.
5. Verify no newer commit appeared during the gate.
6. If drift exists, repair minimally and repeat readback.
7. Publish Current Pointer last.
8. Perform final HEAD + pointer readback.
9. No mutation after pointer in the same update.

## Status rules
POINTER_LAST_WITH_STALE_REFERENCES=FAIL
COUNTER_DRIFT=FAIL
CONCURRENT_HEAD_DRIFT=PARTIAL
POINTER_TARGET_BLOB_PARITY=REQUIRED
NO_DOWNGRADE=TRUE
NO_CROSS_SYSTEM_MERGE=TRUE
CHILD_AUTOLOAD=FORBIDDEN
