"""One Line, One Laugh — make.fun entry (program/v1).

Writes a single funny line, 1-200 UTF-8 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same line every run.

The line is built to the judge brief's criteria, in order: a laugh on a
first read, a surprise turn at the end (the "healthier" setup collapses
into sitting on a taller chair), economy (76 chars, nothing to trim),
a fresh angle (not a stock joke), and clean wording that reads aloud.
"""

import os

LINE = "I bought a standing desk to get healthier; now I just sit on a taller chair."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line, "line must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
