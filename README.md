# Stav Fisher Gross — portfolio and CV

Static site. No build step, no framework, no dependencies. Open `index.html` in a browser and
it works. That is deliberate: it deploys to GitHub Pages with zero configuration, and it keeps
the commit history readable, which the handoff brief treats as evidence of the process.

## Where things stand, 7 September 2026

Scaffolded in one session. Four case study pages exist. Two are drafted from real source
material, two are stubs waiting on interviews that have not happened yet.

| Page | State |
|---|---|
| `index.html` | Lists four case studies. The two Salesforce ones are marked "in writing" and are not linked. |
| `work/aircraft-maintenance.html` | Drafted from the live Carbonmade copy. Needs her edit for voice. |
| `work/founding-a-design-function.html` | Drafted from the Portfolio Panel deck. Needs her edit for voice. |
| `about.html` | Drafted. The most voice-dependent page on the site. |
| `cv.html` | Drafted, single column, print-styled. |

The two Salesforce case studies have no pages yet, on purpose: a case study that is only a list
of unanswered questions is worse than no page. Their scaffolding is in
`notes/interview-scaffold.md` and gets rebuilt into pages once the interview has run.

Everything still unresolved is written down rather than shipped. `notes/drafting-gaps.md` holds
every gap that used to sit inline in the pages; `notes/open-questions.md` sorts every open item
by who can answer it.

## Deployment

Target: `stav-fg.github.io` as a GitHub user site, which gives the cleanest possible URL with
no custom domain and no configuration. A repo named exactly `stav-fg.github.io` on her account
publishes from the default branch at that address.

Not set up yet, and blocked. See below.

## Blocked on Xcode Command Line Tools

`git` on this machine is the Apple stub, not a working binary. `node`, `npm` and `gh` are all
absent. Running any git command triggers the developer tools install prompt.

```bash
xcode-select --install
```

Nothing in this repo needs node. Git is only needed to commit and push, so this blocks
deployment and version history, not the work itself.

## Layout

Committed, because it is the published website:

```
index.html              work index and positioning
about.html
cv.html                 single column, print-styled
work/                   one file per case study
css/site.css            the whole design system, tokenised on :root
assets/                 web-sized imagery
```

Also committed, because the working record belongs with the work:

```
notes/                  findings, open questions, the plan, drafting gaps
drafts/                 CV working copy
```

Local only, never committed:

```
source-material/        every input
```

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

`source-material/carbonmade-originals/` holds 37 images at full resolution, 246MB, pulled from the
live site on 7 September 2026. `source-material/deck-slides/` holds all 50 deck pages rendered at
2x. Back both up somewhere durable before that subscription is cancelled.

### Extraction notes, so nobody repeats the work

- **The live Carbonmade site cannot be read by normal text extraction.** It animates text in, so
  the nodes are hidden and both `innerText` and article-extraction return an empty page. Reading
  `textContent` with inline `<style>` elements stripped returns everything.
- **Carbonmade images** are served from `carbon-media.accelerator.net/0000000mhAP/<id>;<W>x<H>.png`.
  Requesting a large box such as `;4000x4000.png` returns near-original resolution.
- **PDF text and page rendering work without any developer tools**, via macOS PDFKit through
  `osascript -l JavaScript`. `pdftotext` and `pdftoppm` are not installed and cannot be installed
  without Homebrew.
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
