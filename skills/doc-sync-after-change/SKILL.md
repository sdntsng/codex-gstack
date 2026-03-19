---
name: doc-sync-after-change
description: Update project documentation after code changes using the actual diff as the source of truth. Use when a feature, workflow, command, path, or architecture detail changed and the docs may now be stale.
---

# Doc Sync After Change

Use this skill after implementation work to bring docs back into alignment.

## Workflow
1. Inspect the diff.
   - Determine what behavior, commands, files, or workflows changed.
2. Discover affected docs.
   - Typical targets: README, architecture docs, setup docs, usage docs, changelog, TODOs, contribution docs.
3. Update factual drift first.
   - commands
   - paths
   - screenshots or examples
   - counts, feature lists, workflow steps
4. Only make narrative changes when required.
   - Avoid gratuitous rewrites.
   - Preserve the document's role and voice.
5. Verify consistency.
   - Make sure the same concept is not described differently across files.
6. Summarize what changed and what still needs human judgment.

## Good use cases
- new feature added
- command renamed
- setup flow changed
- environment variable added or renamed
- architecture changed enough that docs are now inaccurate

## Guardrails
- The diff is the source of truth; do not invent behavior.
- Keep changelog edits surgical.
- If a version bump or release note is subjective, surface it explicitly.
