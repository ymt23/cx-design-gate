# AGENTS.md

## Purpose
Repository operating rules for CX Design Gate. This repo is the reusable OSS plugin/skill body. Project-specific product truth and calibration data must stay outside this repo.

## Scope
These rules apply to all changes in this repository.

## Product Boundary
- Keep reusable workflow logic, schemas, templates, and anonymized examples in this repo.
- Do not commit private project screenshots, proprietary product requirements, customer data, or project-local calibration cases.
- Store real project calibration packs in the consuming project, for example `repo/.codex/cx-design-gate/calibration/`.
- If a case mentions a real product, app, screen, person, customer, or private asset, it does not belong in this OSS repo unless it has been deliberately anonymized.

## Plugin Structure
- Keep `.codex-plugin/plugin.json` present and validation-ready.
- Keep the primary skill at `skills/design-gate/SKILL.md`.
- Put detailed reusable guidance in `skills/design-gate/references/`.
- Put prompt/artifact skeletons in `skills/design-gate/templates/`.
- Put only anonymized reusable calibration patterns in `examples/generic/`.
- Do not move project-local rules into the global skill body.

## Change Policy
- Preserve the separation between:
  - OSS reusable procedure: this repo
  - project product truth: consuming repo docs
  - project calibration data: consuming repo `.codex/cx-design-gate/calibration/`
- Avoid adding implementation details for one project unless they are generalized and anonymized.
- Keep `SKILL.md` concise. Move longer guidance into references.

## Validation
Before committing changes that affect plugin or skill behavior, run:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
python3 /path/to/skill-creator/scripts/quick_validate.py skills/design-gate
```

If the local Python environment lacks PyYAML, use a temporary environment or shim outside this repo. Do not vendor validation dependencies into this repo.

## CHANGELOG Policy
Update `CHANGELOG.md` for:
- skill behavior changes
- schema or template changes
- hard fail or score cap rule changes
- plugin metadata changes visible to users
- generic examples that affect calibration behavior
- release preparation

CHANGELOG is usually not required for:
- typo-only fixes
- formatting-only changes
- local/private files that are not committed
- non-behavioral comment cleanup

## Commit Message Policy
Use English Conventional Commit style:

```text
<type>: <imperative summary>
```

Allowed types:
- `feat`: add or change Design Gate workflow capability
- `fix`: correct plugin, skill, schema, template, or gate behavior
- `docs`: update README, CHANGELOG, examples, or public documentation
- `chore`: update repo metadata, validation setup, marketplace config, or housekeeping
- `test`: add or update validation or forward-test artifacts
- `refactor`: reorganize files without behavior change
- `release`: prepare version or tag

Examples:

```text
docs: Add repository agent rules
fix: Clarify evidence quality semantics
feat: Add calibration index template
chore: Update plugin metadata
```

## Git Policy
- Do not commit generated local caches or project-local calibration data.
- Keep commits scoped and reviewable.
- Run validation before commits that affect plugin loading, skill metadata, or schemas.
- Do not push without explicit Human approval.
