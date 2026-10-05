# STREAM-5001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read RUNTIME_BINDING.md.
3. Verify the bound source repository and commit still exist.
4. Do not mutate the source repository during rehydration.
5. If the bound commit is unavailable or diverges from current verified evidence, set HOLD and require controlled rebase.
6. Child autoload remains forbidden; rehydrate only after explicit selection.

READY requires successful source verification and intact identity binding.
