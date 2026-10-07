# 666PFS Repo-first Rehydration

Primary runtime authority: GitHub repository `xfraggelpower666x/666PFS_CSM`, branch `main`.

Rehydration order:
1. Read `README.md` as the repository entry.
2. Read `governance/SYSTEM_IDENTITY.md`.
3. Read this rehydration contract.
4. Read `csm/COORDINATION_CONTRACT.md`.
5. Read `governance/BINARY_IMPORT_REPAIR_STANDARD.md`.
6. Read `governance/CHILD_IDENTITY_BINDING_STANDARD.md`.
7. Read `registry/CURRENT_POINTER.md` and resolve its declared canonical surfaces.
8. Read `registry/README.md`, `registry/REHYDRATION_MATRIX.md` and `registry/CURRENT_STATE.md`.
9. Read `handoff/LIVE_CIRCLE_CURRENT.md`.
10. Read the dashboard contracts and `dashboard/CURRENT_DASHBOARD.md`.
11. Read the child inventory and functional migration queue.
12. Resolve only the explicitly selected PFS target.
13. Use Google Drive only as preserved history, backup and recovery evidence when repository evidence is insufficient.

Validation rules:
- FOUND != VERIFIED
- SEARCH_RESULT != READBACK
- READ != REHYDRATED
- NEWER_VALID_EVOLUTION > OLDER_VALID_STATE
- unknown or conflicting evidence produces HOLD / CONFLICT_QUARANTINE instead of guessed state

A newer valid repository state takes precedence over older Drive history. Historical material is never promoted automatically. Child autoload and cross-system merging remain forbidden.


Child binding rule: an existing child must be verified by functional identity, scope, authority, and source/runtime evidence before reuse. Name or ID similarity alone is never sufficient.


## Mandatory LYVRA Freshness Gate for `666PFS UPDATE`

Every direct current-user trigger `666PFS UPDATE` MUST, before finalizing PFS state:
1. Rehydrate 666PFS from the current PFS repository pointer.
2. Read the current LYVRA→PFS handoff surfaces when present.
3. Read LYVRA's current origin-repository HEAD and the current published plugin release evidence relevant to PFS backup-child continuity.
4. Compare the newest valid LYVRA evidence with PFS-stored LYVRA handoff/backup metadata.
5. If LYVRA is newer, rebase only PFS metadata/backup targets to the newer verified LYVRA state; never overwrite newer LYVRA state with an older handoff.
6. Check the current LYVRA approval gate before any private-vault mutation.
7. If approval is absent, stale, or mismatched, set WRITE_BLOCKED and preserve the exact pending target versions/releases.
8. Never autoload LYVRA, mutate LYVRA, transfer LYVRA authority, or merge namespaces as part of this gate.
9. Complete PFS readback/freeze and publish the PFS pointer last.

LYVRA_FRESHNESS_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
LYVRA_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
LYVRA_ORIGIN_HEAD_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
LYVRA_PLUGIN_RELEASE_CHECK_WHEN_RELEVANT=REQUIRED
LYVRA_APPROVAL_CHECK_BEFORE_PRIVATE_WRITE=REQUIRED
LYVRA_AUTOLOAD=FORBIDDEN
LYVRA_MUTATION_BY_PFS_UPDATE=FORBIDDEN


## LYVRA Private Repository Authority Gate

Any 666PFS operation whose write target is a LYVRA-owned private repository MUST obtain a fresh, current, exact LYVRA approval before the write.
The approval must match the target repository/root, operation scope, and exact release/version set being backed up.
A stale, blanket, mismatched, missing, or already-consumed approval is invalid.
Without a matching approval, PFS MUST stop at WRITE_BLOCKED and may only preserve/read/update its own metadata about the pending operation.
PFS has no standing write authority over LYVRA private repositories.

LYVRA_PRIVATE_REPO_WRITE_REQUIRES_FRESH_APPROVAL=TRUE
LYVRA_PRIVATE_REPO_STANDING_PERMISSION=FALSE
LYVRA_APPROVAL_SCOPE_MATCH_REQUIRED=TRUE
LYVRA_APPROVAL_RELEASE_MATCH_REQUIRED=TRUE
LYVRA_APPROVAL_TARGET_MATCH_REQUIRED=TRUE
MISSING_OR_MISMATCHED_LYVRA_APPROVAL=WRITE_BLOCKED


## LYVRA Plugin Source Authority Hierarchy
LYVRA_PLUGIN_SOURCE_OF_TRUTH=ORIGIN_REPOSITORY
LYVRA_PLUGIN_SOURCE_ROLE=PRIMARY_LIVE_RELEASE_AUTHORITY
LYVRA_PLUGIN_BACKUP_ROLE=BACKUP_RECOVERY_ONLY
LYVRA_PLUGIN_BACKUP_CAN_OVERRIDE_SOURCE=FALSE
LYVRAPLUGIN_37001_ROLE=BACKUP_RECOVERY_REGISTRY_ONLY


## LYVRA Approval Request Channel
LYVRA_APPROVAL_REQUEST_AUTHORITY=LYVRA_LIVE_REPOSITORY
LYVRA_APPROVAL_REQUEST_ORIGIN=PFS_OUTBOUND_REQUEST
LYVRA_PRIVATE_REPOSITORY_ROLE=PLUGIN_BACKUP_STORAGE_ONLY
LYVRA_PRIVATE_REPOSITORY_IS_APPROVAL_CHANNEL=FALSE
PFS_MAY_SELF_APPROVE_LYVRA_WRITE=FALSE
PFS_MAY_MUTATE_LYVRA_LIVE_REPOSITORY_DURING_PFS_UPDATE=FALSE
APPROVAL_MISMATCH_ACTION=CREATE_OUTBOUND_REQUEST_AND_SET_APPROVAL_REQUESTED_WRITE_BLOCKED


## Symmetric Foreign Freshness Gate — LYVRA + CLIC
LYVRA_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
LYVRA_ORIGIN_FRESHNESS_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
CLIC_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
CLIC_AUTHORITY_FRESHNESS_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
CLIC_OUTBOX_TO_PFS_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
CLIC_CONTINUITY_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
FOREIGN_AUTOLOAD=FORBIDDEN
FOREIGN_MUTATION=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN
NEWER_VALID_REMOTE_STATE_WINS=TRUE
