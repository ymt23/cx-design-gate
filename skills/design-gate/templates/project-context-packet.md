# Project Context Packet

For normal use, the Human or Project Agent may provide short direction instead:

```text
@cx-design-gate
MN Home の画面案を出してください。
requirements は docs/ops/tasks/.../home_skeleton.md を参照してください。
```

Explicit request_type remains supported for backward compatibility:

```yaml
request_type: design_direction
project_id:
target_screen:
requirements:
  paths:
calibration:
  index_path:
constraints:
  no_implementation: true
  no_spec_creation: true
  no_calibration_creation: true
```

project_id:
target_screen:
request_type:

## Screen Requirements
- paths:
- excerpts:

## Design Principles
- paths:
- excerpts:

## Implementation Scope
allowed_files:
forbidden_files:

## Current Implementation
paths:

## Reference Assets
- id:
  type:
  path_or_url:
  notes:

## Reference Research Required
- Lazyweb: required for design_direction, visual_direction, reference_gate, contract
- Mobbin: required for design_direction, visual_direction, reference_gate, contract
- blocked_if_missing: true

## Non-Negotiable Rules
-

## Release Constraints
-

## Active Calibration Cases
- case_id:
  path:
  reusable_lesson:
  hard_fail_rules:

## Evidence Required
- screenshot
- build_result
- test_result
