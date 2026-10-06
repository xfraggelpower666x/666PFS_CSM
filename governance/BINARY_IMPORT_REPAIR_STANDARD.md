# 666PFS Binary Import Repair Standard

STATUS=ACTIVE
VERSION=1.0
DATE=2026-10-06
SYSTEM_ID=666PFS-CORE-001
NAMESPACE=666PFS

## Trigger condition

Use this workflow only when all of the following are true:

- TARGET_IS_PFS_CHILD=TRUE
- SOURCE_BINARY_EXISTS=TRUE
- SOURCE_BINARY_IDENTITY_VERIFIED=TRUE
- EXPECTED_SIZE_KNOWN=TRUE
- EXPECTED_HASH_KNOWN=TRUE
- REPO_BINARY_IMPORT_OR_READBACK_BLOCKED=TRUE
- PAYLOAD_PUBLICATION_ALLOWED=TRUE

If any condition is false or ambiguous, do not package or push automatically.

## Standard repair package

PFS shall prepare one complete offline repair package containing, when technically available and allowed:

- one double-click BAT launcher,
- one PowerShell binary bridge,
- target manifest,
- expected hash and size values,
- user-facing quick-start instructions,
- the already verified target payload files,
- receipt generation logic.

The user-facing workflow should be reduced to:

1. extract package,
2. double-click BAT,
3. wait for PASS,
4. run `666PFS UPDATE`.

## Bridge safety contract

Before write:
- verify exact local payload filename,
- verify byte size,
- verify SHA-256,
- read current remote HEAD,
- clone/read current target branch,
- verify no conflicting remote change before push.

Write:
- write only the intended child binary paths,
- no force push,
- no unrelated repository mutation,
- no pointer mutation,
- no PFS state/dashboard/registry mutation.

After write:
- perform a fresh remote clone or equivalent independent remote readback,
- verify file presence,
- verify byte size,
- verify byte identity using direct hash and/or exact Git blob identity,
- generate a machine-readable readback receipt.

Only after PASS may a subsequent native `666PFS UPDATE` promote the child to VERIFIED/READY and run:
Pre-Change-Backup → Audit → Re-Audit → Freeze → Pointer last.

## Hard fences

PRIVATE_PAYLOAD_PUBLIC_REPO_COPY=FORBIDDEN
FORBIDDEN_PAYLOAD_AUTO_PACKAGING=FORBIDDEN
PAYLOAD_WITHOUT_VERIFIED_HASH=FORBIDDEN
PAYLOAD_WITHOUT_VERIFIED_SIZE=FORBIDDEN
CROSS_SYSTEM_PAYLOAD_MERGE=FORBIDDEN
CHILD_AUTOLOAD=FORBIDDEN
FORCE_PUSH=FORBIDDEN
BRIDGE_POINTER_MUTATION=FORBIDDEN
BRIDGE_PFS_STATE_MUTATION=FORBIDDEN
READY_WITHOUT_REMOTE_READBACK=FORBIDDEN

## Failure handling

Any local mismatch, authentication failure, concurrency drift, push failure, remote readback failure, size mismatch, hash mismatch, or blob-identity mismatch must produce BLOCKED / PARTIAL.

Never claim successful binary migration unless remote readback directly proves it.

## Proven workflow reference

First proven use:
TARGET_CHILD=CYBERINTROHQ-39001
BRIDGE_COMMIT=e94e216f88256f4720940a11f893ecf20c875a0a
RESULT=VERIFIED_READY
