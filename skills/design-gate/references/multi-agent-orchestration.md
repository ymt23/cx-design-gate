# Multi-Agent Orchestration

Design Gate can be used in a single-agent flow, but visual quality is stronger when implementation and review are separated.

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

## Handoff Shape

1. CX1 prepares Project Context Packet and Visual Fidelity Contract.
2. Human approves implementation handoff.
3. CX2 implements and returns changed files, build/test results, and screenshots.
4. CX1 applies hard fail rules and score caps.
5. Human decides pass, rework, or stop.
