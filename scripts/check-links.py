#!/usr/bin/env python3
"""Check every URL in README.md for link rot. Read-only: never edits the README.

The job of this script is to *find* broken links, not to guess replacements —
a dead link's fix (new URL? retired project?) is a judgement call, so the
script reports and exits non-zero only on a hard schema problem, not on 404s.

Usage:
  python3 scripts/check-links.py           # human-readable report
  python3 scripts/check-links.py --quiet   # print only broken links
  python3 scripts/check-links.py --json    # machine-readable

Exit codes:
  0 = all links reachable
  1 = one or more links broken (see report)
  2 = could not read README.md
"""
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

# Markdown link targets and bare URLs. Strip trailing punctuation that
# markdown prose commonly glues onto a URL.
URL_RE = re.compile(r'https?://[^\s()<>\[\]"\']+')

UA = "Mozilla/5.0 (compatible; awesome-local-ai link check)"
# Some hosts reject HEAD outright, so we retry those with GET.
HEAD_OK = {200, 204, 301, 302, 303, 307, 308}

CTX = ssl.create_default_context()


def probe(url: str) -> tuple[str, int | str]:
    """Return (status_kind, detail) where status_kind is 'ok', 'broken', 'warn'."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={
            "User-Agent": UA,
            "Accept": "*/*",
        })
        try:
            with urllib.request.urlopen(req, timeout=12, context=CTX) as resp:
                if resp.status in HEAD_OK:
                    return ("ok", resp.status)
                return ("warn", resp.status)
        except urllib.error.HTTPError as e:
            # 403/405/429 are usually bot-blocking, not rot — don't cry wolf.
            if method == "GET":
                if e.code in (403, 405, 429):
                    return ("warn", e.code)
                return ("broken", e.code)
        except urllib.error.URLError as e:
            if method == "GET":
                return ("broken", str(e.reason)[:60])
        except Exception as e:  # timeouts, TLS resets, etc.
            if method == "GET":
                return ("warn", type(e).__name__)
    return ("warn", "unknown")


def main() -> int:
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv

    try:
        text = README.read_text(encoding="utf-8")
    except OSError as e:
        print(f"cannot read {README}: {e}", file=sys.stderr)
        return 2

    urls = sorted({u.rstrip(".,;:!") for u in URL_RE.findall(text)})

    with ThreadPoolExecutor(max_workers=12) as pool:
        results = dict(zip(urls, pool.map(probe, urls)))

    broken = {u: d for u, (k, d) in results.items() if k == "broken"}
    warned = {u: d for u, (k, d) in results.items() if k == "warn"}

    if as_json:
        print(json.dumps({
            "total": len(urls),
            "broken": broken,
            "warn": warned,
        }, indent=2))
    else:
        if not quiet:
            print(f"checked {len(urls)} unique URLs in README.md")
        for u, d in sorted(broken.items()):
            print(f"BROKEN {d}  {u}")
        if not quiet:
            for u, d in sorted(warned.items()):
                print(f"  warn {d}  {u}")
            print(f"summary: {len(urls) - len(broken)} ok, "
                  f"{len(broken)} broken, {len(warned)} unverifiable")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
