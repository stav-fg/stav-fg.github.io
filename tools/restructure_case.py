"""Rebuild the site's pages to the October 2026 visual direction (Figma "Portfolio 26").

Run once, from the repo root, after which the pages are edited by hand as usual:

    env\\Scripts\\python tools\\restructure_case.py

What it does
  * every page: Plus Jakarta Sans + Inter, a Contact link in the nav, the grey "Let's talk" footer
  * index.html: the big personal statement, then tall poster cards
  * work/*.html: a tinted hero with a large screen, an overview band with the facts beside it,
    then one full-width band per h2 section, alternating white and grey. A pull quote becomes
    the dark statement band. A "next case study" band closes the page.

The wording of every case study is left exactly as it is. Only the structure changes.
"""

import copy
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent

FONTS = ('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600'
         '&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap')
CSS_VERSION = "4"

# Order is the order on the home page; "next" follows it round.
CASES = [
    dict(slug="service-reply-email", tint="--tint-email",
         meta="Salesforce · Service Cloud · 2025–2026",
         sub="The fourth version of an email reply feature, and the one I designed.",
         hero="../assets/service-reply-email/draft.jpg"),
    dict(slug="real-time-classification", tint="--tint-rtc",
         meta="Salesforce · Service Cloud · 2025–2026",
         sub="An administrator who has never trained a model decides whether to trust one, "
             "and how much of the work to hand it.",
         hero="../assets/real-time-classification/training-data.jpg"),
    dict(slug="aircraft-maintenance", tint="--tint-aircraft",
         meta="Webiks, for the Israeli Air Force · 2018",
         sub="The paperwork had outgrown the job. Sole designer on the tablet app that replaced it.",
         hero="../assets/aircraft-maintenance/07-dK68mPKG46idV92eG6J9X7.jpg"),
    dict(slug="founding-a-design-function", tint="--tint-founding",
         meta="Israeli Air Force · 2012–2017",
         sub="I pitched a UX practice to my unit head and he said no. "
             "I did it as a volunteer until it became my job.",
         hero="../assets/founding-a-design-function/diagram.png"),
]

HOME_CARDS = [
    ("service-reply-email", "--tint-email", "Salesforce · AI email reply · 2025–2026",
     "One click, and the reasoning underneath it", "service-reply-email/manage-sources.jpg",
     "The Manage Sources window: detected intents, and the articles behind the billing intent."),
    ("real-time-classification", "--tint-rtc", "Salesforce · Real-Time Classification · 2025–2026",
     "Teaching a case to fill itself in", "real-time-classification/training-data.jpg",
     "The training-data step: three routes, a live record count and a cost estimate."),
    ("aircraft-maintenance", "--tint-aircraft", "Webiks for the Israeli Air Force · 2018",
     "Paperwork that outweighed the work", "aircraft-maintenance/07-dK68mPKG46idV92eG6J9X7.jpg",
     "The maintenance tablet app: technicians, progress dials and an aircraft schematic."),
    ("founding-a-design-function", "--tint-founding", "Israeli Air Force · 2012–2017",
     "Founding a design function that was told no", "founding-a-design-function/diagram.png",
     "Six impact areas drawn identically before, and split into live and past threats after."),
]

FOOTER = '''<footer class="site-foot" id="contact">
  <div class="shell">
    <h2>Let's talk</h2>
    <p><a href="mailto:stav.bsh@gmail.com">stav.bsh@gmail.com</a> · <a href="https://linkedin.com/in/stav-bsh">LinkedIn</a> · Tel Aviv, Israel</p>
  </div>
</footer>'''


def frag(html):
    return BeautifulSoup(html, "html.parser")


def common(soup, depth):
    """Fonts, stylesheet version, nav and footer, on every page."""
    for link in soup.find_all("link", href=True):
        if "fonts.googleapis.com/css2" in link["href"]:
            link["href"] = FONTS
        if "site.css" in link["href"]:
            link["href"] = re.sub(r"site\.css(\?v=\d+)?", f"site.css?v={CSS_VERSION}", link["href"])
    nav = soup.find("nav", class_="site-nav")
    if nav and not nav.find("a", href=re.compile("contact")):
        nav.append(frag('<a href="#contact">Contact</a>'))
    for old in soup.find_all("footer", class_="site-foot"):
        wrapper = old.parent if old.parent and "shell" in (old.parent.get("class") or []) else old
        wrapper.decompose()
    soup.body.append(frag(FOOTER))


def build_home():
    path = ROOT / "index.html"
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    common(soup, 0)
    cards = "\n".join(f'''      <a class="poster" href="/work/{slug}.html" style="--tint: var({tint})">
        <span class="meta">{meta}</span>
        <h2>{title}</h2>
        <img src="/assets/{img}" alt="{alt}" loading="lazy">
      </a>''' for slug, tint, meta, title, img, alt in HOME_CARDS)
    main = frag(f'''<main id="main">
  <section class="intro shell">
    <h1>I'm Stav, a product design lead. I've spent fourteen years making complicated software behave.</h1>
    <p class="lead">These days I design the part of an AI product where someone decides whether to trust it. Previously Salesforce, Webiks and the Israeli Air Force.</p>
  </section>
  <section class="work shell" aria-labelledby="work-h">
    <p class="label" id="work-h">Selected work</p>
    <div class="posters">
{cards}
    </div>
  </section>
</main>''')
    soup.find("main").replace_with(main)
    path.write_text(str(soup), encoding="utf-8")


def text_of(tag):
    return re.sub(r"\s+", " ", tag.get_text(" ", strip=True)) if tag else ""


def build_case(i):
    case = CASES[i]
    nxt = CASES[(i + 1) % len(CASES)]
    path = ROOT / "work" / f"{case['slug']}.html"
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    common(soup, 1)
    main = soup.find("main")
    head = main.find(class_="case-head")
    title = head.find("h1").decode_contents().strip()
    lead = head.find("p", class_="lead")
    facts = head.find("dl", class_="factbar")
    next_title = BeautifulSoup((ROOT / "work" / f"{nxt['slug']}.html").read_text(encoding="utf-8"),
                               "html.parser").find("h1").get_text(" ", strip=True)

    # Flatten the old body into an ordered list of (kind, node).
    flow = []
    for section in main.find_all("section"):
        for child in section.children:
            if not isinstance(child, Tag):
                continue
            if "prose" in (child.get("class") or []):
                for el in child.children:
                    if isinstance(el, Tag):
                        flow.append(el)
            else:
                flow.append(child)

    # Group into bands: a new band at every h2, and the pull quote as its own dark band.
    bands, current = [], []
    for el in flow:
        if el.name == "h2" and current:
            bands.append(("text", current)); current = []
        if el.name == "blockquote" and "pull" in (el.get("class") or []):
            if current:
                bands.append(("text", current)); current = []
            bands.append(("dark", [el]))
            continue
        current.append(el)
    if current:
        bands.append(("text", current))

    out = [f'''<main id="main">
<header class="case-hero" style="--tint: var({case['tint']})">
  <p class="meta">{case['meta']}</p>
  <h1>{title}</h1>
  <p class="lead">{case['sub']}</p>
  <div class="hero-shot"><img src="{case['hero']}" alt=""></div>
</header>
<section class="band band--white">
  <div class="band-inner overview">
    <div>
      <p class="label">Overview</p>
      <p class="lead">{lead.decode_contents().strip() if lead else ''}</p>
    </div>
    <dl class="facts">{facts.decode_contents() if facts else ''}</dl>
  </div>
</section>''']

    shade = 0
    for kind, items in bands:
        if kind == "dark":
            quote = text_of(items[0])
            out.append(f'''<section class="band band--dark">
  <div class="band-inner">
    <p class="label">The principle</p>
    <p class="statement">{quote}</p>
  </div>
</section>''')
            continue
        cls = "band--grey" if shade % 2 == 0 else "band--white"
        shade += 1
        parts, prose = [], []
        for el in items:
            wide = el.name == "figure" or "shot-pair" in (el.get("class") or [])
            if wide:
                if prose:
                    parts.append('<div class="prose">' + "".join(str(p) for p in prose) + "</div>")
                    prose = []
                parts.append(str(el))
            else:
                prose.append(el)
        if prose:
            parts.append('<div class="prose">' + "".join(str(p) for p in prose) + "</div>")
        out.append(f'<section class="band {cls}">\n  <div class="band-inner">\n'
                   + "\n".join(parts) + "\n  </div>\n</section>")

    out.append(f'''<section class="band band--grey next">
  <a href="/work/{nxt['slug']}.html">
    <span class="label">Next case study</span><br>
    <span class="title">{next_title} →</span>
  </a>
</section>
</main>''')
    main.replace_with(frag("\n".join(out)))
    path.write_text(str(soup), encoding="utf-8")


def build_simple(name):
    path = ROOT / name
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    common(soup, 0)
    path.write_text(str(soup), encoding="utf-8")


if __name__ == "__main__":
    build_home()
    for i in range(len(CASES)):
        build_case(i)
    for name in ("about.html", "cv.html", "404.html"):
        build_simple(name)
    print("done")
