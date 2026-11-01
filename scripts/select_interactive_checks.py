#!/usr/bin/env python3
"""Select registered pilot pages; never claim coverage for unregistered articles."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'tests/browser/pilot.json'


def select(changed, registry):
    shared = any(p.startswith(('assets/', '_includes/', '_layouts/', 'tests/browser/'))
                 or p in {'_config.yml', 'Gemfile', 'Gemfile.lock',
                          'scripts/check_interactive_demos.py',
                          'scripts/select_interactive_checks.py',
                          '.github/workflows/interactive-demo-test.yml'} for p in changed)
    sources = {v['source'] for v in registry.values()}
    return {
        'pages': [slug for slug, item in registry.items() if shared or item['source'] in changed],
        'uncovered_articles': [p for p in changed if p.startswith('pages/') and p not in sources],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base')
    parser.add_argument('--head', default='HEAD')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    registry = json.loads(REGISTRY.read_text())
    if args.all or not args.base or set(args.base) == {'0'}:
        result = {'pages': list(registry), 'uncovered_articles': []}
    else:
        changed = subprocess.check_output(
            ['git', 'diff', '--name-only', args.base, args.head, '--'], cwd=ROOT, text=True).splitlines()
        result = select(changed, registry)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
