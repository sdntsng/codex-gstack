# Porting Guide

## Goal
Turn strong upstream `gstack` workflows into concise Codex-native skills.

## Keep
- role clarity
- explicit workflow phases
- real-world testing and verification habits
- decision points that reduce bad automation

## Remove
- repeated preambles
- upgrade choreography
- contributor-mode logs
- Claude-specific tool references
- hardcoded `.claude/skills/...` paths
- motivational filler repeated in every skill

## Good Codex ports usually have
- a sharp trigger description
- a short workflow section
- explicit output expectations
- a small number of guardrails

## Bad ports usually have
- giant copied markdown bodies
- environment-specific setup that does not apply to Codex
- ambiguous invocation criteria
- too much philosophy and too little procedure

## Fast path for new upstream skills
When a new upstream skill appears:
1. run `sync_from_gstack.py scaffold-new`
2. inspect the generated scaffold under `scaffolds/`
3. decide whether it belongs in the curated pack
4. if yes, create a polished version under `skills/`
5. add the mapping entry
