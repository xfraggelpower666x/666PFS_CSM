# 666PFS Rehydration Matrix

Order:
1. repository README entry
2. system identity
3. rehydration contract
4. 666CSM coordination contract
5. registry routing layer
6. explicitly selected PFS target
7. verified recovery/history source only if repository evidence is insufficient

Decision states:
- SAME_VERSION_SAME_HASH -> NO_UPDATE
- SAME_VERSION_DIFFERENT_HASH -> CONFLICT_HOLD
- LOCAL_VERSION_NEWER -> CONTROLLED_UPDATE
- REMOTE_VERSION_NEWER -> REBASE_OR_BLOCK
- IDENTITY_CONFLICT -> BLOCK
- INCOMPLETE_EVIDENCE -> HOLD

Evidence rules:
- FOUND is not VERIFIED
- SEARCH_RESULT is not READBACK
- READ is not REHYDRATED
