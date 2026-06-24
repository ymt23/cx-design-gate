# I/O Contract

Use this contract so a Human or Project Agent can invoke Design Gate without restating `request_type`, Lazyweb, Mobbin, Evidence Board, Reference Decision Matrix, no-mutation, State Capsule, or Self-Review instructions.

## Human-Facing Input

Prefer short natural-language direction:

```text
@cx-design-gate
MN Home の画面案を出してください。
requirements は docs/ops/tasks/.../home_skeleton.md を参照してください。
```

The Human should not have to name `request_type`, Lazyweb, Mobbin, Evidence Board, Reference Decision Matrix, or no-mutation constraints. Explicit `request_type` remains supported for backward compatibility.

## Default Rules

- Infer the internal intent from the latest Human direction.
- Default calibration path is `.codex/cx-design-gate/calibration/index.md`.
- If the default calibration path is absent, continue with `Calibration skipped`.
- If a Human or Project Agent explicitly provides a calibration path and it is unreadable, return `Input blocked`.
- For design, visual, reference, and contract intents, default to no implementation, no specification creation, no calibration creation, and no file edits.
- If the input contains Japanese text, respond in Japanese. Keep tool names, source names, source URLs, IDs, file paths, enum values, and code-like tokens unchanged.

## Internal Processing Order

1. Human Direction
2. Internal Intent
3. Resolved Context
4. MCP Availability
5. Lazyweb Lane
6. Mobbin Lane
7. Evidence Board
8. Reference Decision Matrix
9. Synthesis Lane
10. Calibration Lessons Used
11. Requested Output
12. State Capsule
13. CXDG Self-Review

## Reference Lanes

- Lazyweb Lane: flow, direction, hypotheses, screen patterns, and A/B-style clues.
- Mobbin Lane: shipped UI examples, component structure, density, spacing, and transitions.
- Synthesis Lane: adoption, transformation, rejection, integrated recommendation, and Human decision points.

Do not collapse Lazyweb and Mobbin into one undifferentiated list. Their differences are part of the evidence.

## Legacy Packet

For backward compatibility, also accept:

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

The Project Agent must provide requirement source paths. It must not prebuild live reference research, Evidence Board, Reference Decision Matrix, or design proposals.

## Legacy Processing Order

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
- an explicitly provided calibration path is missing or unreadable
- the requested work could mutate files and the Human did not explicitly ask for implementation, spec creation, calibration creation, or file edits

Return `Reference research blocked` and do not continue when:
- Lazyweb is unavailable, unauthenticated, or returns no usable evidence
- Mobbin is unavailable, unauthenticated, or returns no usable evidence

Calibration cases can guide judgment, but they do not replace live Lazyweb/Mobbin evidence.

## Fixed Output

Use this order for design direction and visual direction outputs:

1. Input Summary
2. Context Read Result
3. MCP Availability
4. Lazyweb Lane
5. Mobbin Lane
6. Evidence Board
7. Reference Decision Matrix
8. Synthesis Lane
9. Calibration Lessons Used
10. Design Direction or Visual Direction Candidates
11. Human Decision Points
12. Blockers / Risks
13. State Capsule
14. CXDG Self-Review

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

## Version Report

When the Human asks for version, CHANGELOG, current behavior, or plugin version, produce:

1. Plugin Version
2. Changelog Section
3. Recent Behavior Changes
4. Version Consistency

Use `.codex-plugin/plugin.json` as the version source of truth. The top `CHANGELOG.md` heading must match that version. If not, report `Version mismatch`.
