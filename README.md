# codex-gstack

Codex-native workflow skills inspired by `gstack`.

`codex-gstack` is a public skill pack for Codex users who want structured specialist workflows instead of ad hoc prompting. It ports the highest-value ideas from `gstack` into concise, Codex-first skills and adds a lightweight sync pipeline so new upstream `gstack` skills can be detected and scaffolded quickly.

## What this repo includes

### Core engineering skills
- `browser-dogfood`
- `systematic-debugging`
- `web-qa-report`
- `web-qa-fix`
- `pr-preflight-review`
- `doc-sync-after-change`
- `ship`

### Founder and planning skills
- `office-hours`
- `plan-ceo-review`
- `plan-eng-review`

### Design and execution skills
- `design-consultation`
- `design-review-live`
- `project-retro`

## Why this exists
`gstack` has strong workflow ideas, but it is optimized for Claude Code and carries a lot of Claude-specific ceremony. This repo focuses on the reusable part:
- specialist roles
- real browser testing
- root-cause-first debugging
- diff-aware review
- documentation sync
- product and planning reviews

The goal is not to mirror upstream line-for-line. The goal is to keep the workflow value and remove the environment-specific overhead.

## Install locally

To link all skills from this repo into your local Codex setup:

```bash
python3 scripts/sync_from_gstack.py install --target ~/.codex/skills
```

That creates symlinks from this repo's `skills/` directory into `~/.codex/skills`.

## Track upstream gstack changes

If you have a local `gstack` checkout available, generate a fresh sync report and scaffold any newly discovered skills:

```bash
./scripts/update-from-local-gstack.sh ../knowledge-base/gstack
```

Or run the steps explicitly:

```bash
python3 scripts/sync_from_gstack.py status --source ../knowledge-base/gstack
python3 scripts/sync_from_gstack.py scaffold-new --source ../knowledge-base/gstack
```

This will:
- refresh `catalog/gstack-sync-status.md`
- detect upstream skills not yet mapped
- scaffold starter Codex skill folders under `scaffolds/`

## Repo structure

```text
skills/                  curated Codex-native skills
mappings/skills.json     upstream gstack -> codex-gstack mapping
catalog/                 generated status output
scaffolds/               auto-created starter ports for new upstream skills
scripts/                 sync, install, and validation tooling
docs/                    porting notes and contributor docs
```

## Current porting model

Mapped upstream skills become curated Codex skills.

Unmapped upstream skills are not ignored. They are scaffolded automatically so a contributor can finish the port quickly instead of starting from zero.

That means this repo supports both:
- a stable curated skill pack
- a fast path for adopting new upstream `gstack` skills

## Validation

Run:

```bash
python3 scripts/check_repo.py
```

This checks:
- every curated skill has `SKILL.md`
- every curated skill has `agents/openai.yaml`
- the mapping file is valid JSON
- every mapped target exists in `skills/`

## Contribution workflow

1. Add or refine a skill in `skills/`
2. Run `python3 scripts/check_repo.py`
3. If syncing from upstream, run `python3 scripts/sync_from_gstack.py status --source <path>`
4. Commit one logical change at a time

Detailed guidance lives in `CONTRIBUTING.md` and `docs/porting-guide.md`.

## License

MIT
