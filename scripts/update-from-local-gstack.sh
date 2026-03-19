#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 /path/to/gstack" >&2
  exit 1
fi
SOURCE="$1"
python3 "$ROOT/scripts/sync_from_gstack.py" status --source "$SOURCE"
python3 "$ROOT/scripts/sync_from_gstack.py" scaffold-new --source "$SOURCE"
