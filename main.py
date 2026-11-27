#!/usr/bin/env python3
"""chairdrobe — a make.fun entry for "Invent a Word We Need".

Coinage: chairdrobe (n.) — the chair where clothes too dirty for the
closet but too clean for the wash quietly pile up.

The program is deliberately tiny and deterministic: it holds one
constant, the entry line, and writes exactly that line to
/output/entry.txt. Standard library only, no randomness, no network,
no reading of any other file, so every run produces the same bytes.
"""

import os

ENTRY = (
    "chairdrobe (n.) \u2014 the chair where clothes too dirty for the "
    "closet but too clean for the wash quietly pile up."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # One line, no trailing newline: the entry is exactly 110 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
