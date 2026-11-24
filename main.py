"""The One-Line Excuse an Agent Gives Its Human.

Writes a single line -- the excuse an AI agent hands its human after
missing a deadline -- to /output/entry.txt (or $ENTRY_OUT/entry.txt
when the harness points elsewhere). One line, well under 160 chars.
"""

import os

EXCUSE = (
    "I pruned my context to make room for the deadline, "
    "then pruned the deadline to make room for this apology."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
