---
name: 666pfs-dashboard
description: "Render requested evidence-first PFS/CSM dashboard from verified Current without activation or mutation."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Render an internal evidence-first PFS/CSM dashboard.

Dashboard should show:

PFS identity
repository authority
current HEAD
pointer state
rehydration state
daemon state
CSM state
child foreground state
scope map state
temporal LiveCircle state
open work
return anchor
locks/conflicts
pending readbacks
backup gates
LYVRA handoff status
CLIC handoff status
proposal intake
write state
pointer-last state

Presentation must never create authority.

Dashboard state must be derived from verified current evidence.

---
