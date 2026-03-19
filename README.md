# codex-gstack

Codex-native workflow skills inspired by [gstack](https://github.com/garrytan/gstack).

`codex-gstack` is a public skill pack for Codex users who want structured specialist workflows instead of ad hoc prompting. It ports the highest-value ideas from `gstack` into concise, Codex-first skills and ships a lightweight sync pipeline so new upstream `gstack` skills can be detected and scaffolded quickly.

## What you get

### Engineering workflows
- `browser-dogfood` — browser-backed testing, verification, and dogfooding
- `systematic-debugging` — root-cause-first debugging
- `web-qa-report` — report-only QA pass for web apps
- `web-qa-fix` — QA, fix verified bugs, and re-test
- `pr-preflight-review` — branch review before push or PR
- `doc-sync-after-change` — diff-driven documentation sync
- `ship` — release-minded final readiness pass
- `setup-browser-cookies` — establish authenticated browser testing without redoing login manually
- `codex-gstack-upgrade` — refresh a local `codex-gstack` installation safely

### Founder and planning workflows
- `office-hours` — sharpen the product problem before implementation
- `plan-ceo-review` — founder-level product and scope review
- `plan-eng-review` — buildable architecture and execution planning
- `plan-design-review` — design review of the plan before implementation starts

### Design and operating workflows
- `design-consultation` — upfront design direction and system choices
- `design-review-live` — live UI and UX audit
- `project-retro` — retrospective from recent work patterns

## Why this exists

`gstack` has strong workflow ideas, but it is optimized for Claude Code and carries a lot of Claude-specific ceremony. `codex-gstack` focuses on the reusable part:
- specialist roles
- real browser testing
- root-cause-first debugging
- diff-aware review
- documentation sync
- product and planning reviews

The goal is not to mirror upstream line-for-line. The goal is to keep the workflow value and remove the environment-specific overhead.

## Install into Codex

To link all curated skills from this repo into your local Codex setup:

```bash
python3 scripts/sync_from_gstack.py install --target ~/.codex/skills
```

That creates symlinks from this repo's `skills/` directory into `~/.codex/skills`.

## Keep up with upstream gstack

If you have a local clone of upstream `gstack`, refresh the sync report and scaffold any newly discovered upstream skills:

```bash
./scripts/update-from-local-gstack.sh /path/to/gstack
```

Or run the steps explicitly:

```bash
python3 scripts/sync_from_gstack.py status --source /path/to/gstack
python3 scripts/sync_from_gstack.py scaffold-new --source /path/to/gstack
```

This will:
- refresh `catalog/gstack-sync-status.md`
- detect upstream skills not yet mapped
- scaffold starter Codex skill folders under `scaffolds/`

## Current upstream coverage

The current mapping was validated against an external local clone of upstream `gstack`.

- Local `gstack` HEAD: `52f1607`
- Local `gstack` `origin/main`: `50a7cf8`
- Remote upstream checked on 2026-03-19: [garrytan/gstack](https://github.com/garrytan/gstack) (pushed at `2026-03-19T05:38:59Z`)

### Mapping matrix

| Upstream gstack skill | codex-gstack skill | Status |
| --- | --- | --- |
| `browse` | `browser-dogfood` | ported |
| `debug` | `systematic-debugging` | ported |
| `qa-only` | `web-qa-report` | ported |
| `qa` | `web-qa-fix` | ported |
| `review` | `pr-preflight-review` | ported |
| `document-release` | `doc-sync-after-change` | ported |
| `ship` | `ship` | ported |
| `setup-browser-cookies` | `setup-browser-cookies` | ported |
| `gstack-upgrade` | `codex-gstack-upgrade` | ported |
| `office-hours` | `office-hours` | ported |
| `plan-ceo-review` | `plan-ceo-review` | ported |
| `plan-eng-review` | `plan-eng-review` | ported |
| `plan-design-review` | `plan-design-review` | ported |
| `design-consultation` | `design-consultation` | ported |
| `design-review` | `design-review-live` | ported |
| `retro` | `project-retro` | ported |

### Remote upstream delta

The live upstream repo currently has additional top-level skills that are newer than the local imported `gstack` checkout:

| Remote-only gstack skill | codex-gstack status | Notes |
| --- | --- | --- |
| `careful` | not ported | destructive-command safety guardrails |
| `codex` | not ported | Claude-oriented Codex wrapper workflow; needs deeper adaptation |
| `freeze` | not ported | filesystem boundary lock skill |
| `guard` | not ported | combined `careful` + `freeze` safety wrapper |
| `unfreeze` | not ported | clears a prior freeze boundary |

If new upstream skills appear later, `scaffold-new` will generate starter Codex ports automatically. Remote-only skills should be reviewed before porting instead of copied verbatim.

## Repository layout

```text
skills/                  curated Codex-native skills
mappings/skills.json     upstream gstack -> codex-gstack mapping
catalog/                 generated sync status
scaffolds/               starter ports for newly discovered upstream skills
scripts/                 sync, install, and validation tooling
docs/                    porting notes and contributor docs
```

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
4. If new upstream skills appear, run `python3 scripts/sync_from_gstack.py scaffold-new --source <path>`
5. Promote useful scaffolded skills into curated versions under `skills/`
6. Commit one logical change at a time

Detailed guidance lives in `CONTRIBUTING.md` and `docs/porting-guide.md`.

## License

MIT
