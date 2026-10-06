# LIGHT-35001 Repo-first Rehydration

1. Read `SYSTEM_IDENTITY.md`.
2. Read `SOURCE_BINDING.md`.
3. Resolve LIGHT ORCHESTRA source state from the bound WebRadio GitHub repository first.
4. Current verified source anchor is `4d6d7b322132af5b4a4589773e59cf1a3c41e0e2` on `feature/666-light-orchestra-v0.1.0`.
5. Resolve PFS child metadata from this `666PFS_CSM` repository on `main`.
6. Never use Google Drive as the current authority.
7. Drive records may be consulted only as preserved history, backup or recovery evidence when repository evidence is insufficient.
8. A newer valid repository state always supersedes older Drive history.
9. Never auto-restore an older Drive archive into GitHub.
10. Rehydrate source-only status with hardware validation still PENDING.
11. Rehydrate WRITE safety as fail-closed: LENZE and OC21W protocol writes remain blocked until real hardware validation.
12. Rehydrate merge safety as fail-closed while source and production remain diverged.
13. Any source-commit mismatch, identity conflict or missing evidence produces HOLD.
14. Child autoload remains forbidden.

READY means: origin repository identity intact, source binding resolvable, current source commit independently readable, and no authority conflict.

LIVE_AUTHORITY=ORIGIN_REPOSITORY
PFS_CHILD_ROLE=BACKUP_RECOVERY_REGISTRY_ONLY
PFS_CHILD_LIVE_AUTHORITY_OVERRIDE=FORBIDDEN
PFS_CHILD_RUNTIME_AUTHORITY=NONE
