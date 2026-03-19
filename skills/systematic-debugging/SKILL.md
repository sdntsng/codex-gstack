---
name: systematic-debugging
description: Investigate bugs with a root-cause-first workflow. Use when a user asks to debug, diagnose, trace an issue, explain a failure, or fix broken behavior where the actual cause is not yet known.
---

# Systematic Debugging

Use this skill to avoid guess-fix cycles. Investigate first, then change code.

## Workflow
1. Define the symptom.
   - Capture the failing behavior, error text, and reproduction path.
   - Separate observed facts from guesses.
2. Trace the execution path.
   - Identify the relevant entry point, state changes, dependencies, and outputs.
   - Read the smallest code slice that can explain the failure.
3. Form a root-cause hypothesis.
   - State one concrete explanation of why the bug happens.
   - Prefer a falsifiable claim over a broad suspicion.
4. Verify the hypothesis.
   - Reproduce the issue.
   - Add inspection, logging, or targeted checks only as needed.
   - If the evidence does not support the hypothesis, discard it and revisit the trace.
5. Implement the smallest fix that addresses the root cause.
   - Avoid opportunistic refactors.
   - Keep the blast radius tight.
6. Prove the fix.
   - Add or update a regression test when possible.
   - Re-run the relevant checks.
   - Confirm the original symptom is gone.

## Three-strike rule
If three consecutive hypotheses fail, stop escalating guesses. Summarize:
- what was observed
- what was ruled out
- what is still unknown
- what deeper access or context is required

## Preferred outputs
Return:
- symptom summary
- root-cause hypothesis
- evidence used to confirm it
- fix applied
- verification performed
- residual risk, if any

## Guardrails
- No code changes before a plausible causal explanation exists.
- No "quick fix for now" logic unless the user explicitly asks for a temporary mitigation.
- If the issue is environment-specific, say so clearly rather than pretending the code is settled.
