# Generic Fail Case: Overlay Deforms Grid

Verdict: fail

Pattern:
- A persistent floating control overlaps a scroll-content grid.
- The implementer attempts to avoid overlap by shrinking text, changing item insets, or reducing usable card space.
- The grid technically fits, but item information becomes unreadable or unnatural.

Hard fail:
Persistent controls must not deform scroll-content item internals.

Reusable lesson:
Build grid/list/card items as normal scroll content first. Handle persistent overlay interaction with scroll padding, safe areas, z-index, or explicit acceptance rules, not by damaging item layout.
