# PFS / CSM Local Adaptive Learning Contract

Semantic Cyber Field is a shared visual/semantic contract only. Learning state remains local to PFS/CSM.

Pipeline: SIGNAL -> INTERPRETATION -> EVIDENCE -> CONFIDENCE -> DECISION -> ACTION -> OUTCOME -> LEARNING.

Learning states: CANDIDATE, LEARNING, VALIDATED, INTEGRATED, REJECTED, INSUFFICIENT_DATA.
Provenance: LOCAL_OBSERVATION, LOCAL_RUNTIME, USER_CORRECTION, PEER_PROPOSAL, EXTERNAL_REFERENCE, VALIDATED_TEST.
Currentness: CURRENT, AGING, STALE, UNVERIFIED_CURRENTNESS.

Required fields: first_seen, last_seen, observations, contradictions, validation_count, last_validated, validity_window, source_system, accepted_by.

Hard guards:
- LEARNING_NE_WRITE_AUTHORITY
- SHARED_SEMANTICS_NE_SHARED_MEMORY
- PEER_PROPOSAL_NE_LOCAL_LEARNING
- LEARNED_NE_PERMANENT
- CONTRADICTION_NE_OVERWRITE
- OUTCOME_REQUIRED_FOR_ADAPTIVE_PROMOTION
- INFERRED_NE_IRREVERSIBLE_ACTION
- LOCAL_LEARNING_SCOPE_ONLY

Cross-system flow: peer observation -> proposal -> local validation -> local learning. Never mutate another native system's learning state.
