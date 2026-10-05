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
