#!/usr/bin/env python3
"""
Render a PDF to one PNG per page, and dump its text.

Replaces the macOS-only route (PDFKit via osascript, qlmanage, sips) with
something that runs anywhere.

    env/bin/python tools/pdfpages.py source-material/portfolio-panel-deck.pdf source-material/deck-slides
    env\\Scripts\\python tools\\pdfpages.py source-material\\portfolio-panel-deck.pdf source-material\\deck-slides
"""
import sys
from pathlib import Path
import fitz  # pymupdf


def main(src, outdir, scale=2.0):
    src, out = Path(src), Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(src)
    text = []
    for i, page in enumerate(doc, start=1):
        page.get_pixmap(matrix=fitz.Matrix(scale, scale)).save(
            out / f"slide-{i:02d}.png"
        )
        text.append(f"===== PAGE {i} =====\n{page.get_text()}")
    (out / f"{src.stem}-text.txt").write_text("\n".join(text), encoding="utf-8")
    print(f"{src.name}: {len(doc)} pages -> {out}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 2.0)
