#!/usr/bin/env python3
"""Create anatomy-sequence.gif from s1.png, s2.png, s3.png, s4.png in assets/images/."""
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow", file=sys.stderr)
    sys.exit(1)

IMGDIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
FRAMES = ["s1.png", "s2.png", "s3.png", "s4.png"]
OUT = os.path.join(IMGDIR, "anatomy-sequence.gif")

def main():
    paths = [os.path.join(IMGDIR, f) for f in FRAMES]
    for p in paths:
        if not os.path.isfile(p):
            print("Missing:", p, file=sys.stderr)
            sys.exit(1)
    images = [Image.open(p).convert("RGBA") for p in paths]
    images[0].save(
        OUT,
        save_all=True,
        append_images=images[1:],
        duration=800,
        loop=0,
    )
    print("Created:", OUT)

if __name__ == "__main__":
    main()
