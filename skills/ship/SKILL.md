---
name: ship
description: Prepare a branch for release or handoff with disciplined final checks. Use when implementation is done and you need a release-minded pass over validation, documentation, branch state, and delivery readiness without guessing or skipping the boring last mile.
---

# Ship

Use this skill at the end of the implementation cycle, not at the idea stage.

## Workflow
1. Confirm branch state.
   - Identify the current branch.
   - Respect repo rules for protected branches, atomic commits, and merge restrictions.
   - Never assume `main` operations are allowed.
2. Verify code readiness.
   - Run the relevant tests, linters, and build checks.
   - Surface missing validation rather than hand-waving past it.
3. Verify review readiness.
   - Check whether the diff is coherent, documented, and scoped well enough for handoff.
4. Sync supporting materials.
   - Update docs or examples if the change requires it.
   - Call out environment variable changes explicitly.
5. Prepare the handoff.
   - Summarize what changed.
   - Summarize what was verified.
   - Summarize what still needs human action.

## What this skill is for
- final branch readiness before push
- release-minded validation
- preparing a clean implementation summary
- ensuring docs and checks are not forgotten

## What this skill is not for
- deciding product scope
- large refactors during release prep
- unauthorized branch merges or pushes to protected branches

## Guardrails
- Respect repository-specific branch rules.
- If verification cannot be run, say exactly what is missing.
- If the branch is not actually ready, say so plainly.
