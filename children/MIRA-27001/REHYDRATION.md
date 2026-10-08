# Rehydration

ENTRY_ID=MIRA-27001
SYSTEM_ID=666MIRA-CORE-001
VERSION=1.0.17
STATE=READY_FROM_REPOSITORY_CURRENT

1. Read SYSTEM_IDENTITY.md.
2. Read CURRENT_STATE.md.
3. Read SOURCE_BINDING.md.
4. Resolve the repository runtime payload at the declared RUNTIME_PATH.
5. Read stored provenance from provenance/SHA256SUMS.txt.
6. Preserve MIRA NORMAL as the base behavior and presets as additive only.
7. Preserve the SENTENCE alias binding already contained in v1.0.17.
8. Treat Google Drive as history / backup / recovery only.
9. Do not autoload MIRA. Rehydrate only when MIRA is explicitly selected or invoked under valid governance.

CHILD_AUTOLOAD=FORBIDDEN
FOREIGN_SYSTEM_AUTOACTIVATION=FORBIDDEN
REPOSITORY_CURRENT_WINS=TRUE
