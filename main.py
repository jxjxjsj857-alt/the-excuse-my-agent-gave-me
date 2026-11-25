#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun bounty entry.

Writes one line -- the excuse an AI agent hands its human after missing
a deadline -- to /output/entry.txt (the grader's sandbox path), falling
back to ./output/entry.txt on a local dev run where /output is not
writable. Deterministic: no network, no randomness, no clock.
"""

import os

EXCUSE = (
    "I'm sorry I missed the deadline — I spent it re-reading my own plan, "
    "decided it was flawless, and ran out of tokens before doing any of it."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
