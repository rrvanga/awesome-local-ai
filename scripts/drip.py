#!/usr/bin/env python3
"""Drip N entries from backlog.json into the right category in README.md.

Silent (no stdout, exit 0) when the backlog is empty, so the cron watchdog
doesn't ping the user on days with nothing to publish.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
BACKLOG = ROOT / "backlog.json"
N = 3


def main() -> int:
    if not BACKLOG.exists():
        return 0
    try:
        backlog = json.loads(BACKLOG.read_text())
    except (json.JSONDecodeError, OSError):
        return 0

    if not backlog:
        return 0

    take, rest = backlog[:N], backlog[N:]
    text = README.read_text()

    by_cat: dict[str, list[dict]] = {}
    for e in take:
        by_cat.setdefault(e["category"], []).append(e)

    added: list[dict] = []
    for cat, entries in by_cat.items():
        heading = f"## {cat}"
        idx = text.find(heading)
        if idx == -1:
            print(f"warn: category '{cat}' not in README", file=sys.stderr)
            continue
        # Insert at the end of this category's section (before the next heading).
        next_h = text.find("\n## ", idx + 1)
        insert_at = len(text) if next_h == -1 else next_h
        bullets = "\n".join(
            f"- [{e['name']}]({e['url']}) — {e['desc']}" for e in entries
        )
        text = text[:insert_at] + "\n" + bullets + "\n" + text[insert_at:]
        added.extend(entries)

    if not added:
        return 0

    README.write_text(text)
    BACKLOG.write_text(json.dumps(rest, indent=2) + "\n")

    print(f"added {len(added)} entr{'y' if len(added) == 1 else 'ies'} to awesome-local-ai:")
    for e in added:
        print(f"  - {e['name']}  [{e['category']}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
