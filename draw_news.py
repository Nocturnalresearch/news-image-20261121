#!/usr/bin/env python3
"""Draw the WORLD NEWS front page for Saturday, 21 November 2026.

A newspaper front page drawn entirely in code with Pillow: masthead with
the date, a 2x2 grid of the day's four verified stories, each with a small
drawn illustration, a region tag, a bold headline and a one-line subhead.
Deterministic: the same bytes every run. Writes entry.png (1024x1024).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 62, 120)
TEAL = (14, 92, 84)
GREY = (90, 86, 78)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def burst(d, cx, cy, r, color):
    """Starburst: 12 spikes around a centre."""
    import math
    pts = []
    for i in range(24):
        ang = math.pi * i / 12
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)


def draw_war(d, x, y, w, h):
    """Night sky, missile streaks, explosions over a city skyline."""
    d.rectangle([x, y, x + w, y + h], fill=(28, 30, 48))
    # stars
    for sx, sy in [(0.12, 0.2), (0.3, 0.12), (0.55, 0.22), (0.78, 0.1),
                   (0.9, 0.28), (0.42, 0.3), (0.66, 0.34)]:
        px, py = x + int(w * sx), y + int(h * sy)
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(230, 230, 220))
    # missile streaks
    d.line([x + int(w * 0.15), y + int(h * 0.55), x + int(w * 0.42), y + int(h * 0.18)],
           fill=(255, 220, 120), width=4)
    d.line([x + int(w * 0.55), y + int(h * 0.62), x + int(w * 0.85), y + int(h * 0.22)],
           fill=(255, 220, 120), width=4)
    # explosions
    burst(d, x + int(w * 0.42), y + int(h * 0.18), 26, (255, 170, 40))
    burst(d, x + int(w * 0.42), y + int(h * 0.18), 13, (255, 230, 120))
    burst(d, x + int(w * 0.85), y + int(h * 0.22), 22, (255, 150, 30))
    burst(d, x + int(w * 0.85), y + int(h * 0.22), 11, (255, 220, 100))
    # skyline
    base = y + h
    for bx, bw, bh in [(0.02, 0.16, 0.42), (0.2, 0.12, 0.55), (0.34, 0.14, 0.38),
                       (0.5, 0.18, 0.6), (0.7, 0.12, 0.45), (0.84, 0.14, 0.52)]:
        d.rectangle([x + int(w * bx), base - int(h * bh),
                     x + int(w * (bx + bw)), base], fill=(12, 12, 20))
    # lit windows
    for wx, wy in [(0.06, 0.72), (0.24, 0.6), (0.38, 0.76), (0.56, 0.55),
                   (0.74, 0.7), (0.88, 0.62)]:
        d.rectangle([x + int(w * wx), y + int(h * wy),
                     x + int(w * wx) + 6, y + int(h * wy) + 8],
                    fill=(255, 210, 90))


def draw_markets(d, x, y, w, h):
    """Red falling chart over a pale grid, with a big -3.7% tag."""
    d.rectangle([x, y, x + w, y + h], fill=(250, 244, 238))
    # grid
    for i in range(1, 5):
        gy = y + int(h * i / 5)
        d.line([x + 8, gy, x + w - 8, gy], fill=(225, 210, 195), width=1)
    # falling line
    pts = [(x + int(w * f), y + int(h * v)) for f, v in
           [(0.06, 0.18), (0.2, 0.3), (0.32, 0.26), (0.45, 0.48),
            (0.58, 0.44), (0.7, 0.66), (0.82, 0.62), (0.94, 0.86)]]
    d.line(pts, fill=(178, 34, 34), width=6, joint="curve")
    # arrow head at the end
    ex, ey = pts[-1]
    d.polygon([(ex, ey + 16), (ex - 16, ey - 4), (ex + 2, ey - 14)],
              fill=(178, 34, 34))
    # bars
    for i, (bx, bh) in enumerate([(0.12, 0.3), (0.3, 0.22), (0.48, 0.34),
                                  (0.66, 0.2), (0.84, 0.26)]):
        bw = int(w * 0.07)
        d.rectangle([x + int(w * bx), y + h - int(h * bh) - 6,
                     x + int(w * bx) + bw, y + h - 6],
                    fill=(198, 70, 60))
    d.text((x + w - 142, y + 8), "-3.7%", font=font(SANS_B, 44), fill=(178, 34, 34))


def draw_politics(d, x, y, w, h):
    """EU circle of stars beside a Union Jack, over three signed pacts."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 238, 246))
    # EU flag panel
    ex, ey, ew, eh = x + 14, y + 12, int(w * 0.42), int(h * 0.58)
    d.rectangle([ex, ey, ex + ew, ey + eh], fill=(0, 51, 153))
    import math
    cx, cy, r = ex + ew // 2, ey + eh // 2, eh // 3
    for i in range(12):
        ang = -math.pi / 2 + 2 * math.pi * i / 12
        sx, sy = cx + r * math.cos(ang), cy + r * math.sin(ang)
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 204, 0))
    # Union Jack panel
    ux, uy, uw, uh = x + w - 14 - int(w * 0.42), y + 12, int(w * 0.42), int(h * 0.58)
    d.rectangle([ux, uy, ux + uw, uy + uh], fill=(1, 33, 105))
    d.polygon([(ux, uy), (ux + 18, uy), (ux + uw, uy + uh - 18), (ux + uw, uy + uh),
               (ux + uw - 18, uy + uh), (ux, uy + 18)], fill=(255, 255, 255))
    d.polygon([(ux + uw, uy), (ux + uw - 18, uy), (ux, uy + uh - 18), (ux, uy + uh),
               (ux + 18, uy + uh), (ux + uw, uy + 18)], fill=(255, 255, 255))
    d.line([ux, uy, ux + uw, uy + uh], fill=(200, 16, 46), width=7)
    d.line([ux + uw, uy, ux, uy + uh], fill=(200, 16, 46), width=7)
    d.line([ux + uw // 2 - 9, uy, ux + uw // 2 - 9, uy + uh], fill=(255, 255, 255), width=18)
    d.line([ux, uy + uh // 2 - 9, ux + uw, uy + uh // 2 - 9], fill=(255, 255, 255), width=18)
    d.line([ux + uw // 2 - 5, uy, ux + uw // 2 - 5, uy + uh], fill=(200, 16, 46), width=10)
    d.line([ux, uy + uh // 2 - 5, ux + uw, uy + uh // 2 - 5], fill=(200, 16, 46), width=10)
    # three pact documents below
    py = y + h - int(h * 0.26)
    for i in range(3):
        px = x + 16 + i * int(w * 0.31)
        d.rectangle([px, py, px + int(w * 0.26), y + h - 10],
                    fill=(255, 255, 255), outline=(120, 120, 120), width=2)
        d.line([px + 8, py + 10, px + int(w * 0.26) - 8, py + 10],
               fill=(24, 62, 120), width=3)
        d.line([px + 8, py + 22, px + int(w * 0.26) - 14, py + 22],
               fill=(150, 150, 150), width=2)
        d.line([px + 8, py + 31, px + int(w * 0.26) - 20, py + 31],
               fill=(150, 150, 150), width=2)


def draw_climate(d, x, y, w, h):
    """A warming globe with a rising thermometer and a COP31 banner."""
    d.rectangle([x, y, x + w, y + h], fill=(228, 240, 232))
    # globe
    cx, cy, r = x + int(w * 0.32), y + int(h * 0.52), int(h * 0.36)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 140, 200))
    d.ellipse([cx - r + 14, cy - r + 10, cx - r + 52, cy - r + 44], fill=(90, 170, 90))
    d.ellipse([cx + 6, cy + 8, cx + 44, cy + 40], fill=(90, 170, 90))
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(40, 110, 170), width=3)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=(40, 110, 170), width=3)
    # thermometer
    tx = x + int(w * 0.72)
    ty0, ty1 = y + 14, y + h - 46
    d.rounded_rectangle([tx, ty0, tx + 26, ty1], radius=13, fill=(255, 255, 255),
                        outline=(120, 120, 120), width=2)
    d.ellipse([tx - 8, ty1 - 22, tx + 34, ty1 + 8], fill=(200, 40, 30))
    d.rectangle([tx + 6, ty0 + 30, tx + 20, ty1 - 8], fill=(200, 40, 30))
    d.text((tx + 34, ty0 + 2), "+1.5C", font=font(SANS_B, 26), fill=(178, 34, 34))
    # banner
    d.rectangle([x + 10, y + h - 34, x + w - 10, y + h - 8],
                fill=(14, 92, 84))
    d.text((x + 22, y + h - 32), "COP31  •  ANTALYA",
           font=font(SANS_B, 20), fill=(255, 255, 255))


STORIES = [
    {
        "tag": "WAR",
        "color": RED,
        "headline": "MISSILES FALL ON POLAND",
        "subhead": ("Russia's biggest strikes of the year hit Kyiv \u2014 Warsaw "
                    "calls the missiles on its soil a deliberate provocation"),
        "draw": draw_war,
    },
    {
        "tag": "MARKETS",
        "color": RED,
        "headline": "AI ROUT WIPES OUT THE YEAR'S GAINS",
        "subhead": ("S&P 500 falls 3.7% into correction as Nasdaq erases 2026 "
                    "\u2014 Nvidia faces SEC accounting probe"),
        "draw": draw_markets,
    },
    {
        "tag": "POLITICS",
        "color": BLUE,
        "headline": "BRITAIN AND EU SIGN BIGGEST DEAL",
        "subhead": ("Biggest step towards the EU since Brexit \u2014 food trade, "
                    "carbon markets, youth mobility for 100,000 young Britons"),
        "draw": draw_politics,
    },
    {
        "tag": "CLIMATE",
        "color": TEAL,
        "headline": "COP31 DEADLOCKED ON FOSSIL FUELS",
        "subhead": ("Climate talks in Antalya run past deadline as nearly 200 "
                    "nations fail to agree"),
        "draw": draw_climate,
    },
]


def draw_cell(d, x, y, w, h, story):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255),
                outline=(160, 155, 145), width=2)
    # tag
    tag_f = font(SANS_B, 22)
    d.text((x + 16, y + 12), story["tag"], font=tag_f, fill=story["color"])
    tw = d.textlength(story["tag"], font=tag_f)
    d.line([x + 16 + tw + 10, y + 24, x + w - 16, y + 24],
           fill=story["color"], width=2)
    # illustration
    ix, iy, iw, ih = x + 16, y + 42, w - 32, 140
    story["draw"](d, ix, iy, iw, ih)
    d.rectangle([ix, iy, ix + iw, iy + ih], outline=(120, 115, 105), width=1)
    # headline
    hf = font(SERIF_B, 33)
    lines = wrap(d, story["headline"], hf, w - 32)
    hy = iy + ih + 12
    for ln in lines:
        d.text((x + 16, hy), ln, font=hf, fill=INK)
        hy += 38
    # subhead
    sf = font(SANS, 20)
    slines = wrap(d, story["subhead"], sf, w - 32)
    sy = hy + 6
    for ln in slines:
        d.text((x + 16, sy), ln, font=sf, fill=(52, 50, 46))
        sy += 26


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 28  # page margin

    # ---- masthead ----
    d.text((W // 2, 24), "WORLD NEWS", font=font(SERIF_B, 88),
           fill=INK, anchor="ma")
    d.line([m, 128, W - m, 128], fill=INK, width=3)
    d.line([m, 134, W - m, 134], fill=INK, width=1)
    d.text((W // 2, 142), "SATURDAY, 21 NOVEMBER 2026",
           font=font(SANS_B, 28), fill=RED, anchor="ma")
    d.text((m, 142), "No. 325", font=font(SANS, 20), fill=GREY)
    d.text((W - m, 142), "PRICE: FREE", font=font(SANS, 20), fill=GREY,
           anchor="ra")
    d.line([m, 178, W - m, 178], fill=INK, width=3)

    # ---- 2x2 grid ----
    gx, gy = m, 190
    gw = (W - 2 * m - 16) // 2
    gh = 376
    positions = [(gx, gy), (gx + gw + 16, gy),
                 (gx, gy + gh + 14), (gx + gw + 16, gy + gh + 14)]
    for story, (cx, cy) in zip(STORIES, positions):
        draw_cell(d, cx, cy, gw, gh, story)

    # ---- footer ----
    fy = gy + 2 * gh + 14 + 10
    d.line([m, fy, W - m, fy], fill=INK, width=2)
    footer = ("ALSO: Houthis fire on Riyadh for a third night \u2014 Saudi-led "
              "coalition intercepts three missiles.")
    d.text((W // 2, fy + 8), footer, font=font(SANS_I, 19),
           fill=(52, 50, 46), anchor="ma")
    d.text((W // 2, fy + 32),
           "Sources: France 24 \u00b7 CBS \u00b7 BBC \u00b7 The Guardian \u00b7 Al Jazeera \u2014 21 Nov 2026",
           font=font(SANS, 15), fill=GREY, anchor="ma")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
