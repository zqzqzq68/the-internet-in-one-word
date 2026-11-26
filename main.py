"""The Internet in One Word.

This program is the whole entry. It writes a single word to
/output/entry.txt, the one text the judge compares two at a time.

The word is "yapping": the entire internet, at any hour, is billions
of people talking at once and almost nobody listening. It is funny on
its own, it is true of the internet as a whole rather than of one app,
it is not the first obvious word anyone reaches for, and it lands in
one beat at seven letters.

The program is fully deterministic: it takes no input, reads no
network and no environment, and writes the same seven bytes on
every run, so two runs in the grader's sandbox agree byte for byte.
"""

import os

WORD = "yapping"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry word, exactly, with no extra bytes."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
