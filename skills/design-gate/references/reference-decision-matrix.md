# Reference Decision Matrix

Use this matrix after the Evidence Board and before producing a design direction or Visual Fidelity Contract.

## Required Behavior

Lazyweb and Mobbin are both required for screen proposal, design direction, reference gate, and contract creation workflows.

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

Design directions must cite the Evidence Board and matrix decisions they use. A proposal that does not cite Lazyweb and Mobbin evidence and matrix rows is incomplete.

Calibration cases can influence interpretation, but they do not replace live reference research.
