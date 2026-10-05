# 666PFS_CSM

Repository-native control plane for 666PFS and its internal 666CSM service.

## Runtime model
- System: `666PFS-CORE-001`
- Namespace: `666PFS`
- Core baseline: `2.7.3`
- Internal service: `666CSM`
- Primary runtime control surface: this GitHub repository
- Legacy Drive state: history, backup and recovery evidence
- Child autoload: forbidden
- Foreign-system autoload: forbidden

## Rehydration entry
1. Read `governance/SYSTEM_IDENTITY.md`.
2. Read `governance/REHYDRATION_CONTRACT.md`.
3. Read `csm/COORDINATION_CONTRACT.md`.
4. Read `registry/CURRENT_POINTER.md`.
5. Read `registry/README.md`, `registry/REHYDRATION_MATRIX.md` and `registry/CURRENT_STATE.md`.
6. Read `handoff/LIVE_CIRCLE_CURRENT.md`.
7. Read `dashboard/DASHBOARD_CONTRACT.md`, `dashboard/CHILD_MENU_CONTRACT.md`, `dashboard/CHILD_CARD_SCHEMA.md`, `dashboard/RENDERING_ORDER.md` and `dashboard/CURRENT_DASHBOARD.md`.
8. Read `children/CHILD_INVENTORY.md` and `children/FUNCTIONAL_MIGRATION_QUEUE.md`.
9. Render the Whole-System dashboard and visual child menu from canonical repository state.
10. Resolve only the explicitly requested PFS target.

Historical material must never be promoted automatically. A newer valid repository state takes precedence over older Drive or handoff history.
