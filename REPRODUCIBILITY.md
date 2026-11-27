# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The replay checks face connectivity of finite grids with one missing child, intact pairs across a shared face, all 289 explorer selections and exact finite-horizon probability bounds. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/shared-face-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font paths. [Build the paper](paper/BUILD.md).
