---
name: browser-dogfood
description: Run real browser-based product testing with Codex browser tools. Use when you need to open a site, click through flows, verify staging or production behavior, inspect console or network failures, capture screenshots, test responsive layouts, or confirm that a UI change works end to end.
---

# Browser Dogfood

Use this skill to verify product behavior in a real browser instead of inferring from code.

## Workflow
1. Establish the target.
   - Confirm the URL, local dev server, or environment to test.
   - If auth is required, prefer an existing logged-in browser context before asking for credentials.
2. Capture a baseline.
   - Open the page.
   - Take a snapshot of the visible structure.
   - Check console output and failed network requests early.
3. Exercise the flow.
   - Click through the exact user path.
   - Prefer snapshots before and after major actions.
   - For forms, verify validation, success, and failure states.
4. Collect evidence.
   - Save screenshots for important states.
   - Record concrete failures: broken layout, console error, request failure, bad redirect, stale UI, missing state.
5. Conclude with a verdict.
   - State what worked.
   - State what failed.
   - State whether the issue is reproducible and where.

## Default tool choices
- Use Playwright browser tools for most end-to-end testing.
- Use Chrome DevTools tools when you need deeper network, console, DOM, or performance inspection.
- Prefer snapshots over screenshots for navigation and element targeting.
- Use screenshots when visual evidence matters.

## What to check
- Page loads without blocking errors.
- Core interactions work.
- Empty, loading, error, and success states are coherent.
- Responsive layout holds on mobile and desktop when relevant.
- No silent console or network failures are masking a broken experience.

## Output expectations
Return:
- tested URL or flow
- steps executed
- evidence collected
- findings ordered by severity
- pass or fail summary

## Guardrails
- Do not claim a flow works unless you actually executed it.
- Do not rely on screenshots alone when console or network checks are relevant.
- If login blocks progress, say exactly where the flow stopped.
