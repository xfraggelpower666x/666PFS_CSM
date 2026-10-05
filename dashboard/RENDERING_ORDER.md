# Dashboard Rendering Order

Render order for SYSTEMSTART and UPDATE summaries:
1. Whole-System status header
2. Core / authority / repository status
3. 666CSM coordination status
4. registry / lock / queue / recovery state
5. current work and blockers
6. visual child menu
7. selected child detail only when explicitly selected

The renderer reads canonical repository files and never creates independent authority.
