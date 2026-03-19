#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'
MAPPINGS_PATH = ROOT / 'mappings' / 'skills.json'


def fail(message: str) -> None:
    print(f'ERROR: {message}')
    sys.exit(1)


def main() -> None:
    if not SKILLS_DIR.exists():
        fail('skills directory missing')
    if not MAPPINGS_PATH.exists():
        fail('mappings/skills.json missing')

    data = json.loads(MAPPINGS_PATH.read_text())
    if 'mapped_skills' not in data or not isinstance(data['mapped_skills'], list):
        fail('mapped_skills must be a list')

    for item in data['mapped_skills']:
        target = item['target']
        skill_dir = SKILLS_DIR / target
        if not skill_dir.exists():
            fail(f'mapped target missing: {target}')
        if not (skill_dir / 'SKILL.md').exists():
            fail(f'SKILL.md missing for {target}')
        if not (skill_dir / 'agents' / 'openai.yaml').exists():
            fail(f'agents/openai.yaml missing for {target}')

    print('Repo structure looks valid.')


if __name__ == '__main__':
    main()
