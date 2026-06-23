# CX Design Gate

CX Design Gate is a Codex plugin and skill for AI-driven UI design workflows. It separates project truth, visual contracts, implementation handoff, and screenshot-based design review so implementation agents do not treat build success or layout constraints as visual acceptance.

## Status

Early OSS plugin scaffold. The public API and workflow files may change before the first stable release.

## What This Plugin Provides

- A `design-gate` Codex skill for visual fidelity review workflows.
- Project Context Packet requirements for project-specific design truth.
- Visual Fidelity Contract structure for concept art, screenshots, Lazyweb/Mobbin references, and implemented UI reviews.
- Hard Fail and Score Cap rules for preventing optimistic visual scoring.
- Role separation between Human, Project Agent, Designer CX, Architect CX, Implementer CX, and MCP reference services.
- Multi-agent orchestration guidance for separating implementation and visual review.
- Generic calibration examples that avoid project-specific data.

## Core Principle

Project-specific product truth stays in the project. This repository provides the reusable Design Gate procedure, schemas, prompts, and generic calibration patterns.

Project-local calibration cases should live outside this OSS package, for example:

```text
repo/.codex/cx-design-gate/calibration/
  index.md
  cases/
    <case-id>.md
```

## Repository Layout

```text
.codex-plugin/plugin.json
skills/design-gate/SKILL.md
skills/design-gate/references/
skills/design-gate/templates/
examples/generic/
```

## Skill Entry Point

Use the skill as `design-gate` in Codex. The skill expects a Project Context Packet or enough information to request one.

When installed through the local marketplace, the skill appears as `cx-design-gate:design-gate` in new Codex chats.

Typical flow:

```text
1. Project Agent collects project docs, screen requirements, references, and active calibration cases.
2. Design Gate creates or reviews a Visual Fidelity Contract.
3. Implementer CX builds from the contract and returns screenshots/build evidence.
4. Designer CX applies hard fail rules and score caps.
5. Human makes the final pass/rework/stop decision.
```

## Validation

The plugin and skill were validated with the bundled Codex plugin/skill validation scripts. The local environment did not include PyYAML, so validation was run with a temporary local YAML shim instead of installing dependencies into the plugin.

The local plugin was also confirmed in a new Codex chat: `cx-design-gate:design-gate` appeared in Available skills and `SKILL.md` loaded successfully.

## License

MIT. See [LICENSE](LICENSE).
