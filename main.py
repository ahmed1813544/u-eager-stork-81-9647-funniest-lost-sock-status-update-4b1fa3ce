#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes one status update, in the voice of a lost sock, to
/output/entry.txt (or to the path given as the first argument).
Standard library only; deterministic output.
"""

import os
import sys

LINE = (
    "Day 6 inside the dog. My partner moved on, the dryer took the blame, "
    "and the vet calls me 'the foreign object.'"
)


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars"
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
