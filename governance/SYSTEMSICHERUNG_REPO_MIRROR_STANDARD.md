# 666PFS Systemsicherung Repo Mirror Standard

STATUS=ACTIVE
VERSION=1.1
DATE=2026-10-06
SYSTEM_ID=666PFS-CORE-001
NAMESPACE=666PFS

## Required workflow
AUDIT_PRE=REQUIRED
REPAIR=REQUIRED_WHEN_FINDINGS_EXIST
IMPROVEMENT=REQUIRED_WHEN_SAFE_AND_ADDITIVE
EVOLUTION=REQUIRED_WHEN_USER_REQUESTED_OR_GOVERNANCE_GAP_FOUND
AUDIT_FINAL=REQUIRED
REPAIR_FINAL=REQUIRED_WHEN_FINAL_AUDIT_FINDINGS_EXIST
FREEZE=REQUIRED
SYSTEMSICHERUNG_ZIP=REQUIRED
REPO_RECOVERY_MIRROR=REQUIRED

## Repository placement
CORE_BACKUP_ROOT=recovery/666PFS-CORE-001
CHILD_BACKUP_ROOT_TEMPLATE=children/<CHILD_ID>/recovery
EXTERNAL_NATIVE_REPO_BACKUP_ROOT=USE_NATIVE_REPOSITORY_RECOVERY_PATH
PROJECT_NAME_IS_NOT_AUTHORITY=TRUE

## Mirror contract
1. create a downloadable ZIP for the user.
2. calculate SHA-256 and exact byte size.
3. mirror the ZIP into the responsible repository recovery directory when writes are permitted.
4. for one operation affecting multiple PFS scopes, mirror the same consolidated ZIP into the core recovery root and each affected child recovery directory.
5. external native systems remain in their own native repository.
6. write a manifest beside the ZIP.
7. perform repository metadata or byte identity readback where technically available.
8. keep the last VERIFIED_READY version promoted while a newer candidate still requires readback.
9. publish Current Pointer last for PFS-native updates.

## Preservation
PRESERVE_NATIVE_IDENTITY=TRUE
PRESERVE_NATIVE_EXECUTION_AUTHORITY=TRUE
NO_CROSS_SYSTEM_MERGE=TRUE
NO_FORCE_PUSH=TRUE
NO_DOWNGRADE=TRUE
OLDER_BACKUPS=HISTORY_ONLY
NEWER_VALID_STATE_WINS=TRUE
CHILD_AUTOLOAD=FORBIDDEN

## Failure states
REPO_WRITE_UNAVAILABLE=WRITE_BLOCKED
BYTE_READBACK_UNAVAILABLE=READBACK_PENDING
CONCURRENT_WRITER=PARTIAL
HASH_MISMATCH=CONFLICT_QUARANTINE
