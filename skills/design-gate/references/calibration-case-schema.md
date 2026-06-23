# Calibration Case Schema

Calibration cases are project-local judgment examples. They are not product specifications.

## Storage Model

OSS skill stores the schema and anonymized generic examples.

Each project stores real cases locally, for example:

```text
repo/.codex/cx-design-gate/calibration/
  index.md
  cases/
    <case-id>.md
```

## Case Fields

```yaml
case_id: string
status: active | archived | deleted
screen: string
source_type: lazyweb | mobbin | figma | human | other
reference_paths: [string]
screenshot_paths: [string]
final_verdict: pass | strong-pass | borderline | fail
human_feedback_summary: string
designer_cx_verdict: string
what_worked: [string]
what_failed: [string]
root_cause: [string]
hard_fail_rules_triggered: [string]
reusable_lesson: string
future_prompt_rules: [string]
related_docs: [string]
last_reviewed_at: YYYY-MM-DD
```

## Lifecycle

Create a case after Human final judgment, not during iteration.

Keep active when the lesson still affects current screen work.

Archive when product design or implementation architecture changes enough that the case is no longer an active guide.

Delete only when the case is wrong, duplicated, missing evidence, or harmful to future judgment.

## Usage

Project Agent reads the index, selects active cases relevant to the target screen or component pattern, and adds only the reusable lesson and source path to the Project Context Packet.
