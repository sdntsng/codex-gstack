---
name: plan-eng-review
description: Turn an idea or product plan into a buildable technical plan. Use when architecture, system boundaries, data flow, failure modes, background jobs, trust boundaries, or testing strategy need to be nailed down before implementation starts.
---

# Plan Eng Review

Use this skill after the product direction is clear and before the implementation starts to sprawl.

## Workflow
1. Read the request or product plan.
2. Identify the system shape.
   - main components
   - boundaries
   - synchronous vs asynchronous work
   - important state transitions
3. Identify risk.
   - failure modes
   - retries and idempotency
   - data integrity
   - trust boundaries
   - operational complexity
4. Define the implementation spine.
   - key interfaces
   - storage model
   - background work
   - observability needs
5. Define the test plan.
   - unit coverage
   - integration coverage
   - browser or end-to-end checks where needed
6. Produce a buildable plan.

## Output expectations
Return:
- architecture summary
- major components and boundaries
- edge cases and failure handling
- test strategy
- recommended implementation order

## Guardrails
- Do not write code here.
- Force ambiguity into the open instead of smoothing past it.
- Prefer a plan that is boring to build over one that is clever but fragile.
