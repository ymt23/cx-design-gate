# Contributing

CX Design Gate is an early OSS scaffold. Contributions should preserve the separation between reusable workflow logic and project-specific design truth.

## Contribution Rules

- Do not add private project screenshots, product names, or proprietary screen requirements to the OSS repository.
- Keep project-specific calibration cases in the project repo, not here.
- Add only anonymized generic examples under `examples/generic/`.
- Keep `SKILL.md` concise. Put detailed reusable guidance in `references/`.
- Update templates when changing workflow requirements.
- Run plugin and skill validation before proposing changes.

## Validation

Use the Codex plugin and skill validation scripts when available:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
python3 /path/to/skill-creator/scripts/quick_validate.py skills/design-gate
```

If the local Python environment lacks PyYAML, install it outside this repository or use a temporary environment. Do not vendor validation dependencies into this plugin.
