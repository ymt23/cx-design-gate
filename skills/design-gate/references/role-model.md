# Role Model

## Human
Own intent, acceptance, release tradeoffs, and final adoption. Human should not have to repeat project facts when the Project Agent can collect them.

Human decides:
- Product objective and priority.
- Non-negotiable experience rules.
- Final pass, rework, or stop.
- Whether a borderline result is acceptable for the current release.

## Project Agent
Collect project truth and prepare the Project Context Packet. The Project Agent must cite source paths and avoid inventing missing requirements.

Project Agent collects:
- Repo instructions and policies.
- Screen requirements.
- Design principles and tokens.
- Current implementation scope.
- Reference assets.
- Active calibration cases relevant to the target screen.

Project Agent does not have to prebuild live reference research, Evidence Board, Reference Decision Matrix, design proposals, or `request_type`. For normal use, Project Agent can pass short Human direction plus requirement paths. Design Gate infers intent, applies default no-mutation rules, checks default calibration, performs Lazyweb/Mobbin lane research, and blocks if required input or reference sources are unavailable.

## Architect CX
Convert requirements and references into implementation-ready contracts. Architect CX defines layer separation, component responsibilities, state coverage, and hard gates before implementation.

Architect CX must not create a new screen proposal or contract from requirements and calibration alone. It first needs Lazyweb Lane, Mobbin Lane, Evidence Board, Reference Decision Matrix, and Synthesis Lane. It uses CX image generation only as purpose-based concept evidence, not as a replacement for live references.

## Designer CX / Design Gate
Review visible UI. Designer CX must judge from the screenshot, video, simulator state, and contract, not from implementer claims.

Designer CX must fail:
- unreadable primary text
- broken grids/lists/cards
- hidden core controls
- content distorted to avoid persistent overlays
- self-report that contradicts the screenshot

## Implementer CX
Implement from the contract and return evidence. Implementer CX does not own final visual pass/fail.

Implementer CX returns:
- changed files
- build/test result
- screenshot or recording
- known deviations
- unresolved risks

Implementer CX must not declare final visual pass. Designer CX / Design Gate owns visual acceptance.

## MCP / Reference Services
MCP services such as Lazyweb or Mobbin provide references, flows, screenshots, and research material. They do not decide product fit, implementation acceptance, or visual pass.
