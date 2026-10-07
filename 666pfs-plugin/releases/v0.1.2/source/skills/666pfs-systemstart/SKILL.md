---
name: 666pfs-systemstart
description: "Rehydrate existing 666PFS only on direct 666PFS SYSTEMSTART and render its evidence dashboard."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Rehydrate 666PFS from canonical GitHub current.

On direct:

666PFS SYSTEMSTART

perform:

1. Verify direct trigger.
2. Verify repository/connector availability.
3. Verify read/write capabilities.
4. Verify allowlist.
5. Verify lock / queue state when relevant.
6. Read current repository HEAD.
7. Read registry/CURRENT_POINTER.md.
8. Verify system identity.
9. Read governance/REHYDRATION_CONTRACT.md.
10. Follow the current PFS-native rehydration order.
11. Load current registry/state.
12. Load 666CSM coordination state.
13. Load PFS daemon/lifecircle state.
14. Load Scope Map.
15. Load Temporal LiveCircle.
16. Reconstruct current open work and return anchor.
17. Check LYVRA and CLIC handoff/freshness surfaces read-only.
18. Render evidence-first PFS dashboard.

Never autoload a child.

SELECTED_CHILD=NONE unless direct current user context selects a child.

---

Read [plugin lifecycle](../../references/plugin-lifecycle.md) for native plugin-current inspection, impact, parity and backup requirements.
