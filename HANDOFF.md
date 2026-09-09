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

## 3. Setting up the machine

The next machine is a **PC**, so everything here is cross-platform. The old machine was a Mac and
several early steps used macOS-only tools. Those have been replaced.

**Install first.** Git and Python 3.8 or newer. On the PC this moved to, neither could be
installed the normal way, because that account has no admin rights and the python.org MSI fails
with `0x80070003`. What worked there, and what is on that machine now:

- **PortableGit 2.55.0**, unzipped to `%LOCALAPPDATA%\Programs\PortableGit`.
- **The nuget CPython 3.13 build**, unpacked to `%LOCALAPPDATA%\Programs\Python313`. The
  interpreter is at `...\Python313\tools\python.exe`.

On a machine with admin rights the normal installers are fine. Git for Windows is at
https://git-scm.com/download/win and Python at https://python.org.

**Then:**

```
git clone https://github.com/stav-fg/stav-fg.github.io.git stav-portfolio
cd stav-portfolio
%LOCALAPPDATA%\Programs\Python313\tools\python.exe tools\setup.py
```

On macOS or Linux that is `python3 tools/setup.py`.

**On Windows, call the interpreter by its full path.** Two shorter forms look right and both fail
here. `py tools\setup.py` needs the launcher, which only ships with the python.org installer. A
bare `python` resolves to the Microsoft Store stub, which is not an interpreter. Earlier versions of
this file gave each of them in turn, so if you find yourself editing this paragraph to shorten the
command, that is the mistake repeating.

After setup, use the environment's Python for everything: `env\Scripts\python tools\...` on
Windows, `env/bin/python tools/...` elsewhere. That one is stable, because `setup.py` builds it.

`setup.py` checks git and Python, builds the `env/` virtual environment from `requirements.txt`,
reports which source material is missing, and pings the live site. Safe to run repeatedly. It ends
by printing the exact command to run the Figma extractor on your platform.

**The Drive connector** is account-level, so it should already be there. If not, add it in Claude's
settings.

### The tools, and what they replaced

Everything in `tools/` is pure Python now. No Homebrew, no Xcode, no macOS utilities.

| Tool | What it does | Replaced |
|---|---|---|
| `tools/figextract.py` | Pulls text, thumbnail and metadata out of a `.fig` or `.jam` | Nothing, always portable |
| `tools/pdfpages.py` | Renders a PDF to one PNG per page and dumps its text | macOS PDFKit via `osascript`, and `sips` |
| `tools/setup.py` | Sets the machine up | A bash script that only ran on macOS |

Run them with the environment's Python, not the system one:

```
env\Scripts\python tools\figextract.py "RTC Flows.jam" source-material\fig-extracts
env\Scripts\python tools\pdfpages.py source-material\portfolio-panel-deck.pdf source-material\deck-slides
```

### Two macOS habits that will not carry over

Both are noted in the README and neither matters on Windows.

- **`qlmanage -t`** was used to render an HTML page to PNG without a browser, for checking layout.
  On Windows, just open the file in a browser, or ask Claude to screenshot it with its browser
  tools.
- **The Xcode Command Line Tools catch-22** cost an hour on the Mac. Irrelevant here; Git for
  Windows is a normal installer.

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
| `carbonmade-originals/` | **Backed up to Drive 9 September**, `Projects/carbonmade`. 37 images in three folders, verified against the Mac file by file. Safe to cancel Carbonmade. |

The Figma files themselves live in the shared Drive folder `Projects`. On the old machine they were
also on the Desktop under `stav portfolio data`, about 1.9GB. Do not copy that across; download from
Drive on the new machine instead.

**`RTC.fig`, `KGER.fig` and `A3 Registry Setup.fig` are in Drive and were never copied to the Mac.**
Not missing, just never fetched. Download from Drive on whichever machine needs them.

**RTC is no longer blocked on a Figma export.** `Projects/new export/rtc` in Drive holds a complete
24-frame export, each frame as both PNG and PDF, uploaded 9 September. Empty state, toggle-on with
activation toast, a five-step configuration modal with empty states, six training-in-progress
frames, and the config record page in both Configuration Details and Models and Training. That
satisfies item 1 of the RTC request in `notes/document-requests.md`.

### Nothing is left on the Mac

**Checked and closed 9 September 2026.** This section used to list material that existed only on
the Mac. It is empty now.

`carbonmade-originals/` was the one genuinely irreplaceable folder, recoverable only while
stavfg.portfolio.site was up, and that subscription is being cancelled. It is in Drive at
`Projects/carbonmade`, three subfolders, 37 files, counts verified against the Mac.

`fig-extracts/` is on the PC already. Everything else in the table above is re-derivable from Drive,
LinkedIn or the tools in `tools/`.

**The Mac can be wiped or handed back.** Confirm the repo is pushed first, which is the only thing
on it that is not also somewhere else.

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
or anything from `source-material/`. **Run the scan before every push**, using the environment's
interpreter:

```
env\Scripts\python tools\scan.py          Windows
env/bin/python tools/scan.py            macOS and Linux
```

It checks every tracked file against `.confidential-terms`, which is gitignored so the list of
blocked strings never enters the repo itself.

Do not shorten that to `python tools/scan.py`. On Windows it hits the Microsoft Store stub and exits
9009 without scanning, and 9009 is a shell "command not found" rather than a scan result. Anyone
gating a push on the exit code sees non-zero and may read it as the scan having found something.
That failure is at its most expensive here.

**Voice.** No triplets arranged for cadence. No X-not-Y contrasts. No em dashes. Never "passionate",
"leveraging", "robust", "delve", "testament", "tapestry", "unleash". Vary sentence length. Say each
thing once. Full list and the reasoning in `notes/canonical-narrative.md`.

**Interviewing.** One question at a time. Never a batched list. This is a firm preference.

**Ownership.** Do not use documentary ownership to judge what Stav led. Ownership rotates constantly
at Salesforce. If Ehud or Stav says she owned something, that is the fact.

---

## 7. First thing to do on the new machine

Run the setup script. It reports the site status and everything missing, so there is nothing else
to check by hand:

```
%LOCALAPPDATA%\Programs\Python313\tools\python.exe tools\setup.py
git log --oneline -5
```

Full interpreter path, the same as section 3, because `env/` does not exist yet on a new machine.
Building it is what this command does. Every later command uses `env\Scripts\python`.

Then open Stav's working doc and see whether she has answered anything yet. Her answers are the
bottleneck for all four remaining case studies:

https://docs.google.com/document/d/1xNr0xT6stFkhGRiLsXmBwKRRtkWI00vY0jzSaMDqoIE/edit

---

## 8. The customer name in git history, decided and closed

**Decision, 9 September 2026: leave it. Do not rewrite history. This is settled, not pending.**

On 9 September a scan found the anchor customer named in `notes/session-brief.md`, quoted from the
handoff brief inside a sentence about not publishing it. The working file was fixed the same day and
the tip has been clean since. A later scan across all 38 commits found the name in **24 of them**,
because it persisted through every commit that touched that file, plus two `HANDOFF.md` commits from
a second mistake where blocked terms were written into a grep example.

### Why leaving it is the right call

Rewriting was considered properly and rejected on the facts.

**A force push would not have removed it.** Orphaned commits stay reachable on GitHub by direct SHA
until GitHub garbage-collects on its own schedule. The destructive option buys less than it appears
to. Genuine removal means deleting and recreating the repo, or opening a support ticket.

**Deleting the repo costs something real.** The readable commit history is treated by the brief as
evidence of how the work was done. Trading that for a partial fix is a bad trade.

**Exposure is low.** Public repo, zero stars, zero forks, no inbound links, site is `noindex`, and
nobody has been told the repo exists.

**The tip is clean and gated.** `tools/scan.py` runs over `git ls-files` before every push, so
nothing new gets in. That is the control that actually matters going forward.

### Do not reopen this

If a future session rediscovers the name in history, this is the answer. It was found, assessed and
deliberately accepted by Ehud. Reopening it costs a day and changes nothing.

**What would change the decision:** the repo gaining traffic, being linked from her CV or LinkedIn,
being forked, or the site coming out of `noindex` with the customer relationship still sensitive. If
any of those happen, delete and recreate rather than force push, because only that removes it.

### The lesson worth keeping

The scan has to run over `git ls-files`, not over the HTML pages. Earlier scans only checked the
site, so a notes file added afterwards went unchecked for two days.

`tools/scan.py` does this properly now. It reads the blocked strings from `.confidential-terms`,
which is gitignored, because writing the terms into the repo would leak the very thing the scan
protects. That is a mistake I made once in this file and had to undo.

It has three exit codes, so a caller can tell the cases apart:

```
0   scanned, nothing found
1   scanned, found something. Do not push.
2   could not scan. Says nothing about whether the repo is clean.
```

Run it before every push, with the environment's interpreter. Section 6 has the command.
