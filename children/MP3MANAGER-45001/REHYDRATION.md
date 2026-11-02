# MP3MANAGER-45001 Rehydration

STATUS=REGISTERED_PENDING_BINARY_AND_RESTORE
Read SYSTEM_IDENTITY.md and verify PFS Current Pointer. Source: review commit 92aac7fd9f854a1fefdcc677692d99c0f5243b18. Validate original ZIP SHA-256 before use. Never auto-execute. Child binary binding, independent readback, and restore testing remain pending.

## Recovery route — 2026-10-29
Use immutable SOURCE_REVIEW_COMMIT and SOURCE_GIT_BLOB from SOURCE_MANIFEST.md. Download exact archive from the preserved commit, compare its SHA-256 and size, test ZIP CRC and extract all files to a clean temporary folder. No second ZIP copy is required for this child-specific source-bound artifact. Source restore was locally tested with 33/33 files; Windows runtime remains OPEN. Never autoload or assert READY from ZIP checks alone.


## v2.32 current source — 2026-11-02
Current source commit 638825f98bf3230d90218770cd634190f0edfdff; blob ae49001dfe4bc28c504c4ab57a0ef813059d7fa4. Verify ZIP SHA-256 e41ecb237c777f77e11ff79679b45ef4e01c2ae2c6cb54535152f5bfcd2fda07 and 40 entries. Previous v2.27 recovery is retained; Windows runtime acceptance for v2.32 is OPEN. Never autoload.
