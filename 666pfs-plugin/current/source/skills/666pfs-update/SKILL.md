---
name: 666pfs-update
description: "Execute direct 666PFS UPDATE with recovery, managed-plugin preflight, foreign proposal intake, readback and pointer-last governance."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Execute governed repository-native 666PFS updates.

On direct:

666PFS UPDATE

use lifecycle:

VERIFY CURRENT HEAD / POINTER
→ PRE-CHANGE BACKUP
→ AUDIT
→ MANAGED PLUGIN PREFLIGHT
→ MINIMAL REPAIR / INTEGRATION
→ DIRECT READBACK
→ RE-AUDIT
→ PLUGIN IMPACT CHECK
→ COMPLETE PFS-OWNED PLUGIN EVOLUTION AND BACKUP IF REQUIRED
→ FREEZE STABLE MANAGED-PLUGIN BACKUP ROUND WHEN APPLICABLE
→ INFORM LYVRA AND CLIC ONCE PER STABLE ROUND
→ FREEZE
→ POINTER LAST
→ READ-ONLY REHYDRATION

Before any relevant mutation create a PFS-owned recovery/pre-change branch or equivalent verified recovery anchor.

Before any external/private plugin backup notice, inspect all PFS-managed plugin backup states. Do not notify foreign systems while a PFS-owned plugin update or parity repair is still open.

Never write before checking current remote HEAD. Never overwrite newer valid remote state. Every write requires direct readback.

The pointer must be the LAST mutation.
NO_MUTATION_AFTER_POINTER=TRUE

If pointer write is blocked:
status = PARTIAL / POINTER_WRITE_BLOCKED

Resume from that exact lifecycle position on the next native update.

Read [plugin lifecycle](../../references/plugin-lifecycle.md) for native plugin-current inspection, impact, parity, coordinated round and backup requirements.
