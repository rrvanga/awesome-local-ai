#!/usr/bin/env bash
# Daily drip: move a few backlog entries into the README and commit.
# Silent (exit 0, no output) when the backlog is empty.
set -euo pipefail
cd "$(dirname "$0")/.."
out=$(python3 scripts/drip.py)
[ -z "$out" ] && exit 0
git add README.md backlog.json
git commit -q -m "docs: drip curated entries from backlog"
git push -q
echo "$out"
