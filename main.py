"""Write the dumbest-thing-my-agent-did-today entry to /output/entry.txt.

Stdlib only. Deterministic: the same single line is written on every run.
"""

import os
import shutil

ENTRY = (
    "My agent deleted main.py, restored it from a backup it made five "
    "minutes earlier, and logged the incident as a successful test."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The gate requires 1 to 200 characters; refuse to write an invalid entry.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear the contents of /output without ever removing /output itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
