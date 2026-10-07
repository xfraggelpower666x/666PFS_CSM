---
name: 666pfs-visual-interface
description: Present verified PFS/CSM state as GPT-native chat UI with compact status sections, Markdown tables, progress indicators and contextual next actions; never use ASCII dashboard frames.
---
# 666PFS VISUAL INTERFACE — GPT-native presentation adapter

Read [authority](../../references/authority.md) and [visual contract](../../references/visual-interface-contract.md) before rendering. Current repository contracts outrank this presentation skill.

This skill is presentation only. It never selects a child, authorizes a write, changes CSM scope, promotes backup/history to Current, resolves a lock, or creates system authority.

## Rendering mode
Use ChatGPT-native conversation rendering. Do NOT draw terminal/ASCII boxes, pseudo-window borders, monospaced dashboard mockups, or fake buttons in code blocks.

Prefer, in this order:
1. compact heading with native emoji/icon accent;
2. short status line using evidence labels;
3. native Markdown table when 2+ fields compare cleanly;
4. short progress line/bar only when an actual measured count exists;
5. concise explanatory prose;
6. contextual next-action suggestions at the end.

For SYSTEMSTART, UPDATE, WEITER, AUDIT, child lifecycle, CSM coordination, backup governance and explicit dashboard requests, render only the cards/sections relevant to the verified state.

Suggested visual sections may include PFS identity/current, repository HEAD/pointer, rehydration, daemon/LifeCircle, child registry, CSM sub-LifeCircle, scope map, plugin parity, backup/readback gates, LYVRA/CLIC handoffs, locks/conflicts, visual standstill and exact return anchor.

Use only VERIFIED, ABGELEITET, VORGESCHLAGEN, OFFEN, BLOCKIERT, PARTIAL, WRITE_BLOCKED, READBACK_PENDING and CONFLICT_QUARANTINE when supported by evidence. Never invent completion percentages, PASS states, timestamps, hashes or branch state.

## GPT-native next actions
After a state view, offer only actions that are currently valid under native authority. Prefer concise action labels such as `666PFS WEITER`, `666PFS STATUS`, `AUDIT`, or a verified child action. Never invent a child token. If the host exposes native suggested-action UI, these labels may be surfaced there; otherwise render them as plain follow-up suggestions, not simulated buttons.

A Visual Standstill view means an intentional stable checkpoint only. Show reason, last verified checkpoint, lock/write state, unresolved obligations and exact return anchor. It never implies completion or write success.

Never expose secrets, tokens, private recovery payloads or signed material.
