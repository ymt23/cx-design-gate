# Visual Fidelity Contract

Use this contract to convert requirements and references into a UI implementation target before code changes.

## Contract Sections

1. Screen Purpose
2. Evidence Board
3. Lazyweb Lane
4. Mobbin Lane
5. Reference Decision Matrix
6. Synthesis Lane
7. Source References
8. Adopted Elements
9. Rejected Elements
10. Transformed Elements
11. Information Hierarchy
12. Layer Model
13. Layout Regions
14. Component Breakdown
15. Visual Tokens
16. Text and Readability Rules
17. State Coverage
18. Animation and Polish Scope
19. Implementation Scope
20. Simulator Review Criteria
21. Hard Fail Rules
22. Score Caps
23. Open Risks
24. State Capsule
25. CXDG Self-Review

For new design directions or contracts, create Lazyweb Lane, Mobbin Lane, Evidence Board, Reference Decision Matrix, and Synthesis Lane before filling Source References. Source References must cite live Lazyweb and Mobbin results unless the workflow is explicitly blocked.

## Layer Model Requirements

Always label persistent controls and scroll content separately.

Persistent controls include nav bars, tab bars, floating CTAs, toolbars, HUDs, and sticky action bars.

Scroll content includes carousels, cards, lists, grids, forms, feeds, and item panels.

Persistent controls may overlay content, but they must not deform scroll-content internals. If overlap affects final rows, use scroll padding or acceptance criteria rather than changing each card's content layout.
