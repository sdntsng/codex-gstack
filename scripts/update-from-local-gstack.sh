#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="${1:-$ROOT/../knowledge-base/gstack}"
python3 "$ROOT/scripts/sync_from_gstack.py" status --source "$SOURCE"
python3 "$ROOT/scripts/sync_from_gstack.py" scaffold-new --source "$SOURCE"
