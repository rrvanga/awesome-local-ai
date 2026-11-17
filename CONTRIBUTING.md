# Contributing

Thanks for helping make this list better. The bar is **genuinely useful for running AI locally** — not just "an AI tool that exists."

## How to add an entry

1. **Fork** this repo.
2. Add your entry under the right category in `README.md`, keeping alphabetical-ish order.
3. Format: `- [Name](URL) — One sentence on what it is and *why it matters for local AI*.`
4. Open a PR with a short description of what you added and why.

## What belongs

- Open-source or free tools that run inference locally.
- Open-weight models with a clear download path.
- Quantization, optimization, and evaluation tooling.
- Hardware/VRAM guides with real, reproducible math.

## What doesn't belong

- Cloud-only APIs (that's what [llmcost](https://github.com/rrvanga/llmcost) tracks, if you're curious).
- Dead links or abandoned projects (check the last commit first).
- Vague "this AI thing is cool" entries with no local-AI angle.

## Checking links before you submit

Dead links are the main way a curated list rots. Before opening a PR, run:

```bash
python3 scripts/check-links.py
```

It probes every URL in `README.md` concurrently and reports `BROKEN` (hard 404/410/DNS failure) separately from `warn` (403/405/429/timeout, which usually means the site blocks bots rather than that the project is gone). Exit code is `1` if anything is genuinely broken, so it also works as a CI gate. To check only what you added:

```bash
python3 scripts/check-links.py --quiet
```

## The maintainer's backlog

The repo also grows via a daily drip from a private backlog of vetted entries. If you want a project included but don't want to PR it, open an issue and tag it `backlog-request`.
