# MP3MANAGER-45001 Rehydration

STATUS=REGISTERED_PENDING_BINARY_AND_RESTORE
Read SYSTEM_IDENTITY.md and verify PFS Current Pointer. Source: review commit 92aac7fd9f854a1fefdcc677692d99c0f5243b18. Validate original ZIP SHA-256 before use. Never auto-execute. Child binary binding, independent readback, and restore testing remain pending.

## Recovery route — 2026-10-29
Use immutable SOURCE_REVIEW_COMMIT and SOURCE_GIT_BLOB from SOURCE_MANIFEST.md. Download exact archive from the preserved commit, compare its SHA-256 and size, test ZIP CRC and extract all files to a clean temporary folder. No second ZIP copy is required for this child-specific source-bound artifact. Source restore was locally tested with 33/33 files; Windows runtime remains OPEN. Never autoload or assert READY from ZIP checks alone.
