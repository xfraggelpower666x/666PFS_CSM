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
