# Figma files are readable after all

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
