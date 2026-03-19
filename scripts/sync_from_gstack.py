#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_SOURCE = Path(__file__).resolve().parents[2] / 'knowledge-base' / 'gstack'
REPO_ROOT = Path(__file__).resolve().parents[1]
MAPPINGS_PATH = REPO_ROOT / 'mappings' / 'skills.json'
SKILLS_DIR = REPO_ROOT / 'skills'
CATALOG_DIR = REPO_ROOT / 'catalog'
SCAFFOLDS_DIR = REPO_ROOT / 'scaffolds'


def load_mappings() -> dict:
    return json.loads(MAPPINGS_PATH.read_text())


def parse_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text()
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    data = {}
    if not m:
        return data
    block = m.group(1)
    for line in block.splitlines():
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def discover_gstack_skills(source_root: Path) -> list[dict]:
    skills = []
    for skill_md in sorted(source_root.glob('*/SKILL.md')):
        frontmatter = parse_frontmatter(skill_md)
        skills.append({
            'source': skill_md.parent.name,
            'path': str(skill_md),
            'name': frontmatter.get('name', skill_md.parent.name),
            'description': frontmatter.get('description', '').replace('|', '').strip()
        })
    return skills


def write_status(source_root: Path) -> Path:
    mappings = load_mappings()['mapped_skills']
    mapped = {item['source']: item for item in mappings}
    rows = []
    discovered = discover_gstack_skills(source_root)
    for item in discovered:
        if item['source'] in mapped:
            rows.append((item['source'], mapped[item['source']]['target'], mapped[item['source']]['category'], 'mapped'))
        else:
            rows.append((item['source'], '-', '-', 'unmapped'))
    CATALOG_DIR.mkdir(exist_ok=True)
    out = CATALOG_DIR / 'gstack-sync-status.md'
    lines = [
        '# gstack sync status',
        '',
        f'Source: `{source_root}`',
        '',
        '| gstack skill | codex skill | category | status |',
        '|---|---|---|---|'
    ]
    for row in rows:
        lines.append(f'| `{row[0]}` | `{row[1]}` | `{row[2]}` | {row[3]} |')
    out.write_text('\n'.join(lines) + '\n')
    return out


def scaffold_new(source_root: Path) -> list[Path]:
    mappings = load_mappings()['mapped_skills']
    mapped_sources = {item['source'] for item in mappings}
    created = []
    for item in discover_gstack_skills(source_root):
        source = item['source']
        if source in mapped_sources:
            continue
        slug = source
        skill_dir = SCAFFOLDS_DIR / slug
        if skill_dir.exists():
            continue
        (skill_dir / 'agents').mkdir(parents=True, exist_ok=True)
        description = item['description'] or f'Codex scaffold for the upstream gstack skill `{source}`. Use when porting or adapting that workflow into a Codex-native skill.'
        skill_md = f'''---
name: {slug}
description: Codex scaffold derived from the upstream gstack skill `{source}`. Use when adapting that workflow into a Codex-native skill and the final behavior has not been fully curated yet.
---

# {slug}

Source skill: `{source}`
Source file: `{item['path']}`

## Intent captured from gstack
{description}

## Porting notes
- Read the source gstack skill before using this scaffold in production.
- Replace Claude-specific tooling and boilerplate with Codex-native instructions.
- Tighten the trigger description before publishing.
- Add references only if they materially improve repeatability.
'''
        openai_yaml = f'''interface:\n  display_name: "{slug}"\n  short_description: "Scaffolded Codex port of {source}"\n  default_prompt: "Use ${slug} to adapt the upstream gstack workflow into a Codex-native version."\n'''
        (skill_dir / 'SKILL.md').write_text(skill_md)
        (skill_dir / 'agents' / 'openai.yaml').write_text(openai_yaml)
        created.append(skill_dir)
    return created


def install_links(target_dir: Path) -> list[str]:
    linked = []
    target_dir.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        link = target_dir / skill_dir.name
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(skill_dir)
        linked.append(skill_dir.name)
    return linked


def main() -> None:
    parser = argparse.ArgumentParser(description='Sync and scaffold Codex skills from gstack.')
    parser.add_argument('command', choices=['status', 'scaffold-new', 'install'])
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--target', type=Path, default=Path.home() / '.codex' / 'skills')
    args = parser.parse_args()

    if args.command == 'status':
        out = write_status(args.source)
        print(out)
    elif args.command == 'scaffold-new':
        created = scaffold_new(args.source)
        write_status(args.source)
        for path in created:
            print(path)
    elif args.command == 'install':
        for name in install_links(args.target):
            print(name)


if __name__ == '__main__':
    main()
