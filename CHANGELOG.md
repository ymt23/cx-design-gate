# Changelog

## 0.2.0 - Unreleased

- Added conversation-first Human input rules so `request_type` is optional for normal use.
- Added internal intent/state handling for design, visual polish, contract, handoff, review, rework, reference gate, calibration, and version report flows.
- Added Lazyweb Lane, Mobbin Lane, and Synthesis Lane guidance for parallel reference comparison.
- Added default calibration discovery, default no-mutation constraints, and input-language response handling.
- Added State Capsule and Self-Review output requirements.
- Added version report behavior and version/CHANGELOG consistency rules.
- Added Human Prompt Examples to README for Human/CX alignment.
- Strengthened multi-agent handoff, review, and rework evidence contracts without making Design Gate a runtime orchestrator.

## 0.1.0 - 2026-06-24

- Added required Lazyweb/Mobbin reference research before design directions, reference gates, and Visual Fidelity Contracts.
- Added `design_direction` I/O contract for minimal Project Agent invocation.
- Added Evidence Board template and fixed design direction output order.
- Added purpose-based CX image generation handling as concept evidence.
- Added Reference Decision Matrix reference and template.
- Added `design_direction` and `reference_gate` request types to the Project Context Packet schema.
- Added `Reference research blocked` behavior when required reference MCP sources are unavailable.
- Initial CX Design Gate plugin scaffold.
- Added `design-gate` skill.
- Added Project Context Packet, Visual Fidelity Contract, hard fail, score cap, calibration case, and multi-agent orchestration references.
- Added generic pass/fail calibration examples.
- Confirmed local Codex plugin loading in a new chat as `cx-design-gate:design-gate`.
- Added repository agent rules for commits, changelog updates, validation, and project-local data boundaries.
- Documented the recommended requirements-to-research-to-concept-to-review workflow.
