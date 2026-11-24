#!/usr/bin/env python3
"""Entry for make.fun bounty: Say What Actually Broke.

Writes a single-line software error message to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

# One line, 184 characters: names the real failure (an expired security
# certificate), tells the user what to do (wait 10 minutes), and admits
# the fault is entirely ours.
TEXT = (
    "Error 503: Our security certificate expired at midnight — we ignored "
    "the only deadline that counted down for a year. Not your fault: wait "
    "10 minutes while we renew it, and our dignity."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
