# 666PFS Child Menu Contract

The child menu is a visual operational overview, not a flat text list.

## Menu behavior
- group children by functional domain when classification exists
- show one card per registered child
- show lifecycle / health state before descriptive text
- expose trigger and authority summaries without executing anything
- preserve child identity boundaries
- allow selection only after explicit user choice

## Card states
- READY / VERIFIED
- PARTIAL
- UPDATE_AVAILABLE
- RECOVERY_REQUIRED
- BLOCKED
- CONFLICT
- NOT_REHYDRATED

## Hierarchy
666PFS -> 666CSM -> registries -> child cards -> explicitly selected child

Selection does not imply autoload. Child autoload remains forbidden.

## Visual authority class
Show EXTERNAL_BACKUP_CHILD / PFS_LOCAL_LIVE_CHILD / SYSTEM_ARTIFACT_CHILD only when verified. Always display first actual canonical Repo-or-Drive origin LIVE authority, then native-system Repo/Drive backup, then PFS backup; mark unverified links HOLD. Do not render backup as live.
