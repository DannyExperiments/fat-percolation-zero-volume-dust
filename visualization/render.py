"""Render the two neighboring 4-by-4 blocks with their surviving contacts."""

import argparse
from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BACKGROUND = "#101d25"
PANEL = "#192f39"
TEXT = "#f5faf8"
MUTED = "#c6dedb"
LEFT = "#688c9f"
RIGHT = "#799e94"
LINK = "#a6f2c2"
HOLE = "#ffb893"
SIDES = ((0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7))
CORNERS = ((-1,-1), (1,-1), (1,1), (-1,1))


def project(x, y, z, angle):
    horizontal = x*cos(angle) - z*sin(angle)
    depth = x*sin(angle) + z*cos(angle)
    tilt = .68 + .06*sin(angle)
    vertical = y*cos(tilt) - depth*sin(tilt)
    distance = y*sin(tilt) + depth*cos(tilt)
    scale = 950/(15-distance)
    return 435+scale*horizontal, 254-.58*scale*vertical, distance


def tile_geometry(angle):
    faces = []
    edge_labels = []
    gaps = []
    for side, fill in ((0, LEFT), (1, RIGHT)):
        for row in range(4):
            for col in range(4):
                x = (side * 4.2 + col) - 3.60
                z = (row - 1.5)
                adjacent = col == (3 if side == 0 else 0)
                missing = adjacent and row == side
                if missing:
                    gaps.append(project(x, .09, z, angle))
                    continue
                points = [project(x+i*.46, height, z+j*.46, angle)
                          for height in (-.20, 0) for i, j in CORNERS]
                for face_id, face in enumerate(SIDES):
                    vertices = [points[i] for i in face]
                    color = LINK if row >= 2 and adjacent else fill
                    if face_id < 4:
                        color = "#3c6270" if side == 0 else "#41655b"
                    faces.append((sum(point[2] for point in vertices)/4, vertices, color))
                if adjacent and row >= 2:
                    edge_labels.append(project(x, .06, z, angle))
    return faces, edge_labels, gaps


def frame(angle, fonts):
    title, label, body = fonts
    image = Image.new("RGB", (880, 560), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((28, 16), "Two holes cannot cut the seam", font=title, fill=TEXT)
    draw.text((30, 73), "Two adjacent blocks · N = 2, d = 2", font=body, fill=MUTED)
    draw.rounded_rectangle((27, 122, 853, 431), radius=14, fill=PANEL)
    faces, edge_labels, gaps = tile_geometry(angle)
    for _, points, fill in sorted(faces):
        draw.polygon([p[:2] for p in points], fill=fill, outline=BACKGROUND, width=1)
    for a, b in zip(edge_labels[:2], edge_labels[2:]):
        draw.line((a[:2], b[:2]), fill=TEXT, width=3)
    for x, y, _ in gaps:
        draw.line((x-7,y-7,x+7,y+7),fill=HOLE,width=3)
        draw.line((x+7,y-7,x-7,y+7),fill=HOLE,width=3)
    draw.text((32, 450), "×  Two excluded alignments", font=label, fill=HOLE)
    draw.text((32, 499), "2 of 4 shared-face pairs survive", font=label, fill=LINK)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font", default="DejaVuSans.ttf")
    parser.add_argument("--bold-font", default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output", type=Path, default=Path("visualization/shared-face.gif"))
    args = parser.parse_args()
    fonts = (ImageFont.truetype(args.bold_font, 42), ImageFont.truetype(args.bold_font, 30),
             ImageFont.truetype(args.regular_font, 28))
    frames = [frame(.48+i*tau/64, fonts).quantize(colors=104, method=2) for i in range(64)]
    frames[0].save(args.output, save_all=True, append_images=frames[1:],
                   duration=90, loop=0, disposal=2, optimize=True)


if __name__ == "__main__":
    main()
