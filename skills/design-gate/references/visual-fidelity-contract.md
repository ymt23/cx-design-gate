# Visual Fidelity Contract

Use this contract to convert requirements and references into a UI implementation target before code changes.

## Contract Sections

1. Screen Purpose
2. Source References
3. Adopted Elements
4. Rejected Elements
5. Transformed Elements
6. Information Hierarchy
7. Layer Model
8. Layout Regions
9. Component Breakdown
10. Visual Tokens
11. Text and Readability Rules
12. State Coverage
13. Animation and Polish Scope
14. Implementation Scope
15. Simulator Review Criteria
16. Hard Fail Rules
17. Score Caps
18. Open Risks

## Layer Model Requirements

Always label persistent controls and scroll content separately.

Persistent controls include nav bars, tab bars, floating CTAs, toolbars, HUDs, and sticky action bars.

Scroll content includes carousels, cards, lists, grids, forms, feeds, and item panels.

Persistent controls may overlay content, but they must not deform scroll-content internals. If overlap affects final rows, use scroll padding or acceptance criteria rather than changing each card's content layout.
