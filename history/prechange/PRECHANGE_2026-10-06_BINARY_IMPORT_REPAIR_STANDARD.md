# 666PFS Pre-Change Backup — Binary Import Repair Standard

DATE=2026-10-06
SYSTEM_ID=666PFS-CORE-001
NAMESPACE=666PFS
PRECHANGE_HEAD=0f08bf155f6f2b8a2c8f9976e07b4e04773c4675
PREVIOUS_POINTER_BLOB=bc3517a4a803059a27d26f38ed475000c8461552

## User-confirmed durable delta
When a PFS child has verified binary source artifacts but repository binary import/readback is blocked by the available connector path, PFS shall use the proven COMPLETE REPAIR PACKAGE workflow:
- package a double-click BAT launcher,
- package a PowerShell binary bridge,
- include manifests/checks and, when available and allowed, the already verified payload files,
- verify local size/hash before write,
- verify remote HEAD before push,
- abort on concurrency drift,
- push only the intended binary paths,
- perform fresh remote readback,
- verify byte identity/hash,
- produce a readback receipt,
- finish PFS state/freeze/pointer only after a subsequent 666PFS UPDATE.

PRIVATE_OR_FORBIDDEN_PAYLOAD_AUTO_PACKAGING=FORBIDDEN
POINTER_MUTATION_BY_BRIDGE=FORBIDDEN
PFS_STATE_MUTATION_BY_BRIDGE=FORBIDDEN
CHILD_AUTOLOAD=FORBIDDEN
