# Rehydration

ENTRY_ID=CURES-16001
STATE=HOLD_FUNCTIONAL_PAYLOAD_SOURCE_NOT_FOUND
1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_BINDING.md.
3. Do not execute or autoload this child while the complete functional payload source is unavailable.
4. The bound recovery source is verified, but no complete functional payload is currently present there; do not infer or synthesize one.
5. When a complete functional payload source becomes available, validate payload, provenance and readback.
6. Mark READY only after repository payload verification.

CHILD_AUTOLOAD=FORBIDDEN
