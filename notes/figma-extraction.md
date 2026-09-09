# Figma files are readable after all

**Snapshot, written 8 September 2026 on the Mac, kept as a record of how this was worked out.**
The commands below hand-build a venv because that is what was done at the time. Do not follow them
now. `tools/setup.py` builds `env/` from `requirements.txt`, which includes `zstandard`, and
`HANDOFF.md` section 3 has the current invocation for each platform. Anything here that reads as a
statement about "this machine" is about the Mac.

Written 8 September, correcting what I told you earlier.

## I gave up too early

I reported that `.fig` and `.jam` could not be read here, because the document chunk is
Zstandard-compressed and this Mac has no `zstd` binary, no `libzstd` in the dyld cache and no
`compression.zstd` on Python 3.9. All of that was true. The conclusion was not.

`pip` works. `python3 -m venv env && ./env/bin/pip install zstandard` takes about fifteen seconds
and installs a C-extension build. The blocker was fifteen seconds of effort, and I spent longer
than that writing up why it was impossible.

## The pipeline

`tools/figextract.py`. Unzips the container, skips the deflate schema chunk, zstd-decompresses the
document chunk, and pulls UTF-8 text runs out of the kiwi encoding.

```bash
python3 -m venv env && ./env/bin/pip install zstandard
./env/bin/python tools/figextract.py "A3 Record Companion Registry.jam" source-material/fig-extracts
```

Gives labels, the thumbnail and the metadata. It recovers **text**, not layout, so a PDF export is
still better where the visual arrangement is the point. But for FigJam boards, where the text is
almost the whole content, this is close to complete.

Verified on two files: `RTC Flows.jam` gave 75 usable labels, `A3 Record Companion Registry.jam`
gave 334.

## What this changes

**FigJam boards can come straight through Google Drive.** They are small enough to download with
the Drive connector. `A3 Record Companion Registry.jam` is 293KB and came through in one call.

**The large `.fig` files still need a hand.** 122MB to 355MB is far past what the connector will
return. Those need downloading onto this Mac, after which the same script reads them. Or a PDF
export, which additionally preserves layout.

So the revised ask is smaller than the one I sent to the work machine: **PDF export matters for
the `.fig` design files. The `.jam` boards I can simply take.**

## Confidentiality, and this is the important part

The extracts are Salesforce-internal and several categories in them are more sensitive than
anything encountered so far:

- unreleased product names and a named release-priority list
- platform architecture across four layers, including internal service names
- a competitive analysis naming HubSpot, Zendesk and Freshdesk with an assessment of each

None of that can go in this repo, which is public because Pages requires it. The extracts live in
`source-material/fig-extracts/` and are gitignored along with everything else in
`source-material/`. Verified with `git check-ignore`.

The case studies can describe her design decisions without any of it. What must never appear:
internal service names, the roadmap, the release-priority ordering, and the competitor assessment.

## What the two boards actually contain

Summarised deliberately at a level that is safe to publish. Detail is in the gitignored extracts.

**RTC Flows** is four versions of one configuration flow, two of them dated and one labelled as
responding to meeting feedback. That is an iteration story with its own evidence, which is exactly
what the case study needed and what I had assumed did not exist. The flow branches on whether
historical data exists, routes to a predictive path or a cold-start path, and ends in threshold
configuration. There are two thresholds, not one: a higher bar for acting automatically and a lower
bar for routing to a human instead. It also carries an open question the team had not resolved.

That two-threshold design is worth noting on its own. It is the authority argument of the whole
portfolio, expressed inside a single screen: act alone above here, ask a person in between, do
nothing below.

**A3 Record Companion Registry** is an end-to-end admin flow in five labelled phases, from an empty
state through a four-step configuration modal, persistence, a management list view, and runtime
behaviour. It names two explicit safety features. It sits inside an architecture diagram spanning
four layers, includes a worked concrete example, and ends in a competitive analysis.

It was created on **6 September 2026**, which makes it the most recent artifact anywhere in this
project, and it is the single best-documented case study candidate we have.

---

## MSJ resolved, 8 September, from the file itself

Extracted `254 - MSJ.fig`: 12,968 labels. No longer a guess.

**My Service Journey is a guided adoption and maturity product inside Service Cloud.** Its own
copy: *"Discover Service capabilities personalized to your business needs that take your Service
Cloud implementation from good to great. Simply select your business goal and service area to get
started."* And: *"Unlock the full potential of your Service org."*

What is in it:

- Best-practice **journey maps**, chosen by business goal and service area
- **Capability progress**, engagement progress and journey map progress, tracked separately
- A **badge system**: capability badges, business goal badges, business outcome badges, and a
  freemium versus paid badge
- **"Climb the ranks"** — the gamification the research file was about
- Progress rings and progress indicators throughout
- Specific recommended capabilities, for example accessible home pages, article suggestions,
  incident-related deflection, article effectiveness measurement
- **AI Capabilities Adoption** and **AI Initiatives Adoption** as tracked categories

### The name mystery is also solved

One label reads: **"From my Service Journey to my Salesforce Journey"**. Both names are real. The
product started as My Service Journey and was expanding in scope to cover Salesforce more broadly,
which is why the 260 file is titled My Salesforce Journey while the project is MSJ. Not a
mislabelled export. A rename in progress.

### What this means for the portfolio

It is the range piece, confirmed, and it is a better one than hoped.

Every other candidate is an agent at a console being helped by AI. This is B2B adoption design:
persuading an organisation to change what it does, personalised recommendation against stated
business goals, progression and motivation mechanics, and a freemium boundary sitting inside the
experience. Different users, different problem, different evidence of range.

It also has a research artifact attached, `254 Research for MSJ: Gamification Ranks`, which makes
it one of the few with research we can point to.

**Recommendation: it takes the fourth slot**, and the four become teach it, assist with it,
govern it, and get an organisation to adopt it. Email Reply Automation moves to reserve, since it
overlaps KGER on subject matter where MSJ overlaps nothing.
