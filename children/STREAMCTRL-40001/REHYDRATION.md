# STREAMCTRL-40001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_BINDING.md.
3. Verify source repository, branch and source HEAD.
4. Read source CURRENT_POINTER and REHYDRATION_MANIFEST.
5. Preserve source project/session isolation and LiveCircle semantics.
6. Do not mutate source repository during PFS child rehydration.
7. Do not autoload WEBRADIO, INTRO, WINDOWS_APP or LIGHT_ORCHESTRA.
8. If source binding diverges from newer verified source current, mark HOLD until governed refresh.

READY requires direct source readback and intact identity binding.
