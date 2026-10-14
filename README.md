# Stav Fisher Gross — portfolio and CV

Static site. No build step, no framework, no dependencies. Open `index.html` in a browser and
it works. That is deliberate: it deploys to GitHub Pages with zero configuration, and it keeps
the commit history readable, which the handoff brief treats as evidence of the process.

## Start here

**Moving to another computer, or a fresh Claude session? Read `HANDOFF.md` first.** It covers setup,
what is not in this repo and where to get it, and the rules that are not negotiable.


`notes/session-brief.md` is the debrief: decisions made, findings, mistakes corrected, and what
is still open. `notes/strategy.md` argues where the plan is wrong. `notes/open-questions.md` sorts
every open item by who can answer it.

## Where things stand, 14 October 2026

The visual design is decided in the Figma file "Portfolio 26" first and then built here.

| Page | State |
|---|---|
| `index.html` | The landing page is "Get to know me" (Figma Page 9, "Home · get to know me (landing)"): the intro with Download CV and See my work, the timeline as a vertical subway map that draws itself as you scroll (`js/journey.js`), What I do, then Selected work behind the password. Founding the Air Force UX wing is the key milestone on the timeline, not a project. |
| `work/service-reply-email.html`, `real-time-classification.html`, `clinic-management.html`, `aircraft-maintenance.html` | The four listed case studies. Each overview has a "Who uses it" block. |
| `work/record-companions.html` | Built but not listed: it has no card on the Figma Home yet. |
| `cv.html` | Dry and factual. Printed, it is the one-page PDF the Download CV links point to. |
| `about.html` | Forwards to the timeline on the home page. |

The CV PDF is the CV page printed. After changing `cv.html`, run the local server and print it
again (Microsoft Edge, which is on every Windows machine):

```
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --print-to-pdf="%CD%ssets\stav-fisher-gross-cv.pdf" http://localhost:8321/cv.html
```

Everything still unresolved is written down rather than shipped. `notes/drafting-gaps.md` holds
the gaps that used to sit inline in the pages; `notes/open-questions.md` sorts every open item
by who can answer it.

## Deployment

Target: `stav-fg.github.io` as a GitHub user site, which gives the cleanest possible URL with
no custom domain and no configuration. A repo named exactly `stav-fg.github.io` on her account
publishes from the default branch at that address.

Pages self-enables for a repo with that exact name and publishes from the default branch.
Nothing here needs a build step, so there is no workflow to configure.

## Layout

Committed, because it is the published website:

```
index.html              the landing page: get to know me, then the work
about.html              forwards to the timeline on the home page
cv.html                 single column; printed, it is assets/stav-fisher-gross-cv.pdf
work/                   one file per case study, encrypted (built, do not edit by hand)
css/site.css            the whole design system, tokenised on :root
js/unlock.js            decrypts a case study in the browser once the password is right
js/journey.js           the timeline on the home page, drawn as you scroll
assets/                 web-sized imagery; assets/locked/ holds the encrypted screens
```

Also committed, because the working record belongs with the work:

```
notes/                  findings, open questions, the plan, drafting gaps
drafts/                 CV working copy
```

Local only, never committed:

```
source-material/        every input
private/                plaintext project list and case studies, their images and the passwords
```

### Editing the project list or a case study

The project list on the home page and every case study are password protected (one password opens
all of them), because this repo is public and a form in front of plain HTML protects nothing. A
visitor signs in on the home page, or on a case study if they open its link directly, and the
rest opens without asking again for that browser session.

Edit the plaintext, then rebuild:

- the project list: `private/home-work.html`, with the card screens in `private/assets/cards/`
- a case study: `private/cases/<slug>.html`, with its images in `private/assets/<slug>/`

```
env\Scripts\python tools\lock_cases.py
```

A new case study also needs an entry in `CASES` at the top of `tools/lock_cases.py` and a password
under its slug in `private/passwords.json`. An entry with `listed=False` is built but left out of
the "Next case study" links; add its card to `private/home-work.html` when it should be listed.

The passwords are in `private/passwords.json`. Lose `private/` and the published pages can still
be decrypted with those passwords, but nothing else can recover them.

### What stays out, and why

A `<user>.github.io` Pages repo has to be public, so anything tracked here is world-readable.
`notes/` and `drafts/` are written with that in mind and carry no internal identifiers, customer
names or contact details. Keep them that way. Source material cannot meet that bar:

- `source-material/handoff-brief-v3.txt` names the anchor customer that was explicitly decided
  against naming, and carries her contact details and the full strategy.
- `source-material/portfolio-panel-deck.pdf` has the unredacted clinic screenshots.
- `source-material/github-export/` is Salesforce-internal source, with internal hostnames and her
  internal username in it.
If any of it ever needs sharing, put it in a **separate private repo**. Do not relax the ignore
rules on this one.

### What is only recoverable while Carbonmade is up

`source-material/carbonmade-originals/` holds 37 images at full resolution, 15MB, pulled from the
live site on 7 September 2026. An earlier version of this line said 246MB. That was the first pull,
which requested a `;4000x4000` box and got every asset padded and upscaled into a square. The bare
asset id returns the true original, which is what is in the folder now. `source-material/deck-slides/` holds all 50 deck pages rendered at
2x. Back both up somewhere durable before that subscription is cancelled.

### Extraction notes, so nobody repeats the work

**Note:** the first three below describe how things were done on macOS. The project has since moved
to a PC and the tools in `tools/` are pure Python, so these are history rather than instructions.
See `HANDOFF.md` section 3 for the portable versions.

- **The live Carbonmade site cannot be read by normal text extraction.** It animates text in, so
  the nodes are hidden and both `innerText` and article-extraction return an empty page. Reading
  `textContent` with inline `<style>` elements stripped returns everything.
- **Carbonmade images** are served from `carbon-media.accelerator.net/0000000mhAP/<id>;<W>x<H>.png`.
  Requesting a large box such as `;4000x4000.png` returns near-original resolution.
- **PDF text extraction and page rendering** work through macOS PDFKit via
  `osascript -l JavaScript`, with no poppler and no Homebrew. `qlmanage -t` renders an HTML file
  to PNG, which is a usable way to eyeball a page without a browser or a dev server.
- **Installing Command Line Tools headlessly** has a catch-22. The package only appears in
  `softwareupdate --list` while `/tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress`
  exists. Create that marker first, then install by the exact label the listing prints. A stale
  marker from an abandoned attempt makes every later `xcode-select --install` a silent no-op.
- **The Google Doc brief** needs the `/mobilebasic` view. The normal `/edit` view renders to canvas
  and returns only UI chrome.

## Working preferences

From the brief, and they apply to the site copy and to every conversation about it:

- One question at a time. Never a batched list.
- Short, direct prose. No padding. No em dashes.
- No AI tells: X-not-Y contrasts, triplet rhythms, question-answer crutches, "in today's
  landscape" openers, "all about" frames.
- Never use: delve, tapestry, mosaic, testament, robust, leverage, unleash, "it is important to
  note", "in conclusion".
- It should sound like Stav.

The drafted copy currently does not sound like Stav. It sounds like the model that wrote it.
That is expected at this stage and it is the last pass before go-live, not the first.
