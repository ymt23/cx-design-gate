# Project Context Packet

A Project Context Packet is the required input for Design Gate. It lets a project-specific agent pass the right local truth without copying project-specific knowledge into the OSS skill.

## Required Fields

```yaml
project_id: string
target_screen: string
request_type: contract | handoff | review | rework | calibration
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
- If packet summaries and source excerpts conflict, prefer source excerpts.
- Do not load all calibration cases. Load only active cases relevant to the target screen or component pattern.
