# Stav Fisher Gross — portfolio and CV

Static site. No build step, no framework, no dependencies. Open `index.html` in a browser and
it works. That is deliberate: it deploys to GitHub Pages with zero configuration, and it keeps
the commit history readable, which the handoff brief treats as evidence of the process.

## Where things stand, 7 September 2026

Scaffolded in one session. Four case study pages exist. Two are drafted from real source
material, two are stubs waiting on interviews that have not happened yet.

| Page | State |
|---|---|
| `work/service-reply-email.html` | Stub. Lead case study. No source material exists. |
| `work/real-time-classification.html` | Stub. No source material exists. |
| `work/aircraft-maintenance.html` | Drafted from the live Carbonmade copy. Needs her edit. |
| `work/founding-a-design-function.html` | Drafted from the Portfolio Panel deck. Needs her edit. |
| `about.html` | Not built. |
| `cv.html` | Not built. Draft content is in `drafts/cv.md`. |

Every unresolved item in a drafted page is marked inline with a dashed `.gap` callout that
states what is missing and why it matters. They are visible on purpose. Setting
`<body data-mode="clean">` hides them all for a preview without deleting anything.

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

Local only, never committed:

```
notes/                  findings, open questions, the plan
drafts/                 CV and LinkedIn working copy
source-material/        every input
```

### Why the working files are not in the repo

A `<user>.github.io` Pages repo has to be public, so anything tracked here is world-readable.
That rules out most of what this project runs on:

- `source-material/handoff-brief-v3.txt` names the anchor customer that was explicitly decided
  against naming, and carries her contact details and the full strategy.
- `source-material/portfolio-panel-deck.pdf` has the unredacted clinic screenshots.
- `source-material/github-export/` is Salesforce-internal source, with internal hostnames and her
  internal username in it.
- `notes/` quotes those internal identifiers and contains candid assessments never written for an
  audience.
- `drafts/cv.md` carries contact details next to open questions about her own record.

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
