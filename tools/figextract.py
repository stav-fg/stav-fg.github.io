#!/usr/bin/env python3
"""
Extract readable text from a Figma .fig or FigJam .jam export.

Both are zip containers holding canvas.fig, thumbnail.png, meta.json and images/.
canvas.fig is a 12-byte header followed by length-prefixed chunks: the first is
raw-deflate and holds the kiwi schema (generic, useless), the second is
Zstandard and holds the document.

Needs the `zstandard` package, which tools/setup.py installs into env/ from
requirements.txt. Run setup first, then:

    env/bin/python tools/figextract.py <file.jam|file.fig> <outdir>        macOS, Linux
    env\\Scripts\\python tools\\figextract.py <file.jam|file.fig> <outdir>    Windows
"""
import re, sys, json, struct, pathlib, zipfile
import zstandard as zstd

NOISE = re.compile(r'^(Inter|Regular|Medium|Semi ?Bold|Bold|Light|Connector line|'
                   r'Properties|Document|Canvas|Thin|Black)$', re.I)

def decompress(canvas: bytes) -> bytes:
    off = 12
    (n1,) = struct.unpack_from("<I", canvas, off); off += 4 + n1   # skip schema
    (n2,) = struct.unpack_from("<I", canvas, off); off += 4
    return zstd.ZstdDecompressor().decompress(canvas[off:off+n2],
                                              max_output_size=512 * 1024 * 1024)

def labels(data: bytes):
    out, seen = [], set()
    for r in re.findall(rb'[\x20-\x7e\xc2-\xf4][\x09\x0a\x20-\xf4]{3,}', data):
        try: s = r.decode('utf-8')
        except UnicodeDecodeError: continue
        s = re.sub(r'\s+', ' ', s).strip()
        if len(s) < 4 or NOISE.match(s): continue
        if sum(c.isalpha() or c.isspace() for c in s) / len(s) < 0.7: continue
        k = s.lower()
        if any(k in x or x in k for x in seen): continue
        seen.add(k); out.append(s)
    return out

def main(src, outdir):
    src, out = pathlib.Path(src), pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    stem = src.stem.replace(" ", "-")
    with zipfile.ZipFile(src) as z:
        canvas = z.read("canvas.fig")
        if "thumbnail.png" in z.namelist():
            (out / f"{stem}-thumb.png").write_bytes(z.read("thumbnail.png"))
        if "meta.json" in z.namelist():
            (out / f"{stem}-meta.json").write_bytes(z.read("meta.json"))
    text = labels(decompress(canvas))
    (out / f"{stem}-labels.txt").write_text("\n".join(text))
    print(f"{src.name}: {len(text)} labels -> {out}/{stem}-labels.txt")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
