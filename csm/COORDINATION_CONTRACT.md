# 666CSM Coordination Contract

666CSM is the internal coordination service of 666PFS.

Responsibilities:
- registry coordination
- child lifecycle governance
- continuity and recovery routing
- write-order enforcement
- post-write readback enforcement

Boundaries:
- no child autoload
- no cross-child merge
- no foreign-system mutation
- no authority invention
- pointer-style publication is always the last mutation of a governed update
