# LYVRADASH-39001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read DASHBOARD_CARD.md.
4. Resolve runtime payload only when LYVRADASH-39001 is explicitly selected.
5. Preserve PNG transparency; never silently convert transparent PNG assets to JPEG.
6. Preserve the existing dashboard architecture and additive integration model.
7. Do not replace WEBLyvra/live/dist/index.html with the dashboard.
8. Intended dashboard target is an isolated /dashboard/ path beneath the host distribution.
9. Keep external radio iframe isolated from dashboard audio-analysis logic.
10. A file:// offline test is not sufficient to declare iframe/media integration broken.
11. Production validation should use HTTP/HTTPS origin or a local HTTP server.
12. Preserve reduced-motion support and explicit animation pause behavior.
13. Preserve cacheable external image assets; do not re-inline large images as Base64 without explicit instruction.
14. Do not autoload into LYVRA, WEBLYVRA, 666STREAM, or another PFS child.
15. Missing repository binary payload produces PARTIAL / READBACK_PENDING; never fabricate READY.

FOUND != VERIFIED
SEARCH_RESULT != READBACK
READ != REHYDRATED
