# I/O Contract

Use this contract so a Project Agent can invoke Design Gate without restating Lazyweb, Mobbin, Evidence Board, or Reference Decision Matrix instructions.

## Minimal Invocation Packet

For `design_direction`, accept this minimal input:

```yaml
request_type: design_direction
project_id: string
target_screen: string
requirements:
  paths: [string]
calibration:
  index_path: string
constraints:
  no_implementation: true
  no_spec_creation: true
  no_calibration_creation: true
```

The Project Agent must provide source paths. It must not prebuild live reference research, Evidence Board, or Reference Decision Matrix.

## Internal Processing Order

1. Minimal Invocation Packet
2. Resolved Context
3. MCP Availability
4. Evidence Board
5. Reference Decision Matrix
6. Calibration Lessons Used
7. Design Direction A/B/C
8. Human Decision Points
9. Blockers / Risks

## Blocking Rules

Return `Input blocked` and do not continue when:
- a requirements path is missing or unreadable
- the calibration index path is missing or unreadable
- required constraints are absent and the requested work could mutate files or create specs

Return `Reference research blocked` and do not continue when:
- Lazyweb is unavailable, unauthenticated, or returns no usable evidence
- Mobbin is unavailable, unauthenticated, or returns no usable evidence

Calibration cases can guide judgment, but they do not replace live Lazyweb/Mobbin evidence.

## Fixed Output

Use this order for `design_direction`:

1. Input Summary
2. Context Read Result
3. MCP Availability
4. Evidence Board
5. Reference Decision Matrix
6. Calibration Lessons Used
7. Design Direction A/B/C
8. Human Decision Points
9. Blockers / Risks

## Concept Evidence

CX image generation is purpose-based.

Use it after Lazyweb/Mobbin evidence when the request or requirements ask for mood, polish, decoration, visual direction, concept art, or visual exploration.

Do not use it as a substitute for Lazyweb or Mobbin. If concept evidence is not generated, output:

```text
Concept Evidence: not generated
Reason: <brief reason>
```

## Evidence Storage

The initial contract requires Markdown preview plus source URL or identifier. Do not require local image persistence. If evidence is later saved, keep project-private evidence in the consuming project, not in the OSS plugin.
