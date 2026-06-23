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

## Architect CX
Convert requirements and references into implementation-ready contracts. Architect CX defines layer separation, component responsibilities, state coverage, and hard gates before implementation.

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

## MCP / Reference Services
MCP services such as Lazyweb or Mobbin provide references, flows, screenshots, and research material. They do not decide product fit, implementation acceptance, or visual pass.
