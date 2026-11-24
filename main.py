#!/usr/bin/env python3
"""One Word for the Boss — writes the single word to /output/entry.txt."""

import os

WORD = "Cuan"


def main():
    word = WORD.strip()
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word and not word.isspace(), "word must be non-whitespace"
    assert " " not in word and "\t" not in word and "\n" not in word, \
        "exactly one word, no spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    # Read back and re-check the gate on what actually landed on disk.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == word, "entry.txt content mismatch"
    assert written == written.strip(), "no trailing whitespace allowed"
    print(f"Wrote {len(written)}-char word to /output/entry.txt: {written!r}")


if __name__ == "__main__":
    main()
