# Visual Fidelity Contract

Use this contract to convert requirements and references into a UI implementation target before code changes.

## Contract Sections

1. Screen Purpose
2. Evidence Board
3. Reference Decision Matrix
4. Source References
5. Adopted Elements
6. Rejected Elements
7. Transformed Elements
8. Information Hierarchy
9. Layer Model
10. Layout Regions
11. Component Breakdown
12. Visual Tokens
13. Text and Readability Rules
14. State Coverage
15. Animation and Polish Scope
16. Implementation Scope
17. Simulator Review Criteria
18. Hard Fail Rules
19. Score Caps
20. Open Risks

For new design directions or contracts, create the Evidence Board and Reference Decision Matrix before filling Source References. Source References must cite live Lazyweb and Mobbin results unless the workflow is explicitly blocked.

## Layer Model Requirements

Always label persistent controls and scroll content separately.

Persistent controls include nav bars, tab bars, floating CTAs, toolbars, HUDs, and sticky action bars.

Scroll content includes carousels, cards, lists, grids, forms, feeds, and item panels.

Persistent controls may overlay content, but they must not deform scroll-content internals. If overlap affects final rows, use scroll padding or acceptance criteria rather than changing each card's content layout.
