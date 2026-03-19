---
name: web-qa-fix
description: Run a structured QA pass on a web app, fix verified bugs, add regression coverage where appropriate, and re-test the affected flows. Use when the goal is to test and repair a web experience rather than only report issues.
---

# Web QA Fix

Use this skill when QA should lead directly to implementation work.

## Workflow
1. Scope the test pass.
   - Confirm environment and primary flows.
   - Identify whether the user wants a quick pass or a broader sweep.
2. Test in a real browser.
   - Reproduce issues with clear evidence.
   - Do not fix unverified bugs.
3. Prioritize.
   - Fix critical and high severity issues first.
   - Medium and low severity issues are optional if time or scope is constrained.
4. Fix one logical issue at a time.
   - Keep changes tight.
   - Add a regression test when the stack supports it and the bug is testable.
   - Re-run the affected flow after each fix.
5. Commit each fix atomically when working in a git repo with commit requirements.
6. Summarize the final state.
   - What was tested
   - What was fixed
   - What remains
   - Whether the tested scope is ready to ship

## Severity guidance
- Critical: fix immediately.
- High: fix in the same pass unless blocked.
- Medium: fix if straightforward and verified.
- Low: fix only if clearly in scope.

## Output expectations
Return:
- tested flows
- bugs found
- fixes applied
- verification steps
- remaining concerns

## Guardrails
- Do not batch unrelated fixes into one change.
- Do not mark an issue fixed without re-running the affected flow.
- If a fix requires product judgment or broad refactoring, stop and surface the tradeoff.
