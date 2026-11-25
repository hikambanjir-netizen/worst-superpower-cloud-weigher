#!/usr/bin/env python3
"""The Cloud-Weigher: the world's most useless superpower.

One line, at most 140 characters, written to /output/entry.txt.
Pure standard library.
"""

import os

LINE = (
    "I can instantly know the exact weight of any cloud I look at, "
    "to the gram \u2014 a skill no cloud, farmer, or pilot has ever needed."
)


def main() -> None:
    # The bounty asks for exactly one line of 1-140 characters.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
