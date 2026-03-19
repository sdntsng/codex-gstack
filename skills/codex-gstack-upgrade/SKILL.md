---
name: codex-gstack-upgrade
description: Upgrade or refresh a local codex-gstack installation when the skill pack has changed upstream. Use when a user wants to update their installed codex-gstack repo, refresh symlinks into `~/.codex/skills`, or reconcile their local install with the latest curated skills.
---

# Codex Gstack Upgrade

Use this skill to update a local `codex-gstack` installation safely.

## Workflow
1. Identify the install type.
   - local git checkout
   - cloned public repo
   - symlinked skills into `~/.codex/skills`
2. Inspect current state.
   - current branch
   - remotes
   - local modifications
   - whether the installed skills already point at the intended repo
3. Choose the least destructive update path.
   - fetch and fast-forward when safe
   - refresh local symlinks when the repo is already current
   - stop and surface conflicts if local changes would be overwritten
4. Reinstall or relink the skills if needed.
5. Verify the updated skills are visible in `~/.codex/skills`.

## Good use cases
- updating a cloned `codex-gstack` repo
- refreshing symlinked Codex skills after pulling changes
- checking whether a local install is stale

## Output expectations
Return:
- install type detected
- update path used
- whether skill links were refreshed
- any local changes or conflicts that blocked a clean update

## Guardrails
- Do not overwrite local edits silently.
- Prefer fast-forward updates over resets.
- Be explicit when manual conflict resolution is required.
