---
name: design-gate
description: Conversation-first visual design gate for AI-driven UI design and implementation. Use when Codex must turn short human direction, screen requirements, concept art, Lazyweb/Mobbin references, or implemented UI screenshots into design direction, visual direction, Evidence Board, Reference Decision Matrix, Visual Fidelity Contract, implementation handoff, rework instruction, pass/fail design review, State Capsule, Self-Review, or version report. Use for Human/CX role separation, internal request intent, parallel Lazyweb/Mobbin reference lanes, required reference research before proposals or contracts, hard fail rules, score caps, and multi-agent handoff/review contracts.
---

# Design Gate

Use Design Gate to prevent implementation agents from treating build success or constraint satisfaction as visual success. The skill owns the conversation-first workflow between project-specific requirements, reference material, design direction, implementation handoff, and screenshot-based design review.

## Core Rule

Keep project truth outside this skill. Read project documents and project-local calibration packs from the consuming project. Humans should direct outcomes in natural language; Design Gate infers the internal intent and supplies the procedure, schemas, gates, prompts, and generic failure patterns.

## Workflow

1. Accept short Human direction. Do not require Humans to provide `request_type`, Lazyweb/Mobbin instructions, Evidence Board instructions, or no-mutation constraints.
2. Infer the internal intent. Accept explicit `request_type` only as a backward-compatible override.
3. Resolve requirements, default calibration, constraints, and any linked references into a Project Context Packet.
4. For design, visual, reference, or contract intents, run the Reference Research Workflow before proposing a screen direction or contract.
5. If required input is missing, stop with `Input blocked`. If required reference research is blocked, stop with `Reference research blocked`.
6. Build parallel Lazyweb and Mobbin reference lanes, then an Evidence Board and Reference Decision Matrix before converting references into direction or contract outputs.
7. Apply hard fail rules before assigning a score.
8. Treat screenshots and visible behavior as stronger evidence than implementation self-reports.
9. Do not implement unless the user explicitly asks for implementation.
10. End each response with State Capsule and CXDG Self-Review unless the request is only a terse version check.
11. Produce one of these outputs, matching the inferred intent:
   - Design Direction
   - Visual Direction
   - Evidence Board
   - Reference Decision Matrix
   - Visual Fidelity Contract
   - Implementer Handoff Prompt
   - Designer Screenshot Review
   - Rework Instruction
   - Calibration Case Draft
   - Version Report

## Reference Research Workflow

Use this workflow whenever the user asks for a screen proposal, visual direction, design direction, reference gate, or Visual Fidelity Contract, even if the user does not name an internal request type.

Required sequence:
1. Read the packet-linked requirements and relevant active calibration cases.
2. Confirm both Lazyweb and Mobbin MCP reference tools are available.
3. Search Lazyweb and Mobbin with target-screen queries derived from the requirements.
4. Keep results in separate lanes:
   - Lazyweb Lane: flow, direction, hypotheses, screen patterns, and A/B-style clues.
   - Mobbin Lane: shipped UI examples, component structure, density, spacing, and transitions.
   - Synthesis Lane: adoption, transformation, rejection, and integrated recommendations.
5. Build an Evidence Board with preview, source URL or identifier, relevance, and evidence type.
6. Decide whether concept evidence is needed. Use CX image generation only when the request or requirements ask for mood, polish, decoration, visual direction, or concept art. If not used, state `Concept Evidence: not generated` and why.
7. Create a Reference Decision Matrix with `adopt`, `transform`, `reject`, or `compare_only` for each reference.
8. Only after the Evidence Board and matrix, produce design directions, visual directions, or a Visual Fidelity Contract.

Do not use calibration cases as a substitute for live Lazyweb/Mobbin reference research. If either Lazyweb or Mobbin is unavailable, missing, unauthenticated, or returns no usable evidence, output `Reference research blocked` with the missing source and do not produce screen proposals.

For Mobbin, use screen and flow results as static or flow references unless the tool response includes motion evidence. Do not infer video, duration, easing, or animation metadata from Mobbin screen images.

For detailed input and output shape, use `references/io-contract.md`, `references/request-types.md`, `templates/evidence-board.md`, `references/reference-decision-matrix.md`, `templates/design-direction-output.md`, `templates/state-capsule.md`, and `templates/self-review.md`.

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

If the task lacks readable requirement sources, ask the Project Agent or Human for them, or produce a packet request using `templates/project-context-packet.md`.

For normal use, accept the conversation-first input in `references/io-contract.md`. Do not require the Human or Project Agent to prebuild live reference research, Evidence Board, Reference Decision Matrix, `request_type`, or no-mutation constraints.

Minimum Project Context Packet fields:
- project_id
- target_screen
- request_type
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
- `references/io-contract.md`: Conversation-first input and fixed output contract.
- `references/request-types.md`: Internal intent labels and outputs.
- `references/project-context-packet.md`: Context packet schema and intake rules.
- `references/reference-decision-matrix.md`: Required Lazyweb/Mobbin reference research and adoption decisions.
- `references/visual-fidelity-contract.md`: Contract structure for image/reference to UI implementation.
- `references/hard-fail-rules.md`: Non-negotiable visual fail conditions.
- `references/score-cap-rules.md`: Score cap rubric.
- `references/calibration-case-schema.md`: Project-local calibration case schema.
- `references/multi-agent-orchestration.md`: Multi-agent handoff/review/rework contract.
- `templates/state-capsule.md`: Conversation state handoff shape.
- `templates/self-review.md`: CXDG guardrail checklist.
- `templates/version-report.md`: Plugin version and CHANGELOG report shape.
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
