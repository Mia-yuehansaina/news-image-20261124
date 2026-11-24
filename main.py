#!/usr/bin/env python3
"""Write the competition entry image to /output/entry.png.

The entry image is bundled in this repository as entry.png. This program
simply copies it byte-for-byte to the output directory, so the result is
identical on every run. It uses only the Python standard library, needs
no network access, and never depends on the clock or on randomness.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1
    out_dir = "/output"
    target = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"Wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
