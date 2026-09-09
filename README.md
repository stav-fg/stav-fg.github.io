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

## Where things stand, 7 September 2026

Scaffolded in one session, from the handoff brief plus the source material it pointed at.
Two case studies are written from real material. Two are listed but unwritten, because the
interviews behind them have not happened.

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

Pages self-enables for a repo with that exact name and publishes from the default branch.
Nothing here needs a build step, so there is no workflow to configure.

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
