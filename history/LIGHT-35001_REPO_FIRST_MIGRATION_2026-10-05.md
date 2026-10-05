# LIGHT-35001 Repo-first Migration — 2026-10-05

## Decision

LIGHT-35001 no longer uses Google Drive as an active CURRENT or backup authority.

Authority order:

1. Native LIGHT ORCHESTRA source: `xfraggelpower666x/WebRadio-666SOUNDsDESIGn`
2. PFS/CSM child metadata and rehydration control: `xfraggelpower666x/666PFS_CSM` branch `main`
3. Google Drive: historical backup/recovery evidence only

## Source checkpoint at migration

- WebRadio branch: `feature/666-light-orchestra-v0.1.0`
- Verified source head: `55613be74e1ba5bc2ba62225247d6fd07caf1e37`
- Offline regression tests: 20/20 PASS
- Release Integrity: PASS
- Radio CodeForge: PASS
- Windows/hardware validation: pending

## Legacy R6 Drive evidence

- Canonical ZIP ID: `1A6rY-2mI1iE8l2ezYzr8T5g9qN86KdCk`
- Backup ZIP ID: `1JXjIJqcgsFTOyCLYQU4a7ISuEFOma6_C`
- SHA-256: `f86dd1a20ece2b8059f0bd9789e2a4cfa30050f5cafe6d2e982f34ee67806852`

These Drive records are preserved but non-authoritative. They must never supersede a newer valid repository state automatically.

## Restore rule

Restore requires explicit user approval and a comparison against the newest verified GitHub source. Child autoload remains forbidden.
