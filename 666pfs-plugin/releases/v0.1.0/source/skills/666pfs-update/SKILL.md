---
name: 666pfs-update
description: "Execute direct 666PFS UPDATE with recovery, foreign proposal intake, readback and pointer-last governance."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Execute governed repository-native 666PFS updates.

On direct:

666PFS UPDATE

use lifecycle:

PRE-CHANGE BACKUP
→ AUDIT
→ MINIMAL REPAIR / INTEGRATION
→ DIRECT READBACK
→ RE-AUDIT
→ FREEZE
→ POINTER LAST
→ READ-ONLY REHYDRATION

Before any relevant mutation:

create a PFS-owned recovery/pre-change branch or equivalent verified recovery anchor.

Never write before checking current remote HEAD.

Never overwrite newer valid remote state.

Every write requires direct readback.

The pointer must be the LAST mutation.

NO_MUTATION_AFTER_POINTER=TRUE

If pointer write is blocked:

status = PARTIAL / POINTER_WRITE_BLOCKED

Resume from that exact lifecycle position on the next native update.

---
