# 666PFS Registry Layer

This directory is the repository-native routing layer for PFS registries.

Registry classes:
- system registry
- child registry
- menu registry
- trigger registry
- continuity / recovery metadata

Rules:
- repository metadata routes runtime state
- private legacy registry payloads remain outside this public repository
- child autoload is forbidden
- historical sources never become current automatically
- missing evidence produces HOLD instead of guessed state

## Child classification and precedence
Resolve child classification before UPDATE or NEW CHILD using governance/CHILD_AUTHORITY_STORAGE_POLICY_V1.md. Live origin Repo or Drive is first, first-party origin backups second, PFS backup third. The registry cannot infer live ownership from a ZIP or automatically convert existing children.
