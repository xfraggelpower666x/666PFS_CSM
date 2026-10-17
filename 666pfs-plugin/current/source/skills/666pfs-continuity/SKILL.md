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
