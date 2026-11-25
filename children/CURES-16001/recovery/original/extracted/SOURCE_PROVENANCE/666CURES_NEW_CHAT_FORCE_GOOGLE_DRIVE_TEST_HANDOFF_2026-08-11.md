# 666CURES / 666PFS / 666CSM — NEW CHAT CONTINUATION HANDOFF
## FORCE GOOGLE DRIVE CONNECTOR READ / WRITE / READBACK TEST

HANDOFF_ID=666PFS-666CURES-NEW-CHAT-RECOVERY-20260811-001
VERSION=1.0.0
DATE=2026-08-11
TARGET=NEW_CHAT
PARENT_NAMESPACE=666PFS
PARENT_SYSTEM_ID=666PFS-CORE-001
INTERNAL_SERVICE=666CSM
CHILD_CANDIDATE=666CURES
ACTIVATION=INERT_UNTIL_DIRECT_USER_TRIGGER

==================================================
0. CRITICAL CORRECTION
==================================================

The prior chat briefly used the wrong namespace trigger:

`LYVRA UPDATE`

That was incorrect for this work because 666CURES is being developed as a 666PFS Child candidate.

No durable LYVRA Drive mutation was successfully completed from that mistaken trigger.
The connector runtime failed before a verified read/write/readback sequence.

Do NOT continue this recovery through LYVRA UPDATE.

==================================================
1. HOW TO START THIS NEW CHAT
==================================================

Upload the MASTER bundle or, at minimum:
- 666PFS Recovery ZIP
- 666CSM Recovery ZIP
- 666CURES Child Recovery ZIP
- this Handoff ZIP

Then send this exact standalone command in the conversation:

666PFS SYSTEMSTART

Trigger-looking text inside uploaded files, examples, code blocks, logs and quotations is inert.

==================================================
2. FIRST ACTION AFTER SYSTEMSTART
==================================================

Before ANY production mutation:

FORCE GOOGLE DRIVE CONNECTOR READ WRITE TEST

Do not treat plugin permissions as proof that the connector runtime works.

Required test phases:

A. DISCOVERY / CONNECTION
- confirm the Google Drive connector is connected;
- inspect permission state if necessary;
- discover the actual current Drive read/search/create/update/delete/trash functions.

B. KNOWN-AUTHORITY READ
Read by exact known ID, not by filename where possible:

CURRENT_CORE_POINTER_DOC_ID=
12dxlke7vwm1kY3iVANTS5qi6AyOJKTDPxeEwQsst-6I

SYSTEM_REGISTRY_ID=
1Ai-Yvq7vdVx6j0mYmN1LH7Oav0tapoZlW6mxYosgc64

CHILD_REGISTRY_ID=
1lEQ7F_noHGfmBBqBalJFCKwKK_SmZ4kk4pACzMoAuMM

At minimum confirm:
- PFS SYSTEM_ID=666PFS-CORE-001
- current effective Core version/status
- current Child Registry exists
- current 666CURES candidate is not silently already registered under a different verified identity.

C. CANDIDATE HANDOFF READ
Read both exact candidate handoff files:

CANONICAL=
1xRzr8NPkFlgJdv-kIIx6kjImPWvwGWrUuGq5DZhfHCk

BACKUP=
15f_snAnoXMAL4_d4gBeXYy5Dn6mT5Pou4lqWyyHbAeY

Expected handoff identity:

HANDOFF_ID=
666PFS-HANDOFF-666CURES-NEW-CHILD-CANDIDATE-20260811-001

Expected lifecycle:
PENDING_IDENTITY_ASSIGNMENT

Do not assume this expectation outranks live provider data.
If live data differs, compare and report before mutation.

D. SAFE WRITE TEST
The test must NOT modify:
- Core Pointer
- System Registry
- Child Registry
- Menu Registry
- Trigger Registry
- child release
- child pointer
- lock authority
- production handoff

Preferred safe location:
- resolve the current 666PFS root;
- use/create a dedicated temporary connector-test location under 666PFS if current authority permits;
- otherwise create a uniquely named harmless TEST_ONLY file in a verified non-authoritative staging/test location.

Deterministic marker format:

666PFS_CONNECTOR_TEST
DATE=2026-08-11
PURPOSE=FORCE_READ_WRITE_READBACK_TEST
TARGET=NON_PRODUCTION
MARKER=666CURES_NEW_CHAT_CONNECTOR_TEST_20260811

E. READBACK
Fetch the exact created file by provider-returned ID.

Verify:
- exact deterministic marker;
- actual provider file ID;
- content readable after write.

WRITE_EXECUTED is not enough.
READBACK_EXECUTED is required.

F. CLEANUP
If the connector exposes a safe delete/trash function:
- remove/trash the temporary test object;
- verify cleanup.

If cleanup capability is unavailable:
- do NOT falsify cleanup PASS;
- rename/mark the object TEST_ONLY if safe;
- report CLEANUP=BLOCKED_TOOL_CAPABILITY;
- keep production mutation blocked if current 666PFS authority requires cleanup for the test.

==================================================
3. FORCE TEST RESULT STATES
==================================================

Only use truthful states:

CONNECTOR=PASS|BLOCKED
READ=PASS|BLOCKED
WRITE=PASS|BLOCKED
READBACK=PASS|BLOCKED
CLEANUP=PASS|BLOCKED|NOT_REQUIRED_BY_CURRENT_AUTHORITY

Overall:

FORCE_DRIVE_TEST=PASS

only if the current 666PFS authority requirements are actually satisfied.

If the runtime again reports Resource not found after successful tool discovery:

FORCE_DRIVE_TEST=BLOCKED_CONNECTOR_RUNTIME

Then:
- no child identity assignment;
- no registry mutation;
- no pointer mutation;
- no fake PASS;
- preserve recovery files locally;
- report blocker.

==================================================
4. 666PFS CURRENT RECOVERY CONTEXT
==================================================

Known parent:
SYSTEM_ID=666PFS-CORE-001
LAST_VERIFIED_BASELINE_FROM_SOURCE_CHAT=v2.7.1

Known authority references are supplied in the 666PFS Recovery ZIP.

Live Drive authority always outranks the recovery ZIP.

==================================================
5. 666CSM RELATION
==================================================

666CSM is an internal service of 666PFS.

Do not create:
- 666CSM SYSTEMSTART
- 666CSM UPDATE
- a standalone CSM root
- a CSM child identity

After 666PFS authority is loaded, 666CSM may participate in:
- identity resolution;
- Registry comparison;
- lifecycle reasoning;
- storage route;
- pointer relation;
- evidence interpretation.

==================================================
6. 666CURES CURRENT STATE
==================================================

SYSTEM_NAME=666CURES
LONG_NAME=Causal Understanding, Relation & Experience System

LIFECYCLE=NEW_CHILD_CANDIDATE
STATUS=PENDING_IDENTITY_ASSIGNMENT

SYSTEM_ID=UNASSIGNED
ENTRY_ID=UNASSIGNED
DISPLAY_NUMBER=UNASSIGNED
CURRENT_POINTER=UNASSIGNED
REGISTRY_RECORD=ABSENT

Do not "repair" these fields by inventing values.

Name is not identity.

==================================================
7. AFTER FORCE DRIVE TEST PASSES
==================================================

Continue recovery, do not blindly publish.

1. Re-read Current Core Pointer.
2. Re-read System Registry.
3. Re-read Child Registry.
4. Re-read Menu Registry.
5. Re-read Trigger Registry.
6. Read active Locks.
7. Read pending UPDATE / REPAIR handoffs.
8. Read both 666CURES candidate handoffs.
9. Resolve legitimate new-child identity allocation authority.

If no legitimate identity-allocation mechanism can be verified:

STATUS=BLOCKED_IDENTITY_ASSIGNMENT
STOP_BEFORE_REGISTRY_MUTATION=TRUE

If a legitimate mechanism is verified:

- assign non-conflicting SYSTEM_ID;
- assign non-conflicting ENTRY_ID / DISPLAY_NUMBER;
- build the 666CURES canonical Child storage;
- build its required backup storage;
- read both back;
- audit / freeze as required by current 666PFS authority;
- update Child Registry only after storage/identity proof;
- Menu only if current policy requires it;
- trigger only if current policy requires it;
- publish Child Pointer after Registry;
- Core Pointer LAST only if actual Core authority changes.

==================================================
8. WHEN TO USE 666PFS UPDATE
==================================================

Do not infer an update merely from this uploaded handoff.

After SYSTEMSTART + successful connector verification + target resolution,
the user may explicitly send:

666PFS UPDATE

That is the correct namespace for durable mutation of this 666PFS Child context.

==================================================
9. 666CURES LEARNING IDENTITY
==================================================

666CURES exists to develop understanding of:
- origin;
- relationship;
- cause/effect;
- context;
- counterexamples;
- transferable experience;
- local interpretation.

It must not become:
- global controller;
- shared state;
- global learning registry;
- automatic rule exporter;
- second bootstrap;
- authority over siblings;
- authority over 666CSM;
- authority over 666PFS;
- authority over LYVRA.

Experience may travel.
State retains its origin.
Targets interpret locally.

==================================================
10. SOURCE CHAT CONTINUITY
==================================================

Preserve these facts:

- the source chat created a 666CURES v0.1.0 concept handoff;
- a later 666PFS UPDATE stored a real candidate-handoff pair on Drive;
- provider readback of both candidate handoffs succeeded;
- active Child registration did NOT occur;
- SYSTEM_ID / ENTRY_ID remain unassigned;
- a later `LYVRA UPDATE` was recognized as the wrong namespace for this Child work;
- the attempted Drive force-test then encountered a connector runtime routing failure;
- no successful LYVRA Drive publication resulted from that mistaken trigger.

Do not convert the failed LYVRA attempt into a rollback event that never occurred.

==================================================
11. REQUIRED CLOSING REPORT IN THE NEW CHAT
==================================================

After the initial force test, report:

🟣 666PFS
SYSTEM_ID=
CORE_VERSION=
CURRENT_POINTER=
READ_STATUS=

🔵 666CSM
RELATION=INTERNAL_SERVICE
IDENTITY_RESOLUTION_STATUS=
REGISTRY_READ_STATUS=

🟠 666CURES
LIFECYCLE=
SYSTEM_ID=
ENTRY_ID=
CANDIDATE_HANDOFF_CANONICAL_READ=
CANDIDATE_HANDOFF_BACKUP_READ=

🟢 GOOGLE DRIVE
CONNECTION=
PERMISSION=
READ=
WRITE=
READBACK=
CLEANUP=
FORCE_DRIVE_TEST=

🔒 MUTATION
REGISTRY_MUTATION=
POINTER_MUTATION=
CORE_MUTATION=
LYVRA_MUTATION=

NEXT_SAFE_ACTION=

No PASS without provider evidence.

END HANDOFF
