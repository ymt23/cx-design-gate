# Reference Decision Matrix

Use this matrix after the Lazyweb Lane, Mobbin Lane, and Evidence Board, and before producing a design direction, visual direction, or Visual Fidelity Contract.

## Required Behavior

Lazyweb and Mobbin are both required for screen proposal, design direction, visual direction, reference gate, and contract creation workflows.

If either source is unavailable, unauthenticated, missing from the active tool list, or returns no usable reference evidence, stop with:

```text
Reference research blocked
```

Include the missing source and the attempted query. Do not continue by relying only on project requirements, calibration cases, memory, or general design knowledge.

## Required Columns

| source | query | result_url | result_title/app | why_relevant | adoption_mode | target_component | transformed_lesson |
| --- | --- | --- | --- | --- | --- | --- | --- |

`source` must be `lazyweb` or `mobbin`.

`adoption_mode` must be one of:
- `adopt`: use the reference behavior directly where it matches project requirements.
- `transform`: translate the reference into the project's product, platform, and tone.
- `reject`: explicitly avoid the reference because it conflicts with requirements or calibration.
- `compare_only`: use the reference only as contrast or market context.

## Output Rule

Design directions and visual directions must cite the Evidence Board and matrix decisions they use. A proposal that does not cite Lazyweb and Mobbin evidence and matrix rows is incomplete.

Keep Lazyweb and Mobbin rows distinguishable. Lazyweb should mainly support flow, direction, hypothesis, and screen-pattern lessons. Mobbin should mainly support shipped UI, component structure, density, spacing, and transition lessons.

Calibration cases can influence interpretation, but they do not replace live reference research.
