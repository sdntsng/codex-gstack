---
name: plan-design-review
description: Review a product or feature plan from a design perspective before implementation. Use when a plan needs clearer UX decisions, better interaction-state coverage, stronger hierarchy, more intentional responsiveness, or protection against generic AI-generated design choices.
---

# Plan Design Review

Use this skill before implementation when the design is still in the plan, not yet in the UI.

## Workflow
1. Read the plan or feature brief.
2. Identify missing design decisions.
   - screen hierarchy
   - primary actions
   - loading, error, empty, and success states
   - mobile and desktop behavior
   - accessibility expectations
3. Check whether the plan is specific enough to implement without improvising weak UI.
4. Improve the plan.
   - add missing state coverage
   - sharpen information hierarchy
   - remove generic or lazy design language
   - define the important interactions explicitly
5. End with a design-ready verdict.

## What this skill should catch
- "clean modern UI" with no actual design choices
- missing empty, error, or loading states
- no responsive intent beyond stacking things on mobile
- unclear content hierarchy
- generic card-grid thinking where the product needs more intent
- plans that assume polish will happen later

## Output expectations
Return:
- design quality summary of the plan
- missing decisions
- recommended changes
- revised design guidance ready for implementation

## Guardrails
- Do not implement the UI here.
- The goal is a better plan, not a design essay.
- Be specific enough that an engineer or designer could build from it without guessing.
