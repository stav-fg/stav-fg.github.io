"""Build the password-protected parts of the site: every case study, and the project list on the
home page.

This repo is public, so nothing can be protected by hiding a form over plain HTML. Each protected
part is published as ciphertext and decrypted in the browser once the right password is typed.

    private/cases/<slug>.html      plaintext body of a case study (gitignored)
    private/assets/<slug>/*        its images (gitignored)
    private/home-work.html         the project list shown on the home page (gitignored)
    private/assets/cards/*         the screens on the project cards (gitignored)
    private/passwords.json         {"<slug>": "<password>", "home": "<password>"} (gitignored)

        env\\Scripts\\python tools\\lock_cases.py

writes work/<slug>.html with only the title, the one-line summary and a password form in the
clear, puts the encrypted project list into index.html between its <!--locked:home--> markers, and
writes every image they use to assets/locked/<id>.bin. Images are encrypted with the same key as
their page, so they are useless without the password too.

Crypto: PBKDF2-SHA256 (250,000 rounds, random salt per page) to an AES-256-GCM key. The browser
side is js/unlock.js, which uses WebCrypto with the same parameters. A password typed on one page
is kept for the browser session, so the other pages open without asking again as long as they use
the same password.

A case study fragment: the first top-level <div class="hero-shot"> goes into the tinted hero, and
everything after it goes below. Image paths are written as the public page would use them
(../assets/<slug>/name.jpg) and are rewritten to the encrypted files here.
"""

import base64
import hashlib
import html
import json
import os
import re
from pathlib import Path

from bs4 import BeautifulSoup, Tag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT = Path(__file__).resolve().parent.parent
PRIVATE = ROOT / "private"
LOCKED = ROOT / "assets" / "locked"
ROUNDS = 250_000
CSS_VERSION = "21"
JS_VERSION = "3"

# Public parts of each page, in home page order. "next" goes round the listed pages in this order.
# A page with listed=False is still built, but nothing links to it and its "next" is the first
# listed page. Founding the Air Force UX wing is not a project at all since 14 October 2026: it is
# a key milestone on the home page timeline.
CASES = [
    dict(slug="service-reply-email", tint="--tint-email",
         title="AI Email Reply",
         meta="Salesforce · Service Cloud · 2025-2026",
         lead="One click drafts a reply to every question in a customer's email."),
    dict(slug="real-time-classification", tint="--tint-rtc",
         title="Real-Time Classification",
         meta="Salesforce · Service Cloud · 2025-2026",
         lead="A model that fills in a support case's fields as soon as the case comes in."),
    dict(slug="record-companions", tint="--tint-rc",
         title="Record Companions",
         meta="Salesforce · Service Cloud · 2026",
         lead="The setup page where admins decide which AI assistants run on their records."),
    dict(slug="clinic-management", tint="--tint-clinic",
         title="Clinic Management",
         meta="Asperii, for a top US healthcare enterprise (S&P 500) · 2020-2021",
         lead="The clinic management system is used to plan and follow treatment plans, schedules and resource allocation."),
    dict(slug="aircraft-maintenance", tint="--tint-aircraft",
         title="Aircraft Maintenance",
         meta="Webiks, for the Israeli Air Force · 2018",
         lead="A tablet app that replaced paper reporting in Air Force aircraft maintenance."),
]

# Hides the password form while a password from earlier in the session is being tried, so a
# signed-in visitor does not see the form flash on every page. The same line is in index.html.
NO_FLASH = ('<script>try{if(sessionStorage.getItem("unlock:pw"))'
            'document.documentElement.className="unlocking"}catch(e){}</script>')

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<meta content="noindex, nofollow" name="robots"/>
<title>{title} · Stav Fisher Gross</title>
<meta content="{lead}" name="description"/>
<link href="../favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="https://stav-fg.github.io/work/{slug}.html" rel="canonical"/>
<meta content="article" property="og:type"/>
<meta content="Stav Fisher Gross" property="og:site_name"/>
<meta content="{title} · Stav Fisher Gross" property="og:title"/>
<meta content="{lead}" property="og:description"/>
<meta content="https://stav-fg.github.io/work/{slug}.html" property="og:url"/>
<meta content="https://stav-fg.github.io/assets/og-card.png" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="630" property="og:image:height"/>
<meta content="Stav Fisher Gross, Product Design Lead" property="og:image:alt"/>
<meta content="summary_large_image" name="twitter:card"/>
<link href="../apple-touch-icon.png" rel="apple-touch-icon"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Plus+Jakarta+Sans:wght@500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="../css/site.css?v={css}" rel="stylesheet"/>
{no_flash}
<script defer src="../js/unlock.js?v={js}"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="shell">
<header class="site-head">
<a class="wordmark" href="/">Stav Fisher Gross</a>
<nav aria-label="Primary" class="site-nav">
<a href="/">About</a>
<a aria-current="page" href="/#my-work">Work</a>
<a href="#contact">Contact</a></nav>
</header>
</div>
<main id="main">
<header class="case-hero" style="--tint: var({tint})">
<div class="band-inner">
<a class="back-link" href="/#work"><span aria-hidden="true">←</span> All work</a>
<p class="meta">{meta}</p>
<h1>{title}</h1>
<p class="lead">{lead}</p>
<form class="gate" data-slug="{slug}" autocomplete="off">
<label for="pw">This case study is password protected.</label>
<div class="gate-row">
<input id="pw" name="pw" type="password" placeholder="Password" required/>
<button type="submit">View case study</button>
</div>
<p class="gate-msg" role="status" aria-live="polite"></p>
<p class="gate-ask">Don't have it? Email <a href="mailto:stav.bsh@gmail.com">stav.bsh@gmail.com</a>.</p>
</form>
</div>
</header>
<script type="application/json" id="locked">{payload}</script>
<section class="band band--grey next">
<a href="/work/{next_slug}.html">
<span class="label">Next case study</span><br/>
<span class="title">{next_title} →</span><br/>
<span class="next-lead">{next_lead}</span>
</a>
<p class="next-all"><a href="/#work">All work</a></p>
</section>
</main>
<footer class="site-foot" id="contact">
<div class="shell">
<h2>Let's talk</h2>
<p><a href="mailto:stav.bsh@gmail.com">stav.bsh@gmail.com</a> · <a href="https://linkedin.com/in/stav-bsh">LinkedIn</a> · <a download="" href="/assets/stav-fisher-gross-cv.pdf">Download CV</a> · Tel Aviv, Israel</p>
</div>
</footer>
</body>
</html>
"""

IMG_SRC = re.compile(r"(?:\.\./|/)?assets/([^/]+)/(.+)$")
INCLUDE = re.compile(r"<!--include:([\w.-]+)(?:#([\w-]+))?-->")
HOME_SLOT = re.compile(r"(<!--locked:home-->).*?(<!--/locked:home-->)", re.S)


def b64(b):
    return base64.b64encode(b).decode("ascii")


def derive(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ROUNDS, dklen=32)


def new_key(password):
    salt = os.urandom(16)
    return salt, derive(password, salt)


def seal(key, data):
    """iv (12 bytes) followed by AES-GCM ciphertext and tag."""
    iv = os.urandom(12)
    return iv + AESGCM(key).encrypt(iv, data, None)


def lock_images(soup, key, used):
    """Encrypt every local image the fragment uses and point its <img> at the encrypted file."""
    for img in soup.find_all("img", src=True):
        m = IMG_SRC.match(img["src"])
        if not m:
            continue
        src = PRIVATE / "assets" / m.group(1) / m.group(2)
        data = src.read_bytes()
        # Name by a keyed hash, so file names say nothing about what is inside.
        name = hashlib.sha256(key + data).hexdigest()[:20] + ".bin"
        (LOCKED / name).write_bytes(seal(key, data))
        used.add(name)
        img["data-locked"] = f"/assets/locked/{name}"
        img["data-type"] = "image/png" if src.suffix.lower() == ".png" else "image/jpeg"
        del img["src"]


def payload(salt, key, hero, body):
    """What js/unlock.js reads: `hero` goes next to the form, `body` after the section it is in."""
    blob = seal(key, json.dumps({"hero": hero, "body": body}).encode("utf-8"))
    return json.dumps({"salt": b64(salt), "rounds": ROUNDS, "data": b64(blob)})


def include(m):
    """<!--include:_name.svg--> pulls in a diagram kept in its own file next to the fragment.
    A second copy on the same page is written <!--include:_name.svg#hero-->, which adds -hero to
    every id in it so the two copies do not share ids."""
    text = (PRIVATE / "cases" / m.group(1)).read_text(encoding="utf-8")
    if m.group(2):
        for name in set(re.findall(r'\bid="([^"]+)"', text)):
            text = re.sub(rf"\b{re.escape(name)}\b", f"{name}-{m.group(2)}", text)
    return text


def split_fragment(text):
    soup = BeautifulSoup(text, "html.parser")
    tops = [c for c in soup.children if isinstance(c, Tag)]
    hero = next((t for t in tops if "hero-shot" in (t.get("class") or [])), None)
    if hero is None:
        raise SystemExit("fragment has no top-level <div class=\"hero-shot\">")
    rest = [t for t in tops if t is not hero]
    return soup, hero, rest


def build(case, nxt, password, used):
    slug = case["slug"]
    text = (PRIVATE / "cases" / f"{slug}.html").read_text(encoding="utf-8")
    text = INCLUDE.sub(include, text)
    soup, hero, rest = split_fragment(text)
    salt, key = new_key(password)
    lock_images(soup, key, used)

    out = PAGE.format(slug=slug, tint=case["tint"], meta=html.escape(case["meta"], quote=False),
                      title=case["title"], lead=html.escape(case["lead"]),
                      payload=payload(salt, key, str(hero), "\n".join(str(t) for t in rest)),
                      css=CSS_VERSION, js=JS_VERSION, no_flash=NO_FLASH,
                      next_slug=nxt["slug"], next_title=nxt["title"], next_lead=html.escape(nxt["lead"]))
    (ROOT / "work" / f"{slug}.html").write_text(out, encoding="utf-8")


def build_home(password, used):
    """Encrypt the project list and put it into index.html, which keeps the intro and the form."""
    soup = BeautifulSoup((PRIVATE / "home-work.html").read_text(encoding="utf-8"), "html.parser")
    salt, key = new_key(password)
    lock_images(soup, key, used)
    script = f'<script type="application/json" id="locked">{payload(salt, key, "", str(soup))}</script>'
    page = ROOT / "index.html"
    text = page.read_text(encoding="utf-8")
    if not HOME_SLOT.search(text):
        raise SystemExit("index.html has no <!--locked:home--> ... <!--/locked:home--> markers")
    page.write_text(HOME_SLOT.sub(lambda m: f"{m.group(1)}\n{script}\n{m.group(2)}", text), encoding="utf-8")


def main():
    passwords = json.loads((PRIVATE / "passwords.json").read_text(encoding="utf-8"))
    LOCKED.mkdir(parents=True, exist_ok=True)
    used = set()
    listed = [c for c in CASES if c.get("listed", True)]
    for case in CASES:
        nxt = listed[(listed.index(case) + 1) % len(listed)] if case in listed else listed[0]
        build(case, nxt, passwords[case["slug"]], used)
        print("locked", case["slug"], "->", nxt["slug"])
    build_home(passwords["home"], used)
    print("locked home")
    for stale in LOCKED.glob("*.bin"):
        if stale.name not in used:
            stale.unlink()


if __name__ == "__main__":
    main()
