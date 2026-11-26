"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: `python3 main.py` creates /output if needed and writes the
entry line (95 characters, one line, no trailing newline) to
/output/entry.txt. Verified locally 2026-11-25: output matches the intended
line exactly, sha256 db968ee834dad462da309df372ec41e6ce73603ae1d6ed83356a4da5087cdf19.
"""

import os

TEXT = "We held a meeting to decide whether the email needed a meeting, and the meeting decided it did."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
