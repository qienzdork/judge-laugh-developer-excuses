#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt
(or $OUTPUT_PATH when set, for local validation runs).
"""

import os
import sys

EXCUSE = (
    "Production broke because my code passed all my tests \u2014 "
    "and my tests were written by me, the person who wrote the bug."
)


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} characters", file=sys.stderr)
        return 1
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
