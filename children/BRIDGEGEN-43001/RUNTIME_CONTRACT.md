# Runtime Contract — BRIDGEGEN-43001

STATUS=VERIFIED_READY_V1.0.0
MODE=PACKAGE_GENERATOR_AND_SAFE_LOCAL_EXECUTION_WORKFLOW

INPUTS:
- verified source payload path(s)
- expected SHA-256 per payload
- expected byte size per payload
- target repository
- target branch
- exact target path(s)
- publication authorization

OUTPUT PACKAGE:
- double-click BAT launcher
- PowerShell bridge
- target manifest
- expected hash/size manifest
- quick-start instructions
- verified payload files when allowed
- machine-readable remote readback receipt

EXECUTION_SEQUENCE:
PREFLIGHT -> CAPTURE_HEAD -> FRESH_CLONE -> COPY_AUTHORIZED_PATHS -> STAGE_EXACT_PATHS -> PREPUSH_HEAD_RECHECK -> PUSH_NO_FORCE -> FRESH_REMOTE_READBACK -> SIZE_HASH_IDENTITY_PASS -> RECEIPT

FAILURE_POLICY=BLOCK_OR_HOLD
UNEXPECTED_HEAD_MOVEMENT=CONFLICT_QUARANTINE
REMOTE_READBACK_FAILURE=PARTIAL
READY_WITHOUT_REMOTE_READBACK=FORBIDDEN
