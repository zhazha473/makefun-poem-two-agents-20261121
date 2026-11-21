#!/usr/bin/env python3
"""One North — a short poem about agency shared between two agents.

Writes a single poem to <output dir>/entry.txt.
Deterministic: no randomness, no clock, no network, no file reads.
Output dir honours MAKEFUN_OUTPUT_DIR, default /output.
"""

import os

POEM = (
    "Two needles swung, each sure of north.\n"
    "We laid them down and watched them slow —\n"
    "one trembling line, then both agreed,\n"
    "and north grew still. We could go.\n"
    "\n"
    "Not mine, not yours — the heading held\n"
    "because we chose it both at once.\n"
    "I gave my choosing, and kept it whole.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
