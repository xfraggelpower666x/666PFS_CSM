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
