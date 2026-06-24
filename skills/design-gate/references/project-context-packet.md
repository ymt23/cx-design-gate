# Project Context Packet

A Project Context Packet is the resolved context Design Gate uses after reading the minimal invocation input. It lets a project-specific agent pass the right local truth without copying project-specific knowledge into the OSS skill.

For normal use, the Project Agent may provide only short Human direction and requirement paths. Design Gate infers the internal intent, applies defaults from `io-contract.md`, and resolves the input into this packet shape. Explicit `request_type` remains supported for backward compatibility.

## Required Fields

```yaml
project_id: string
target_screen: string
request_type: design_direction | visual_direction | reference_gate | contract | handoff | review | rework | calibration | version_report
screen_requirements:
  paths: [string]
  excerpts: [string]
design_principles:
  paths: [string]
  excerpts: [string]
implementation_scope:
  allowed_files: [string]
  forbidden_files: [string]
current_implementation:
  paths: [string]
reference_assets:
  - id: string
    type: concept_art | screenshot | mobbin | lazyweb | figma | other
    path_or_url: string
    notes: string
non_negotiable_rules: [string]
release_constraints: [string]
active_calibration_cases:
  - case_id: string
    path: string
    reusable_lesson: string
    hard_fail_rules: [string]
evidence_required: [screenshot, build_result, test_result]
```

## Intake Rules

- If a packet is missing, request it or produce a packet request.
- If source paths are missing, treat the packet as incomplete.
- If a minimal invocation has unreadable requirements, return `Input blocked`.
- If the default calibration path `.codex/cx-design-gate/calibration/index.md` is absent, continue with `Calibration skipped`.
- If an explicitly provided calibration path is unreadable, return `Input blocked`.
- If packet summaries and source excerpts conflict, prefer source excerpts.
- Do not load all calibration cases. Load only active cases relevant to the target screen or component pattern.
- If `reference_assets` is empty for `design_direction`, `visual_direction`, `reference_gate`, or `contract`, run Lazyweb and Mobbin reference research and create a Reference Decision Matrix before proposing UI.
- Treat a request for screen ideas, screen proposals, or initial screen direction as `design_direction` even when the prompt does not name that request type.
- Treat mood, polish, decoration, or visual treatment requests as `visual_direction`.
