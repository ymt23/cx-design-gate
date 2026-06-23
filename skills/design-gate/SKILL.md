---
name: design-gate
description: Visual fidelity gate for AI-driven UI design and implementation. Use when Codex must turn a screen requirement, concept art, screenshot reference, Lazyweb/Mobbin reference, or implemented UI screenshot into a reviewed Visual Fidelity Contract, implementation handoff, rework instruction, or pass/fail design gate. Use for Human/CX role separation, Project Context Packet intake, persistent-control versus scroll-content layer checks, hard fail rules, score caps, and multi-agent UI implementation review.
---

# Design Gate

Use Design Gate to prevent implementation agents from treating build success or constraint satisfaction as visual success. The skill owns the workflow between project-specific requirements, reference material, implementation handoff, and screenshot-based design review.

## Core Rule

Keep project truth outside this skill. Read project documents and calibration packs through a Project Context Packet. This skill supplies the procedure, schemas, gates, prompts, and generic failure patterns.

## Workflow

1. Obtain or request a Project Context Packet before making a design judgment.
2. Read only the packet-linked project documents, screen requirements, references, and active calibration cases needed for the target screen.
3. Produce one of these outputs, matching the user's request:
   - Visual Fidelity Contract
   - Implementer Handoff Prompt
   - Designer Screenshot Review
   - Rework Instruction
   - Calibration Case Draft
4. Apply hard fail rules before assigning a score.
5. Treat screenshots and visible behavior as stronger evidence than implementation self-reports.
6. Do not implement unless the user explicitly asks for implementation.

## Role Split

Use the detailed role model in `references/role-model.md` when a task involves multiple CX roles or Human handoff.

Default roles:
- Human: Director and final judge.
- Project Agent: Collects project truth and creates the Project Context Packet.
- Design Gate / Designer CX: Reviews visible UI against contract and hard gates.
- Architect CX: Converts requirements and references into contracts.
- Implementer CX: Builds from the contract and returns screenshot/build evidence.
- MCP services: Provide references only; they do not decide adoption or visual pass.

## Required Inputs

If the task lacks a Project Context Packet, ask the Project Agent or Human for one, or produce a packet request using `templates/project-context-packet.md`.

Minimum packet fields:
- project_id
- target_screen
- screen_requirements
- design_principles
- implementation_scope
- reference_assets
- non_negotiable_rules
- release_constraints
- active_calibration_cases

See `references/project-context-packet.md` for the full schema.

## Layer Gate

Always distinguish persistent controls from scroll content:
- Persistent Control Layer: tab bars, nav bars, toolbars, floating CTAs, HUDs, sticky action bars.
- Scroll Content Layer: cards, lists, grids, carousels, feeds, form sections, inventory/item grids.

Persistent controls must not deform scroll-content item internals. If overlap must be managed, prefer scroll padding, safe area, z-index, hit-area rules, or review-scoped acceptance. Do not shrink card text, alter item dimensions, or distort content layout to avoid an overlay.

## Hard Fail First

Before scoring, apply `references/hard-fail-rules.md`. If a hard fail applies, say so directly and do not call the result pass.

Common hard fails:
- Primary text is unreadable, clipped, hidden, or too compressed at screenshot scale.
- Grid/list/card item display is broken even if constraints technically fit.
- Persistent controls deform content item internals.
- Screenshot contradicts the implementer's self-report.
- Build/test success is used as visual pass evidence.

## Score Caps

If the user requests scoring, apply `references/score-cap-rules.md`. Score caps limit optimistic scoring when important evidence is missing or partially broken.

## Resources

- `references/role-model.md`: Human/CX/MCP responsibilities and forbidden judgments.
- `references/project-context-packet.md`: Context packet schema and intake rules.
- `references/visual-fidelity-contract.md`: Contract structure for image/reference to UI implementation.
- `references/hard-fail-rules.md`: Non-negotiable visual fail conditions.
- `references/score-cap-rules.md`: Score cap rubric.
- `references/calibration-case-schema.md`: Project-local calibration case schema.
- `references/multi-agent-orchestration.md`: CX1/CX2/CX3 orchestration guidance.
- `templates/*.md`: Prompt and artifact templates.
- `../../examples/generic/*.md`: Anonymized pass/fail calibration patterns.

## Output Discipline

Use concise, evidence-led judgments. Separate:
- observed screenshot result
- implementation claim
- contract requirement
- pass/fail decision
- next action

When the screenshot and implementation report disagree, prefer the screenshot.
