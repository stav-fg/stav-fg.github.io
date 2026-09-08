# Visuals for the case studies

Written 8 September, after seeing inside the `.fig` files.

## What I can and cannot see

**Can:** every text label, the file's overall structure from its thumbnail, and every embedded
raster asset. A `.fig` is a zip; `Service AI Service Replies.fig` carries 311 images inside it.

**Cannot:** render her actual vector frames. That needs Figma. So the screens themselves still
have to be exported by hand.

The Service Replies file is organised the way a portfolio wants: labelled section cards
(Multi-Intent Support for SR – Setup, SR Chat Messaging, SR Core Messaging Contextual, SR
Messaging for SRA, SR Voice for SRA), each followed by a row of screen states. Exporting is
mechanical, not a hunt.

## A useful discovery about safety

The embedded reference images use Salesforce's **public demo data**: the Dreamforce solar-panel
scenario, `@dreamforce24.demo` addresses, invented customers. Frames built on that data are far
safer to publish than frames showing a real org.

**Export rule: prefer frames using demo data.** Where a frame shows real org names or real case
content, either pick a sibling frame or blur before export. That single rule removes most of the
redaction work later.

## Four kinds of visual, in descending order of value

### 1. Redrawn diagrams of the decision, not screenshots of the screen

The strongest asset in the portfolio so far is not a screenshot. It is the aerial defense ellipse
diagram, because it shows the *decision* rather than the artifact.

The same applies here, and the best candidate is already built:
`drafts/visuals/rtc-threshold-gradient.svg`.

Two thresholds on a confidence axis create three bands: below the lower one nothing happens,
between them a person confirms, above the higher one the model acts alone. Underneath, who decides
in each band: nobody, a person, the model.

That is the thesis of the entire portfolio in one image, drawn from her own configuration screen,
and it contains nothing confidential. It should appear in the RTC case study and, in reduced form,
possibly on the home page.

Others worth drawing rather than screenshotting:
- **KGER**: the one-click surface against the expanded intent list, showing what the second click
  reveals. A before/after of information density.
- **A3 Registry**: the five-phase admin lifecycle as a single spine, from empty state to running
  actor. Redrawn without internal service names.
- **MSJ**: the progression model. Business goal in, personalised capability recommendations out,
  progress accruing across three separate tracks.

### 2. One real screen per case study, at full width

A portfolio needs proof the thing shipped, and a diagram cannot do that. One screen per study,
chosen for legibility rather than completeness, captioned with the decision it demonstrates rather
than a description of what is on it.

The caption is the work. "The default view" is wasted. "Technicians are assigned by dragging onto
the schematic, so the assignment carries its own location" earns its place.

### 3. Before and after pairs, where they exist

RTC has four dated versions of its configuration flow, two of them explicitly responding to
meeting feedback. That is an iteration story with timestamps, and showing v1 beside v3 is more
persuasive than any claim about process.

### 4. The commit history, for the prototypes piece

Unusual on a design portfolio and immediately legible. A rendered list of real commit messages with
internal scopes stripped, or a small cadence chart across the six weeks.

## What to export, and roughly how many

Per case study: **one hero screen, two to four supporting states, and any before/after pair.**
Around six frames each, twenty-five in total. Not the whole file.

Priority order:
1. **RTC** — the model comparison and configuration surfaces. This is the study the screens carry.
2. **A3 Registry** — the four-step configuration modal and the list view.
3. **KGER** — the collapsed reply and the expanded intent view, as a pair.
4. **MSJ** — the journey map, a progress state, and the badge or rank surface.

PNG at 2x is fine. Name them so the order is obvious.

## What must never be exported

Internal service names, the roadmap, release-priority ordering, and the competitor assessment found
on the A3 board. Any frame showing a real customer org. The case studies work without all of it.
