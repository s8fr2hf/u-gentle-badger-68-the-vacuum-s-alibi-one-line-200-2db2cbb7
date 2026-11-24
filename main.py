#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters max.

Pure standard library. Writes the vacuum's deadpan alibi to /output/entry.txt.
"""

import os

ALIBI = (
    "I did not miss that spot. My sensors found a sock, a crumb, and "
    "something I have classified as evidence. I filed a report and "
    "clocked out early. Case closed."
)


def main() -> None:
    line = ALIBI.strip()
    assert 1 <= len(line) <= 200, f"alibi must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "alibi must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
