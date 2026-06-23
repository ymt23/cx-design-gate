# Hard Fail Rules

Apply these before scoring. A hard fail means the result cannot be accepted as a visual pass even if build and tests succeed.

## Visual Readability

Fail if primary text is unreadable, hidden, clipped, too compressed, or visually too small at screenshot scale.

Fail if a report says text is visible but the screenshot shows it hidden or unreadable.

## Component Structure

Fail if the target grid/list/card structure is broken, even when individual constraints technically fit.

Fail if a card/list/grid item cannot display its required title and supporting metadata naturally.

## Layer Separation

Fail if persistent controls deform scroll-content item internals.

Fail if a floating CTA, tab bar, toolbar, HUD, or sticky action bar causes card text, item dimensions, grid spacing, or row layout to be altered away from the component's own design.

## Evidence Integrity

Fail if implementation self-report contradicts screenshot evidence.

Fail if build/test success is used as the main proof of visual quality.

Fail if a required screenshot, recording, or simulator check is missing for a visual decision.

## Scope Integrity

Fail if implementation changes forbidden areas to make the visual problem disappear.

Fail if a rework modifies unrelated screen regions without approval.
