#!/bin/sh
# Create anatomy-sequence.gif from s1.png, s2.png, s3.png, s4.png
# Requires ImageMagick: brew install imagemagick
cd "$(dirname "$0")/.." || exit 1
DIR="assets/images"
for f in s1.png s2.png s3.png s4.png; do
  [ -f "$DIR/$f" ] || { echo "Missing: $DIR/$f"; exit 1; }
done
if command -v magick >/dev/null 2>&1; then
  magick -delay 8 -loop 0 "$DIR/s1.png" "$DIR/s2.png" "$DIR/s3.png" "$DIR/s4.png" "$DIR/anatomy-sequence.gif"
elif command -v convert >/dev/null 2>&1; then
  convert -delay 8 -loop 0 "$DIR/s1.png" "$DIR/s2.png" "$DIR/s3.png" "$DIR/s4.png" "$DIR/anatomy-sequence.gif"
else
  echo "Install ImageMagick: brew install imagemagick" >&2
  exit 1
fi
echo "Created: $DIR/anatomy-sequence.gif"
