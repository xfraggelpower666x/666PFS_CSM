---
name: 666pfs-foreign-handoff-intake
description: "Inspect LYVRA and CLIC handoffs and proposals read-only during each PFS UPDATE or requested intake audit."
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

CLIC:
- active authority branch/head
- 666CLIC_NATIVE_RUNTIME/outbox/666PFS/*
- continuity/repo-to-repo handoffs
- plugin freshness
- native backup authorization when relevant
- improvement proposals
- architecture proposals
- learning proposals

Rules:

FOREIGN_PROPOSAL_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
LYVRA_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED
CLIC_HANDOFF_CHECK_ON_EVERY_PFS_UPDATE=REQUIRED

Foreign proposal presence NEVER equals adoption.

Every proposal must be classified:

VERIFIZIERT
ABGELEITET
VORGESCHLAGEN
OFFEN
BLOCKIERT

PFS_NATIVE_ADOPTION_REQUIRES_COMPATIBILITY_AUDIT=TRUE

FOREIGN_PROPOSAL_IS_NOT_AUTHORITY=TRUE

FOREIGN_AUTOLOAD=FORBIDDEN
FOREIGN_MUTATION=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN

---
