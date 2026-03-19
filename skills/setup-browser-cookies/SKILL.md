---
name: setup-browser-cookies
description: Prepare browser-based QA against authenticated pages by reusing an existing logged-in browser session or importing cookies into the testing context. Use when browser testing is blocked by auth and you need a practical path to test logged-in flows.
---

# Setup Browser Cookies

Use this skill when real browser testing is blocked by authentication.

## Workflow
1. Identify the auth requirement.
   - Which site or environment needs login?
   - Is an existing logged-in browser session already available?
2. Prefer the least fragile approach.
   - Reuse the existing browser context if possible.
   - If that is not enough, import or establish auth state in the browser automation context.
3. Validate access.
   - Open the target page.
   - Confirm the session is authenticated.
   - Check that the relevant protected route is actually reachable.
4. Hand control back to the calling browser or QA workflow.

## Good use cases
- testing staging or production pages behind auth
- verifying dashboards or admin tools that require login
- preserving a user's existing browser session for QA work

## Output expectations
Return:
- target site or environment
- auth method used
- whether authenticated access was verified
- any remaining blockers

## Guardrails
- Prefer session reuse over asking for raw credentials.
- Be explicit if authentication could not be established.
- Do not claim protected flows are testable until an authenticated page was actually reached.
