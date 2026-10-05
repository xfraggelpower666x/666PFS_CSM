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
4. Read `registry/README.md` and `registry/REHYDRATION_MATRIX.md`.
5. Read `dashboard/DASHBOARD_CONTRACT.md`, `dashboard/CHILD_MENU_CONTRACT.md`, `dashboard/CHILD_CARD_SCHEMA.md` and `dashboard/RENDERING_ORDER.md`.
6. Render the Whole-System dashboard and visual child menu from canonical repository state.
7. Resolve only the explicitly requested PFS target.

Historical material must never be promoted automatically.
