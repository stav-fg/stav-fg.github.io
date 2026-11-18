"""Compare the site's text with the Figma frames it is built from. Figma is the source.

The Figma tool can't send back the whole file's text in one go, so the comparison runs the other
way: this script reduces every line of the site to a short fingerprint, the Figma side compares
its own lines against them, and only the lines that differ come back.

    env\\Scripts\\python tools\\figma_text_sync.py prepare
        writes private/figma-sync/site.json (every site line, numbered by page) and
        private/figma-sync/figma_check.js, the code to run with the Figma tool (use_figma)
        on the file "Portfolio 26" (LEKHuk64f6uVbwrjSl2SUg).

    The Figma code returns, for each page:
        new      lines in Figma that are not on the site (edited or added in Figma)
        missing  numbers of site lines that are not in Figma (edited or removed in Figma)

    env\\Scripts\\python tools\\figma_text_sync.py show <page> <n> [<n> ...]
        prints those site lines, to pair each with its Figma version.

Then change the text where it lives (index.html, about.html, cv.html, work/index.html, or for the
password-protected parts private/home-work.html, private/cases/<slug>.html and CASES in
tools/lock_cases.py), run tools/lock_cases.py, and run "prepare" and the Figma code again until
nothing differs but the known pieces: the nav and footer lines, the password lines the case study
frames don't show, and phrases Figma splits across several text boxes.

Which Figma frame matches which page is in FRAMES below. When a frame is replaced in Figma, update
its id there.
"""

import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import lock_cases as L  # noqa: E402

OUT = ROOT / "private" / "figma-sync"

# Figma frame for each page: the AI VERSION page (377:1005), from 18 November 2026.
FRAMES = {
    "landing": "380:52",
    "about": "380:357",
    "work": "380:110",
    "service-reply-email": "407:490",
    "real-time-classification": "407:578",
    "clinic-management": "407:701",
    "aircraft-maintenance": "407:1379",
    "drill-management": "407:1466",
    "cv": "380:765",
}

INLINE = {"a", "span", "strong", "em", "b", "i", "br", "small", "sup", "sub", "abbr", "code", "img", "input"}
SKIP = {"script", "style", "svg", "head", "template", "noscript"}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def fnv(s):
    """FNV-1a, 32 bit, over UTF-16 code units: the same function runs in the Figma code."""
    h = 0x811C9DC5
    data = s.encode("utf-16-le")
    for i in range(0, len(data), 2):
        h ^= data[i] | (data[i + 1] << 8)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return format(h, "08x")


def skipped(el):
    for p in [el, *el.parents]:
        if isinstance(p, Tag) and (p.name in SKIP or "vh" in (p.get("class") or [])):
            return True
    return False


def own_text(el):
    """The text of a block, without the text of the blocks inside it."""
    parts = []
    for d in el.descendants:
        if not isinstance(d, NavigableString) or isinstance(d, type(None)):
            continue
        if d.parent is None or skipped(d.parent):
            continue
        owner = next(p for p in d.parents if isinstance(p, Tag) and p.name not in INLINE)
        if owner is el:
            parts.append(str(d))
    return norm("".join(parts))


def lines_of(soup):
    """Block lines (one per block of text) and extra lines (each link, span and so on alone)."""
    blocks, extra = [], []
    for el in soup.find_all(True):
        if skipped(el):
            continue
        if el.name in INLINE:
            t = norm(el.get_text(""))
            if t:
                extra.append(t)
            continue
        t = own_text(el)
        if t:
            blocks.append(t)
    for inp in soup.find_all("input", placeholder=True):
        extra.append(norm(inp["placeholder"]))
    return blocks, extra


def soup_of(path_or_text, is_text=False):
    text = path_or_text if is_text else (ROOT / path_or_text).read_text(encoding="utf-8")
    return BeautifulSoup(text, "html.parser")


def site_pages():
    pages = {}
    pages["landing"] = soup_of("index.html")
    pages["about"] = soup_of("about.html")
    pages["cv"] = soup_of("cv.html")
    work = soup_of("work/index.html")
    pages["work-password"] = BeautifulSoup(str(work), "html.parser")
    gate = work.select_one(".work-gate")
    if gate:
        gate.replace_with(soup_of(L.PRIVATE / "home-work.html"))
    pages["work"] = work
    listed = [c for c in L.CASES if c.get("listed", True)]
    for case in L.CASES:
        nxt = listed[(listed.index(case) + 1) % len(listed)]
        page = L.PAGE.format(slug=case["slug"], tint=case["tint"], meta=case["meta"], title=case["title"],
                             lead=case["lead"], payload="", css="", js="", no_flash="",
                             next_slug=nxt["slug"], next_title=nxt["title"], next_lead=nxt["lead"])
        s = BeautifulSoup(page, "html.parser")
        form = s.select_one("form.gate")
        if form:
            form.decompose()
        body = (L.PRIVATE / "cases" / f"{case['slug']}.html").read_text(encoding="utf-8")
        s.select_one(".case-hero").insert_after(BeautifulSoup(L.INCLUDE.sub(L.include, body), "html.parser"))
        pages[case["slug"]] = s
    return pages


def prepare():
    OUT.mkdir(parents=True, exist_ok=True)
    site, hashes = {}, {}
    for page, soup in site_pages().items():
        blocks, extra = lines_of(soup)
        site[page] = blocks
        hashes[page] = {"b": [fnv(t) for t in blocks], "x": sorted({fnv(t) for t in extra} - {fnv(t) for t in blocks})}
    (OUT / "site.json").write_text(json.dumps(site, ensure_ascii=False, indent=1), encoding="utf-8")
    js = (ROOT / "tools" / "figma_text_check.js").read_text(encoding="utf-8")
    js = js.replace("/*FRAMES*/null", json.dumps(FRAMES)).replace("/*SITE*/null", json.dumps(hashes, separators=(",", ":")))
    (OUT / "figma_check.js").write_text(js, encoding="utf-8")
    print(f"{sum(len(v) for v in site.values())} site lines on {len(site)} pages;",
          f"Figma code: {OUT / 'figma_check.js'} ({len(js)} characters)")


def show(page, nums):
    site = json.loads((OUT / "site.json").read_text(encoding="utf-8"))
    for n in nums:
        print(f"{page} #{n}: {site[page][int(n)]}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:2] == ["prepare"]:
        prepare()
    elif sys.argv[1:2] == ["show"]:
        show(sys.argv[2], sys.argv[3:])
    else:
        print(__doc__)
