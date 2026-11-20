# Rehydration

ENTRY_ID=UMIP-4001
STATE=READY_FOR_MANUAL_SELECTION
1. Read SYSTEM_IDENTITY.md and SOURCE_BINDING.md.
2. Read CURRENT_STATE.md and verify VERSION=1.11.1, PAYLOAD_MIGRATION=VERIFIED, REPOSITORY_READBACK=PASS.
3. Revalidate the named runtime ZIP against SHA256=c291d21f858ed645c454267fb23d115384690cd8b3a9a23d420251c1ab6446ca before allowing any functional payload use.
4. Treat Drive as HISTORY_BACKUP_RECOVERY only; no recovery promotion.
5. Do not autoload this child. Manual native selection remains subject to the PFS owner workflow.
6. No direct 666UMIP start/resume trigger is asserted here; retain action gates until those routes are verified.

CHILD_AUTOLOAD=FORBIDDEN
DIRECT_START_ROUTE=NOT_VERIFIED
DIRECT_RESUME_ROUTE=NOT_VERIFIED
