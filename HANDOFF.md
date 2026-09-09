# Handoff: continuing this on another computer

Written 9 September 2026, for Stav picking this up on her own machine, same Anthropic account.

**If you are a fresh Claude session: read this file first, then the four files in step 2. Do not
re-interview anyone. Almost everything has been decided and the reasoning is written down.**

---

## 1. What this is, in four lines

Stav's portfolio and CV, rebuilt for a big tech job search. Her Salesforce access ends
**30 September 2026**, and anything not extracted by then is gone.

The site is built and live at `https://stav-fg.github.io`, currently `noindex` because there is no
go-live date yet. Two case studies are written, four more are chosen and unwritten.

---

## 2. Read these four, in this order

| File | Why |
|---|---|
| `notes/canonical-narrative.md` | What the portfolio argues, and the voice rules. Everything written should serve this. |
| `notes/strategy.md` | Where the original plan was wrong. The job search has the same deadline as the artifact pull and was not in the plan. |
| `notes/session-brief.md` | Decisions made, findings, and the mistakes that were corrected. |
| `notes/document-requests.md` | The four case studies, and the specific datapoints each still needs. |

Then `notes/open-questions.md` for everything still unresolved, sorted by who can answer it.

`notes/memory-export.md` holds what Claude's local memory contained on the old machine. Memory does
not travel between computers, so re-save those if you want them to persist.

---

## 3. Setting up a new Mac

```bash
git clone git@github.com:stav-fg/stav-fg.github.io.git stav-portfolio
cd stav-portfolio
./tools/setup.sh
```

`setup.sh` checks for git, creates the Python environment the Figma extractor needs, and tells you
what is missing. It is safe to run more than once.

Two things it cannot do for you:

- **Xcode Command Line Tools.** Needed for git. `xcode-select --install`. If that seems to do
  nothing, see the catch-22 documented in the README; it cost an hour on the first machine.
- **The Drive connector.** Account-level, so it should already be there. If not, add it in Claude's
  settings.

---

## 4. What is not in this repo, and where to get it

The repo is public because GitHub Pages requires it, so all source material is gitignored. On the
old machine that was 56MB under `source-material/`. None of it is lost, but it has to be fetched
again.

| What | Where it comes from |
|---|---|
| `handoff-brief-v3.txt` | The original Google Doc, still in Drive |
| `portfolio-panel-deck.pdf` | Shared in Ehud's Drive |
| `linkedin-profile-export.pdf` | Re-export from LinkedIn in two minutes |
| `deck-slides/` | Re-derivable from the deck PDF, see README extraction notes |
| `github-export/` | `github.zip` in the shared Drive Projects folder |
| `fig-extracts/` | Re-derivable from any `.fig` with `tools/figextract.py` |
| **`carbonmade-originals/`** | **Only recoverable while stavfg.portfolio.site is up.** 15MB, 37 images. Carbonmade is being cancelled, so copy this folder across before that happens. |

The Figma files themselves live in the shared Drive folder `Projects`. On the old machine they were
also on the Desktop under `stav portfolio data`, about 1.9GB. Do not bother copying that; download
from Drive on the new machine instead.

**`RTC.fig`, `KGER.fig` and `A3 Registry Setup.fig` were never on the old machine at all.** Three of
the four case studies. They are in Drive.

---

## 5. Where things stand

**Done:** the site, its design system, two written case studies, the About and CV pages, the
accessibility pass, social metadata, the aerial defense diagram, the RTC threshold diagram, all
Carbonmade copy and imagery archived, both FigJam boards extracted, MSJ identified from its own
file.

**Chosen and unwritten:** four Salesforce case studies. Real-Time Semantic Classification,
KGER multi-intent email, A3 Registry, My Service Journey. They form one argument: teach it, assist
with it, govern it, get an organisation to adopt it.

**Blocked on Stav:** everything in her working doc. Link is in `notes/canonical-narrative.md` under
"Where things live".

**Blocked on nobody:** the prototypes-repo case study, drafted at `drafts/case-study-prototypes.md`,
needs three answers and no documents.

---

## 6. Rules that are not negotiable

**Confidentiality.** This repo is public. Never commit: internal service names, the roadmap, the
release-priority ordering, the competitor comparison from the A3 board, the anchor customer name,
or anything from `source-material/`. Before any push, check with
`git ls-files | xargs grep -il <term>`.

**Voice.** No triplets arranged for cadence. No X-not-Y contrasts. No em dashes. Never "passionate",
"leveraging", "robust", "delve", "testament", "tapestry", "unleash". Vary sentence length. Say each
thing once. Full list and the reasoning in `notes/canonical-narrative.md`.

**Interviewing.** One question at a time. Never a batched list. This is a firm preference.

**Ownership.** Do not use documentary ownership to judge what Stav led. Ownership rotates constantly
at Salesforce. If Ehud or Stav says she owned something, that is the fact.

---

## 7. First thing to do on the new machine

Run `./tools/setup.sh`, then check the site still builds and the live version matches:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://stav-fg.github.io
git log --oneline -5
```

Then open the working doc and see whether Stav has answered anything yet. Her answers are the
bottleneck for all four remaining case studies.

---

## 8. One outstanding cleanup

On 9 September a scan across every tracked file found the anchor customer named in
`notes/session-brief.md`, quoted from the handoff brief inside a sentence about not publishing it.
It was committed on 7 September and pushed, so it sat publicly readable on GitHub for two days.

The working file is fixed. **The commit history still contains it**, because the repo is public and
that commit is on origin. Clearing it means rewriting history and force pushing, which changes every
commit hash. Nobody else has cloned this repo so the practical cost is low, but it is destructive
and should be a deliberate decision rather than something done in passing. Ask before doing it.

**The lesson worth keeping:** the confidentiality scan has to run over `git ls-files`, not over the
HTML pages. Earlier scans only checked the site, so a notes file added afterwards went unchecked for
two days. Run this by hand before any push:

```
for t in Singapore DaVita soma.salesforce sbenshimongros; do
  echo "$t: $(grep -rilF "$t" $(git ls-files) | tr '\n' ' ')"
done
```
