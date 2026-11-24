#!/usr/bin/env python3
"""Entry for Make the AI Judge Laugh: Cat Reviews Its Human.

Writes a single-line one-star review from a house cat about its
human (at most 200 characters) to /output/entry.txt and prints it
to stdout. Pure standard library.
"""

import os

REVIEW = "One star. My human woke me at 3 AM to ask why I was awake, then fell asleep on MY couch, in MY sunbeam, and still hasn't served breakfast."

def main():
    assert 1 <= len(REVIEW) <= 200, f"review length {len(REVIEW)} out of range"
    assert "\n" not in REVIEW and "\r" not in REVIEW, "review must be a single line"
    assert REVIEW.strip(), "review must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)

if __name__ == "__main__":
    main()
