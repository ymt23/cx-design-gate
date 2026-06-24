# Multi-Agent Contract

Design Gate can be used in a single-agent flow, but visual quality is stronger when implementation and review are separated. Design Gate does not spawn CX1, CX2, or CX3 by itself. It provides the handoff, review, and rework contracts that a Project Agent or orchestrator can use.

## Preferred Roles

- CX1: Orchestrator and Designer Gate.
- CX2: Implementer.
- Optional CX3: Independent Reviewer.
- Human: Final Judge.

## Rules

- Do not let the implementer be the final visual judge.
- Use Human approval before spawning or handing off to external agents when the environment requires it.
- Give each agent a scoped task and evidence requirements.
- Designer Gate should review screenshot/recording plus contract, not implementation rationale.
- If screenshot evidence and implementer report disagree, prefer screenshot evidence.
- Implementer CX must return evidence, known deviations, and unresolved risks, but must not declare final visual pass.
- Designer CX / Design Gate owns pass, borderline, rework, or fail judgment against visible evidence.

## Contract Flow

1. CX1 prepares Project Context Packet and Visual Fidelity Contract.
2. Human approves implementation handoff.
3. CX2 implements and returns changed files, build/test results, and screenshots.
4. CX1 applies hard fail rules and score caps.
5. Human decides pass, rework, or stop.

## Handoff Packet

- Project Context Packet
- Visual Fidelity Contract
- Implementation scope and forbidden files
- Evidence required: changed files, build/test result, screenshots or recording
- Known role boundary: implementer does not self-approve visual quality

## Review Packet

- Visual Fidelity Contract
- Screenshot or recording evidence
- Implementer report
- Hard fail rules and score caps
- Output: pass, borderline, rework required, or fail

## Rework Packet

- Failed visual gate items
- Focused correction instructions
- Explicit non-goals
- Evidence required after rework
