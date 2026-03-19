---
name: web-qa-report
description: Run a structured QA pass on a web app and return a prioritized bug report without making code changes. Use when you need report-only testing for a local app, staging site, production site, or a specific user flow.
---

# Web QA Report

Use this skill for report-only QA. Test the product, gather evidence, and return findings without editing code.

## Workflow
1. Define scope.
   - Confirm the environment, routes, and flows to test.
   - If no scope is given, cover the main happy path plus obvious error states.
2. Run the QA pass.
   - Use real browser interaction.
   - Check visual behavior, form behavior, console errors, network failures, and broken states.
3. Classify findings.
   - Critical: blockers, crashes, data loss, auth failure, dead primary paths.
   - High: major feature breakage or misleading behavior.
   - Medium: degraded UX, partial failures, confusing state handling.
   - Low: polish, copy, spacing, or edge-case issues.
4. Attach evidence.
   - Include route, action, observed result, and screenshot or log evidence where useful.
5. End with ship readiness.
   - State whether the tested scope is shippable.
   - List the blockers separately.

## Output format
Return findings in severity order. For each finding include:
- title
- severity
- reproduction steps
- expected behavior
- actual behavior
- evidence

## Guardrails
- Do not suggest fixes as if they were verified.
- Do not say "looks good" unless meaningful flows were actually exercised.
- Distinguish confirmed bugs from suspected risks.
