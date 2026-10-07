---
name: 666pfs-foreign-handoff-intake
description: "Inspect LYVRA and CLIC handoffs, instructions, recommendations and proposals read-only during every PFS UPDATE."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Read relevant LYVRA and CLIC handoff/outbox carriers on every 666PFS UPDATE.

This skill is READ-ONLY toward foreign systems.

Required checks every PFS update:

LYVRA:
- authority freshness
- relevant handoffs
- plugin/runtime fingerprint when applicable
- backup approval
- improvement proposals
- architecture proposals
- learning proposals
- instructions/recommendations explicitly addressed to PFS
- private-repository backup integration requirements

CLIC:
- active authority branch/head
- 666CLIC_NATIVE_RUNTIME/outbox/666PFS/*
- continuity/repo-to-repo handoffs
- plugin freshness
- native backup authorization when relevant
- improvement proposals
- architecture proposals
- learning proposals
- instructions/recommendations explicitly addressed to PFS

Rules:

FOREIGN_PROPOSAL_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
FOREIGN_RECOMMENDATION_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
FOREIGN_INSTRUCTION_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
LYVRA_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
CLIC_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED

Classify all incoming items:
VERIFIZIERT
ABGELEITET
VORGESCHLAGEN
OFFEN
BLOCKIERT

Verified durable PFS-relevant items may be adopted only after PFS compatibility audit. Foreign proposal presence NEVER equals adoption or foreign authority.

PFS_NATIVE_ADOPTION_REQUIRES_COMPATIBILITY_AUDIT=TRUE
FOREIGN_PROPOSAL_IS_NOT_AUTHORITY=TRUE

FOREIGN_AUTOLOAD=FORBIDDEN
FOREIGN_MUTATION=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN
