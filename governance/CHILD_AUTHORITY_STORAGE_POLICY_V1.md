# PFS Child Authority & Storage Policy V1.0

SYSTEM_ID=666PFS-CORE-001
STATUS=ACTIVE
POLICY_VERSION=1.0
SCOPE=PFS_NATIVE_CHILD_GOVERNANCE
APPLIES_TO=666PFS_UPDATE|666PFS_NEW_CHILD|CHILD_LIFECYCLE|CSM|REHYDRATION|VISUAL_MENU

## Evidence-first classification
Before any creation, update or reclassification independently verify functional identity, live authority, source/runtime ownership, intended execution, existing child identity and permitted storage target. System size and names are insufficient evidence.

### EXTERNAL_BACKUP_CHILD
Use for any independently governed live system operating in its own repository, Drive runtime, or other external authority. PFS stores only source-bound backup/recovery/metadata and verified artifacts. Native owner alone governs live runtime, deployment, source changes and approvals.
PFS_ROLE=BACKUP_RECOVERY_ONLY
PFS_RUNTIME_AUTHORITY=NONE
PFS_DEPLOY_AUTHORITY=NONE
PFS_SOURCE_MUTATION=FORBIDDEN
SOURCE_CURRENT_OVERRIDES_PFS_BACKUP=TRUE

### PFS_LOCAL_LIVE_CHILD
Use only where verified functional identity and explicit native authority make 666PFS the real owner of a local production. Maintain PFS-controlled CURRENT, source/runtime metadata, rollback and a tested recovery route. A ZIP may be attached as an independent backup, never presumed to be an active runtime.
PFS_ROLE=LOCAL_LIVE
PFS_NATIVE_AUTHORITY=REQUIRED_AND_VERIFIED
CURRENT_CARRIER=REQUIRED
RUNTIME_PASS=REQUIRES_ACTUAL_TEST

### SYSTEM_ARTIFACT_CHILD
Use for a local deliverable primarily stored as a self-contained ZIP or system package, not for an externally governed live system merely because a ZIP exists.
PFS_ROLE=SYSTEM_ARTIFACT
ARTIFACT=ZIP_OR_VERIFIED_SYSTEM_PACKAGE
MANIFEST=REQUIRED
SHA256=REQUIRED
SIZE_BYTES=REQUIRED
ZIP_ENTRIES_AND_CRC=REQUIRED_WHEN_ZIP
DIRECT_REMOTE_BYTE_READBACK=REQUIRED
RESTORE_TEST=SEPARATELY_REQUIRED_FOR_RECOVERY_READY
RUNTIME_AUTHORITY=NOT_INFERRED_FROM_ZIP

## Trigger decisions
666PFS UPDATE: Determine exact current class first; update only the PFS-owned area. External live evolution implies refreshed PFS backup target, not external live mutation.
666PFS NEW CHILD: Classify before allocating an identity. For externally owned systems create a backup-only child. For proven PFS-local production choose LOCAL_LIVE or SYSTEM_ARTIFACT based on actual operating model. Do not infer permissions from request wording alone.
UNKNOWN_OR_CONFLICTING_AUTHORITY=HOLD
AMBIGUOUS_FUNCTIONAL_IDENTITY=HOLD_AND_AUDIT
EXISTING_CHILD_BULK_RECLASSIFICATION=FORBIDDEN
CHILD_AUTOLOAD=FORBIDDEN
FOREIGN_AUTOLOAD=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN
NEW_CHILD_MUST_BE_EXPLICITLY_AUTHORIZED=TRUE

## Write lifecycle
Verify newest HEAD/pointer/lock/queue and allowlist. Create pre-change recovery anchor. Independently read source and target. Apply minimal PFS-only change. Perform direct readback, registry/dashboard reconciliation, freeze, pointer LAST. After pointer no mutation. Never assert binary/recovery PASS without actual bytes, hash and archive/restore checks.

## Display
Child menu and card must display CLASSIFICATION, LIVE_OWNER, PFS_ROLE, STORAGE_MODE, SOURCE_CURRENT, RESTORE_STATUS and VERIFIED_EVIDENCE. Unknown becomes neutral HOLD, never a guessed LIVE class.
