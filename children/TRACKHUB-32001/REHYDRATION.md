# Rehydration

ENTRY_ID=TRACKHUB-32001
CLASSIFICATION=EXTERNAL_BACKUP_CHILD
STATE=SOURCE_CURRENT_VERIFIED_BACKUP_REFRESH_OPEN

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_BINDING.md.
3. Resolve external TDH Current first; never promote PFS backup over newer source Current.
4. Read CURRENT_STATE.md and compare SOURCE_CURRENT_VERSION to PFS_BACKUP_VERSION.
5. Use PFS backup only for backup/recovery purposes.
6. Mark refreshed backup VERIFIED only after actual binary import plus direct repository byte/hash/readback.
7. Never autoload or mutate external TDH runtime from PFS.

CHILD_AUTOLOAD=FORBIDDEN
FOREIGN_MUTATION=FORBIDDEN
