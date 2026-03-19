# Contributing

## Principles
- Keep skills concise.
- Keep Codex-native instructions in `skills/`.
- Do not copy Claude-specific boilerplate from upstream `gstack`.
- Preserve workflow value, not source formatting.

## When upstream gstack changes
1. Pull or update your local `gstack` checkout.
2. Run:

```bash
python3 scripts/sync_from_gstack.py status --source <gstack-path>
python3 scripts/sync_from_gstack.py scaffold-new --source <gstack-path>
```

3. Review any newly generated folders under `scaffolds/`.
4. Promote the useful ones into curated skills under `skills/`.
5. Update `mappings/skills.json` when a scaffold becomes a curated skill.

## Skill authoring rules
- Frontmatter should be minimal and precise.
- Put detailed knowledge in references only when it materially improves repeatability.
- Prefer workflow instructions over slogans.
- Mention when the skill should stop and surface uncertainty.

## Validation
Run:

```bash
python3 scripts/check_repo.py
```

## Local install
To install or refresh links into your Codex setup:

```bash
python3 scripts/sync_from_gstack.py install --target ~/.codex/skills
```
