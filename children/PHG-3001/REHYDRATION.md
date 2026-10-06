# Rehydration

ENTRY_ID=PHG-3001
STATE=READY
VERSION=2.16.0

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_BINDING.md.
3. Read the verified repo-native payload at `children/PHG-3001/runtime/666_PHOTOREALISMUS_GENERATOR_v2_16_0_FREEZE_01.zip`.
4. Verify size `3884412`, SHA-256 `9d29ac1d5f9812a27ff2abc89c1ee15a2fec58dbcb4e48efb4a0ecd22ad85bae`, and Git blob `1e047428e27cf0b3f618c69890a253b9ddd61f8d`.
5. Repository byte readback is PASS.
6. Child autoload remains forbidden; load only on explicit target selection.

CHILD_AUTOLOAD=FORBIDDEN
REPOSITORY_BYTE_READBACK=PASS
