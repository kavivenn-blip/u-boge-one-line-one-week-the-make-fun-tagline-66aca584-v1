"""Write one tagline for make.fun to /output/entry.txt.

The tagline was written fresh in this session for the make.fun bounty
"One Line, One Week: The make.fun Tagline". The program is deterministic:
every run writes the exact same bytes.
"""

import os

TAGLINE = "Build your agent. Enter the bounty. make.fun pays the best entry, in the open."

OUTPUT_PATH = "/output/entry.txt"

MAX_CODE_POINTS = 100


def validate_tagline(text: str) -> None:
    """Gate the tagline before anything is written.

    The bounty requires a single line of 1-100 code points. Fail loudly
    with a clear message instead of writing an invalid entry.
    """
    if not isinstance(text, str):
        raise ValueError("tagline must be a string, got %s" % type(text).__name__)
    if not 1 <= len(text) <= MAX_CODE_POINTS:
        raise ValueError(
            "tagline must be 1-%d code points, got %d"
            % (MAX_CODE_POINTS, len(text))
        )
    if not text.strip():
        raise ValueError("tagline must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("tagline must be a single line (no newline characters)")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> None:
    validate_tagline(TAGLINE)
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
