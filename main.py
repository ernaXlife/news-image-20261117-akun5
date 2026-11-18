#!/usr/bin/env python3
"""news-image-20261117 entry: emit the pre-rendered front page.

The page itself is rendered offline (PIL) and bundled as image.jpg; this
program only places a byte-identical copy at /output/entry.png so the run
is deterministic. No network, no randomness.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "image.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, dest)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        raise RuntimeError("copy incomplete: size mismatch")


if __name__ == "__main__":
    main()
