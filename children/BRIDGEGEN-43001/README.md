# 666 BINARY REPOSITORY BRIDGE GENERATOR

A standalone 666PFS child for building and validating safe repository bridge packages when verified binary payloads cannot be transferred through the active direct connector path.

It does not replace the PFS core binary-governance standards. It operationalizes them as a reusable child capability.

## Core rule

DIRECT_BINARY_PATH > BRIDGE_FALLBACK

A bridge is created only when the direct route is genuinely blocked and the source bytes, size, hash, publication permission and exact destination are verified.

## Safety

The bridge never writes PFS Current Pointer, never mutates plugin state, never deploys services, never force-pushes, and never silently promotes candidate/reference payloads.

PASS requires an independent fresh remote readback.
