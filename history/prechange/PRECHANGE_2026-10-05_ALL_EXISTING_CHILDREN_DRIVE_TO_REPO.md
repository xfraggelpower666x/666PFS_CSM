# 666PFS Pre-Change Backup — All Existing Children Drive-to-Repo Migration

DATE=2026-10-05
SYSTEM_ID=666PFS-CORE-001
NAMESPACE=666PFS
BRANCH=main
PRECHANGE_HEAD=5781721cd6faa1e5ff66753e484a771eada3a54c

## User-prioritized migration order
1. Migrate all existing PFS children from verified Drive legacy evidence to the GitHub repository.
2. Verify and rehydrate every migrated child.
3. Keep Drive as history / backup / recovery only.
4. Defer creation of any genuinely new child until existing-child migration is complete.

## Direct Drive evidence
- Central legacy child root was directly listed.
- Multiple registered child folders and release/freeze packages were found.
- Additional legacy/recovery candidates not yet normalized in the repo inventory were found and must be reconciled rather than silently promoted.
- Existing Drive folder `LYVRA Plugin Backup` was found; therefore it is not to be treated as an invented new child.

## Governance
CHILD_AUTOLOAD=FORBIDDEN
FOREIGN_AUTOLOAD=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN
LYVRA_AUTHORITY_UNCHANGED=TRUE
DRIVE_ROLE_DURING_MIGRATION=RECOVERY_SOURCE_ONLY
TARGET_AUTHORITY=GITHUB_REPOSITORY
