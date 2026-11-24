"""Sum up 24 November 2026 world news in one image.

Deterministic: copies the bundled entry.png to /output/entry.png.
No network, no randomness, no model calls.
"""
import os
import shutil
import sys


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
