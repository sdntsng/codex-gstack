---
name: pr-preflight-review
description: Review the current branch before push or PR creation. Use when you need a diff-aware check for scope drift, missing requirements, structural risks, weak tests, or incomplete implementation before asking humans to review the work.
---

# PR Preflight Review

Use this skill before pushing or opening a PR.

## Workflow
1. Detect the intended base branch.
   - Prefer the existing PR base when present.
   - Otherwise use the repo default branch.
2. Inspect stated intent.
   - Read branch name, recent commits, TODOs, or issue context.
   - Summarize what the branch appears to be trying to do.
3. Compare intent to diff.
   - Look for scope creep.
   - Look for missing promised work.
   - Look for obvious test or documentation gaps.
4. Review for structural risk.
   - correctness issues
   - data or trust-boundary risks
   - state and edge-case handling
   - missing cleanup or follow-through
5. Produce findings in severity order.
   - Findings first.
   - Then open questions.
   - Then a short readiness summary.

## What this skill should catch
- unrelated files changed without reason
- partial implementations
- hidden behavior changes without tests
- known risk patterns that CI may miss
- branch not actually ready for external review

## Output expectations
Return:
- base branch used for comparison
- intent summary
- scope check result
- findings ordered by severity
- overall verdict: ready, ready with concerns, or not ready

## Guardrails
- Be skeptical of diff size and blast radius.
- Do not spend time on style nits unless they hide a correctness problem.
- If there are no findings, say that explicitly and mention residual verification gaps.
