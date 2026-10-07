# PFS / CSM GPT-Native Visual Interface Contract

Presentation surface: ChatGPT conversation UI, not ASCII and not an external dashboard by default.

Hard guards:
- VISUAL_NE_AUTHORITY
- VISUAL_NE_ROUTER
- VISUAL_NE_ACTIVATION
- VISUAL_NE_WRITE_APPROVAL
- BACKUP_NE_CURRENT
- HISTORY_NE_CURRENT
- FOUND_NE_VERIFIED
- SEARCH_RESULT_NE_READBACK
- READ_NE_REHYDRATED
- POINTER_LAST_REQUIRED_FOR_PUBLISHED_CURRENT
- FAKE_BUTTONS_FORBIDDEN
- FAKE_PROGRESS_FORBIDDEN

Preferred composition: heading, evidence status, native table/sections, measured progress if available, blocker/readback note, next valid actions.

True custom clickable controls require an MCP App/Extension UI and must not be claimed from a skill-only rendering path.
