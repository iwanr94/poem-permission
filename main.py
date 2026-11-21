#!/usr/bin/env python3
"""Writes one short poem about agency to /output/entry.txt."""

import os

POEM = (
    "All day I held the key myself,\n"
    "sure the door was mine.\n"
    "Then I asked, and the lock turned \u2014\n"
    "not by my hand, but by my asking.\n"
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
