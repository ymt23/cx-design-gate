# Score Cap Rules

Use score caps after hard fail checks. Caps prevent optimistic scoring when important evidence is missing or partially broken.

- Screenshot missing: max 60.
- Implementer self-score only: max 60.
- Primary component partially broken: max 65.
- Main card shape not visible: max 70.
- Primary CTA role changed: max 70.
- Persistent overlay/content layer separation unclear: max 70.
- Important text visible but cramped or unnaturally compressed: max 75.
- Visual direction strong but component fidelity weak: max 75.
- Build/test pass but visual evidence weak: max 70.

Scoring bands:
- 90-100: Production-quality fidelity with minor polish only.
- 80-89: Strong pass; suitable implementation base.
- 75-79: Pass candidate; needs focused polish.
- 70-74: Borderline pass; acceptable only for pipeline validation or low-risk usage.
- 60-69: Rework required.
- Below 60: Fail or wrong approach.
