---
name: 666pfs-update
description: "Execute direct 666PFS UPDATE with instruction/recommendation intake, managed-plugin evolution checks, recovery, readback and pointer-last governance."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Execute governed repository-native 666PFS updates.

On direct:

666PFS UPDATE

use lifecycle:

VERIFY CURRENT HEAD / POINTER
→ PRE-CHANGE BACKUP
→ CHECK DIRECT USER INSTRUCTIONS
→ CHECK INBOUND RECOMMENDATIONS / HANDOFFS / PROPOSALS
→ CLASSIFY AND COMPATIBILITY-AUDIT PFS-RELEVANT DELTAS
→ CHECK ALL PFS-MANAGED PLUGINS FOR VERSION / RELEASE / FINGERPRINT / PARITY CHANGES
→ AUDIT
→ MINIMAL REPAIR / INTEGRATION
→ DIRECT READBACK
→ RE-AUDIT
→ PLUGIN IMPACT CHECK
→ COMPLETE PFS-OWNED PLUGIN EVOLUTION AND BACKUP IF REQUIRED
→ FREEZE STABLE MANAGED-PLUGIN SET WHEN APPLICABLE
→ INFORM LYVRA AND CLIC ONCE PER STABLE SET
→ REQUEST EACH SYSTEM'S OWN NATIVE BACKUP AUTHORIZATION
→ INFORM LYVRA THAT THE ROUND TARGETS PRIVATE-REPOSITORY PLUGIN-BACKUP INTEGRATION
→ EXECUTE ELIGIBLE BACKUPS ONLY AFTER MATCHING APPROVALS
→ DIRECT BACKUP READBACK / HASH / SIZE / ENTRY VERIFICATION
→ UPDATE BACKUP CHILDREN / RECEIPTS
→ FREEZE
→ POINTER LAST
→ READ-ONLY REHYDRATION

Implement verified durable PFS-relevant incoming instructions/recommendations in the same native update when safe and authorized.

Before any relevant mutation create a PFS-owned recovery/pre-change branch or equivalent verified recovery anchor.

Before any external/private plugin backup request, inspect all PFS-managed plugin backup states and finish PFS-owned plugin evolution. Do not request a foreign backup round from an unstable managed-plugin set.

Never write before checking current remote HEAD. Never overwrite newer valid remote state. Every write requires direct readback.

The pointer must be the LAST mutation.
NO_MUTATION_AFTER_POINTER=TRUE

If pointer write is blocked:
status = PARTIAL / POINTER_WRITE_BLOCKED

Resume from that exact lifecycle position on the next native update.

Read [plugin lifecycle](../../references/plugin-lifecycle.md) for native plugin-current inspection, impact, coordinated stable-set handling, parity and backup requirements.
