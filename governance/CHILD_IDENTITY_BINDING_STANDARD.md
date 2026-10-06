# 666PFS Child Identity Binding Standard

DATE=2026-10-06
SYSTEM_ID=666PFS-CORE-001
STANDARD_ID=CHILD_IDENTITY_BINDING_STANDARD
VERSION=1.0.0
STATUS=ACTIVE

## Core rule

NAME_OR_ID_MATCH != FUNCTIONAL_IDENTITY_MATCH

A child may never be reused, rebound, evolved, renamed, or treated as the target of a new project solely because its name, abbreviation, entry ID, system ID, folder name, or apparent semantic similarity looks compatible.

When the intended function of an existing child is unclear, the child itself must be inspected before any binding or mutation occurs.

## Mandatory verification before child reuse

Before an existing child can be selected for a new project or function, inspect the strongest currently available evidence, in this order where applicable:

1. Current Pointer / Current State references for that child.
2. SYSTEM_IDENTITY.md.
3. REHYDRATION.md.
4. SOURCE_BINDING.md and/or SOURCE_MANIFEST.md.
5. README.md and dashboard card.
6. Current runtime/source content or repository subtree.
7. Verified handoff / freeze / recovery evidence when current metadata is insufficient.
8. Legacy Drive evidence only as history/recovery evidence when repository evidence is insufficient.

The verification must establish:
- functional purpose,
- scope,
- authority,
- runtime/source ownership,
- compatibility with the requested project,
- whether the child is already assigned to another function.

## Decision rules

AMBIGUOUS_CHILD_MATCH => READ_CHILD_BEFORE_BINDING
UNVERIFIED_CHILD_REUSE => FORBIDDEN
FUNCTIONAL_IDENTITY_MISMATCH => KEEP_EXISTING_CHILD_UNCHANGED
FUNCTIONAL_IDENTITY_MISMATCH => CREATE_SEPARATE_CHILD_IF_USER_AUTHORIZES_NEW_CHILD
INSUFFICIENT_EVIDENCE => OPEN_OR_CONFLICT_QUARANTINE
NAME_SIMILARITY_ONLY => NOT_SUFFICIENT
ID_SIMILARITY_ONLY => NOT_SUFFICIENT
HISTORY_BACKUP => NEVER_AUTO_PROMOTE_TO_LIVE

A child with unclear identity must not be modified merely to make it fit the new request.

## Mutation guard

Before a protected child binding or identity mutation:
1. resolve current authority,
2. create pre-change backup,
3. verify child identity from content,
4. verify no identity/scope conflict,
5. perform minimal change,
6. direct readback,
7. update dependent registry/dashboard/handoff surfaces,
8. publish CURRENT_POINTER last,
9. perform no mutation after pointer publication in the same update.

## Incident rule

If a wrong child binding is detected:
- stop further propagation,
- preserve unrelated newer valid state,
- restore the affected child from verified pre-change evidence,
- remove erroneous binding metadata,
- record rollback receipt,
- do not reuse the child again until its function is directly verified.

## CURES incident precedent

The 2026-10-06 CURES-16001 rollback is the precedent establishing this rule:
a name/ID resemblance was not sufficient to prove that an existing child was the intended target.

This standard is global for all 666PFS child creation, registration, migration, rebinding, evolution, and recovery workflows.
