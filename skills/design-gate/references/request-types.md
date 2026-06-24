# Internal Request Types

Request types are internal intent labels. Humans should normally give short natural-language direction instead of naming these values.

## Intent Table

| internal intent | human asks for | output | required live references |
| --- | --- | --- | --- |
| `reference_gate` | reference research, examples, comparable screens | Lazyweb Lane, Mobbin Lane, Evidence Board, Reference Decision Matrix | Lazyweb + Mobbin |
| `design_direction` | screen ideas, layout direction, information architecture, primary CTA direction | design direction candidates, synthesis, Human decision points | Lazyweb + Mobbin |
| `visual_direction` | mood, polish, decoration, visual treatment, concept feel | visual direction candidates, optional concept evidence, synthesis | Lazyweb + Mobbin |
| `contract` | lock direction for implementation, make an implementation-ready contract | Visual Fidelity Contract | Lazyweb + Mobbin unless already present |
| `handoff` | prepare implementer instructions | Implementer CX handoff packet | contract required |
| `review` | review screenshot or recording | pass / borderline / rework / fail review | screenshot or recording required |
| `rework` | turn review findings into fix instructions | focused rework prompt | failed review findings required |
| `calibration` | create or review a calibration case | calibration draft or critique | Human must explicitly request |
| `version_report` | show version, changelog, current behavior | Plugin Version, Changelog Section, Recent Behavior Changes, Version Consistency | none |

## Inference Rules

- "画面案", "proposal", "ideas", "direction" -> `design_direction`.
- "温かい", "polish", "mood", "visual", "decoration", "concept" -> `visual_direction`.
- "実装前", "contract", "固めて" -> `contract`.
- "実装者に渡す", "handoff", "Implementer CX" -> `handoff`.
- "スクショ", "review", "採点", "pass/fail" -> `review`.
- "修正指示", "rework", "直して" after a review -> `rework`.
- "version", "CHANGELOG", "現在挙動" -> `version_report`.

If several intents match, choose the earliest unfinished phase that can produce a useful next artifact. State that inference in the State Capsule.

## Mutation Rules

Design, visual, reference, and contract intents are non-mutating by default. Do not implement, create specs, create calibration cases, or edit files unless the Human explicitly asks for that mutation.
