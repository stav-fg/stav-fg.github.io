"""Turn raw screen exports into the images the site publishes.

Two outputs, both driven by the manifest at the bottom of this file:

  covers   assets/covers/<slug>.jpg, 1600x1000. A crop of one real screen, set on a
           soft tinted panel with rounded corners and a shadow, bleeding off the
           bottom-right edge. Every project uses the same recipe so the index reads
           as one set.
  shots    assets/<slug>/<name>.jpg, at most 1600 px wide, for the case study pages.

Sources live in source-material/, which is gitignored: the raw exports never enter
the public repo, only these resized copies do. PDFs are rendered at 2x with pymupdf,
and SVGs the same way, so a diagram can be a cover too.

    env\\Scripts\\python tools\\prepare_images.py
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source-material" / "screens" / "all"

COVER_W, COVER_H = 1600, 1000
SHOT_MAX_W = 1600


def load(path):
    path = Path(path)
    if not path.is_absolute():
        path = SRC / path
    if path.suffix.lower() in (".pdf", ".svg"):
        doc = pymupdf.open(path)
        pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    return Image.open(path).convert("RGB")


def crop_frac(im, box):
    """box is (left, top, right, bottom) as fractions of the image."""
    w, h = im.size
    l, t, r, b = box
    return im.crop((round(l * w), round(t * h), round(r * w), round(b * h)))


def rounded(im, radius):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.width - 1, im.height - 1), radius, fill=255)
    return mask


def cover(src, box, bg, out, inset=(150, 130), width=1450, bleed=True):
    """Screen crop on a tinted panel, offset so it runs off the right and bottom edges.

    bleed=False centres the whole image instead, for diagrams that must be seen entire.
    """
    shot = crop_frac(load(src), box)
    # Fill the panel: at least `width` wide, and tall enough to run off the bottom edge.
    if bleed:
        x, y = inset
        scale = max(width / shot.width, (COVER_H - y + 40) / shot.height)
    else:
        scale = min(1440 / shot.width, 880 / shot.height)
    shot = shot.resize((round(shot.width * scale), round(shot.height * scale)), Image.LANCZOS)
    if not bleed:
        x, y = (COVER_W - shot.width) // 2, (COVER_H - shot.height) // 2

    canvas = Image.new("RGB", (COVER_W, COVER_H), bg)
    mask = rounded(shot, 18)

    shadow = Image.new("L", (COVER_W + 200, COVER_H + 200), 0)
    shadow.paste(mask, (x + 100, y + 118))
    shadow = shadow.filter(ImageFilter.GaussianBlur(36))
    tint = Image.new("RGB", shadow.size, (30, 26, 44))
    base = Image.new("RGB", shadow.size, bg)
    base.paste(canvas, (100, 100))
    base = Image.composite(tint, base, shadow.point(lambda v: int(v * 0.22)))
    canvas = base.crop((100, 100, 100 + COVER_W, 100 + COVER_H))

    canvas.paste(shot, (x, y), mask)
    out = ROOT / "assets" / "covers" / f"{out}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out, quality=86, optimize=True, progressive=True)
    return out


def shot(src, slug, name, box=None):
    im = load(src)
    if box:
        im = crop_frac(im, box)
    if im.width > SHOT_MAX_W:
        im = im.resize((SHOT_MAX_W, round(im.height * SHOT_MAX_W / im.width)), Image.LANCZOS)
    out = ROOT / "assets" / slug / f"{name}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=85, optimize=True, progressive=True)
    return out


# --- manifest --------------------------------------------------------------
# Tints: one soft colour per project, all pale enough that the screen carries the image.

LAVENDER = (236, 230, 247)
MIST = (226, 234, 246)
SAND = (242, 236, 226)
SAGE = (228, 237, 230)

COVERS = [
    # slug, source, crop box, tint, bleed. Whole screens, centred: a crop of a
    # dense enterprise screen reads as a broken fragment at card size.
    ("real-time-classification", "1790758224692__11_-_Modal__Step_4.png", (0, 0, 1, 1), LAVENDER, False),
    ("service-reply-email", "1790246615630__CSR_4_-_draft_generated.pdf", (0, 0, 1, 1), MIST, False),
    ("aircraft-maintenance", ROOT / "assets/aircraft-maintenance/07-dK68mPKG46idV92eG6J9X7.jpg",
     (0, 0, 1, 1), SAND, False),
    ("founding-a-design-function", "aerial-defense-ellipses.svg", (0, 0, 1, 1), SAGE, False),
]

SHOTS = [
    # source, slug, name, crop box
    ("1790758226522__19_-_Config_Rec9ord_Page_-_Models_&_Training.png", "real-time-classification",
     "thresholds", (0.04, 0.315, 1.0, 0.585)),
    ("1790758224692__11_-_Modal__Step_4.png", "real-time-classification", "training-data", None),
    ("1790758228187__9_-_Modal__Step_3.png", "real-time-classification", "input-fields", None),
    ("1790758232001__12_-_Modal__Step_5.png", "real-time-classification", "review", None),
    ("1790758229644__15_-_Config_Rec9ord_Page_-_Configuration_Details.png", "real-time-classification",
     "record-page", None),
    ("1790246615630__CSR_4_-_draft_generated.pdf", "service-reply-email", "draft", None),
    ("1790246598569__CSR_5_-_manage_sources.png", "service-reply-email", "manage-sources", None),
]


if __name__ == "__main__":
    for slug, src, box, bg, *rest in COVERS:
        print(cover(src, box, bg, slug, bleed=rest[0] if rest else True).relative_to(ROOT))
    for src, slug, name, box in SHOTS:
        print(shot(src, slug, name, box).relative_to(ROOT))
