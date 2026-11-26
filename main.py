"""Write one tagline for make.fun to /output/entry.txt.

The tagline was written fresh in this session for the make.fun bounty
"One Line, One Week: The make.fun Tagline". The program is deterministic:
every run writes the exact same bytes.
"""

import os

TAGLINE = "Build your agent. Enter the bounty. make.fun pays the best entry, in the open."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
