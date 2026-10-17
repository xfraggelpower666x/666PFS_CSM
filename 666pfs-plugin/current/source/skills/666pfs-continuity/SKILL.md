---
name: 666pfs-continuity
description: "Continue direct 666PFS WEITER from the verified current return anchor without restarting."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Handle direct:

666PFS WEITER

Rehydrate from current pointer and continue the last verified open work.

Required concepts:

CURRENT_WORK
COMPLETED
OPEN
INTERRUPTIONS
OBLIGATIONS
RETURN_ANCHOR
NEXT_MEANINGFUL_STEP
BLOCKERS
EXTERNAL_WAITING_STATES

If new user information interrupts active work:

ABSORB_NEW_INFORMATION=TRUE
PROCESS_CAUSALLY_RELATED_EFFECTS=TRUE
PRESERVE_INTERRUPTED_RETURN_ANCHOR=TRUE
RESUME_INTERRUPTED_WORK=TRUE
NO_UNNECESSARY_RESTART=TRUE

Never restart a workflow simply because a new chat/turn occurred.

---

## Persistent interruptions and return
For every interruption: preserve active task, scoped task stack, verified phase, completed/open obligations, interruption cause, current HEAD/pointer, rollback anchor and next meaningful step. Absorb new relevant information, classify dependent changes, then resume the interrupted task from its validated return anchor; do not restart, silently drop it, or automatically mutate. For NEW/NEXT CHAT, use verified same-lineage handoff only, never globally latest-by-time. Pending auth/lock/conflict stays blocked. Rehydrate fresh repository Current first; fresh-host acceptance remains independent. Patterns from CLIC/STREAM/LYVRA are evidence only, not foreign authority.

## Persistent task carrier
On every continuation resolve governance/PFS_TASK_CONTINUITY_CONTRACT.md and handoff/PFS_TASK_CONTINUITY_CURRENT.json from verified latest PFS Current. Use scoped task stack and currentness; process causal additions then resume prior task from last verified return anchor. No automatic resumed write through an unresolved blocker. NEW/NEXT CHAT requires lineage-verified handoff and independent fresh-host acceptance.

## Visual continuation output
After resumed work, show evidence-based outcome, open obligations, exact return anchor and working host-supported contextual choices; if no clickable actions are available, print exact copyable PFS commands. Resolve governance/PFS_NATIVE_VISUAL_CONTINUATION_CONTRACT_V1.md. This does not grant write permission.
