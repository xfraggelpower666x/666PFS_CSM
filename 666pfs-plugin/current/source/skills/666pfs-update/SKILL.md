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

## Child Authority & Storage preflight
During UPDATE, before child changes, rehydrate governance/CHILD_AUTHORITY_STORAGE_POLICY_V1.md and classify the precise target and source-first backup hierarchy. An external live system may only be updated as PFS backup/recovery metadata; local PFS-owned work may update LIVE current or verified artifact according to class. Preserve interrupted task stack and return anchor when a user's new relevant detail arrives, then return to original work after processing. Do not treat new information as cancellation.

## Three checks then learning
Apply governance/PFS_LEARNING_BY_DOING_CONTRACT.md: max three repeat probes per unchanged causal failure. Change method or HOLD, record evidence, preserve task continuation. Does not bypass locks, native approvals, readback or pointer-last requirements.

## Mandatory visual closure and original task resumption
Resolve governance/PFS_NATIVE_VISUAL_CONTINUATION_CONTRACT_V1.md. After readback/pointer-last, display actual status, evidence, blockers, exact original task return anchor and working next-action choices. New user feedback is processed causally, then prior task resumes unless blocked. No fake buttons, no unnecessary same-failure checks.
