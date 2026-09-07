# Document pick list

Written 7 September 2026 against the index of her Salesforce Drive. I have no access to that
Drive, so each item below has to be exported or shared deliberately.

**Format:** Google Docs, Slides, Sheets and PDFs are all readable. Recordings are not, but their
notes are. Export or copy into the shared personal Drive folder and I can read them directly.

**Redaction:** do not pre-redact. I would rather see the customer name and strip it myself than
have someone remove the detail that made the story.

---

## The seven candidates

Four to build, three in reserve. Chosen for minimum overlap, because four studies of "AI suggests
something to an agent" reads as one study told four times.

| # | Case study | Why it earns a slot | Docs exist? |
|---|---|---|---|
| 1 | **KGER / MKGER — multi-intent email reply** | The trust problem. One click on the surface, inspectable reasoning underneath. She is confirmed UX Lead. | Strong |
| 2 | **A3 Registry UI / Record Companions** | Admin and builder UX, not agent UX. Different design problem, and it went through legal twice. | Strongest |
| 3 | **Real-Time Semantic Classification** | A wrong answer here is silent. It looks like a filled-in field and propagates. Confirmed UX Lead. | Good |
| 4 | **The prototypes repo** | Method rather than product. Needs no documents at all. | N/A |
| 5 | Service Replies multi-intent | Richest doc cluster of any project | Very strong |
| 6 | Enhanced / Work Summaries | Personalisation and customisable structure | Strong |
| 7 | Embedded / Agentic Email | She authored the framing deck herself | Good |

Reserve is 5, 6, 7. Reasoning for the cut in the response.

---

## 1. KGER / MKGER — multi-intent email reply

**Want, in order:**
1. `260 KGER - Customer Intent Mapping PRD` — she is UX Lead on it. Establishes ownership and the problem.
2. `EK Support for KGER & MKGER - PBD` — defines the multi-article variant, which is the harder design and the better story.
3. `264 Multi Intent Brainstorming - Chat` — brainstorming is where rejected directions live, and rejected directions are what interviewers ask about.
4. `KGER/Service Replies Blitz` notes — a blitz usually means a compressed decision session.
5. `KGER Access Guard Issue` — a security constraint that shaped the design. Small, possibly a great detail.

**Skip:** the superseded `OLD_` version, unless the diff between old and new shows a reversal.
If it does, it is suddenly the most valuable document in this list.

## 2. A3 Registry UI / Record Companions

**Want, in order:**
1. `264 - A3 Registry UI - PRD` — the core.
2. `A3 Registry UI - Meeting with Legal` **and** `A3 Registry Setup - Legal Discussion` — both. Design constrained by legal review is unusual, memorable, and something almost no competing portfolio will have.
3. `user-scoped-record-companions-design` — a design doc written by someone else about her area shows how the team worked.
4. `260 Service Assistant Framework Extensibility PRD` — the umbrella, for framing only.
5. `A3 Overview` and `A3 - Registry UI` meeting notes.

**Skip for now:** `Salesforce A3 Architecture`, unless the case study ends up being about the
constraints the architecture imposed.

## 3. Real-Time Semantic Classification

**Want, in order:**
1. `262 Real Time Semantic Classification PRD` — she is UX Lead.
2. `260 Real Time Case Classification` — the sibling. Two PRDs across two releases means the thing evolved, and how it evolved is the story.
3. The earlier draft of the 262 PRD, **only** to diff against the final.

This is the thinnest of the four. If nothing here shows a design decision rather than a
requirement, swap it for Service Replies.

## 4. The prototypes repo

Nothing needed. Draft is at `drafts/case-study-prototypes.md`. Blocked only on questions for her.

---

## Reserve

**Service Replies (5).** Want `Service Replies Multi-Intent Integration Proposal` and
`Service Replies Multi-Intent Detection PBD` first. A proposal names alternatives, which is the
most useful document type there is. Also `Service Replies - Handover`, which usually says what
shipped and what did not. Held in reserve only because it overlaps heavily with KGER.

**Summaries (6).** Want `Customizable Case Summary Structure PBD` and
`[Spring '26] Enhanced Summaries Enablement`. Enablement decks are written to explain a feature to
people who did not build it, which makes them unusually good source material.

**Embedded Email (7).** Want `Embedded Service AI Ongoing UX`, which she last edited herself in
November 2025, and `<WIP> Service AI Agentic Automation Gen II - Product Framing`.

---

## Two documents I want regardless of which studies get built

1. **`Embedded Service AI Ongoing UX`** — a presentation she authored and last edited. Her own
   framing of the whole area, in her own words. That is the single best source for getting the
   portfolio into her voice, which is currently the largest quality gap in everything written.
2. **`Copy of Work Handoff - Stav Fisher Gross`** — a spreadsheet she last edited in August 2026.
   A handoff document is an inventory of everything she owned, written by her, at the end. It is
   probably the fastest route to an accurate scope claim on the CV.

---

## What the index does not contain, and it matters

Nothing in it is:

- a usability study or research readout
- an adoption, acceptance or edit-rate number
- an accessibility audit
- a launch readiness or GA readout
- a QBR or exec review deck

Those are the September deadline items. Their absence from this sweep is the single most
important thing the index tells us, because it is possible they do not exist, and it is better to
know that in the first week of September than the last.

**Worth a targeted second pass** on: `readout`, `adoption`, `metrics`, `dashboard`, `GA`,
`launch review`, `usability`, `research`, `study`, `accessibility`, `a11y`, `VPAT`, `QBR`,
`business review`. Plus paginating the earlier sweeps.

---

## Corrections to earlier notes

**MSJ is out.** I flagged "My Salesforce Journey" as a possible hidden strong project across five
release cycles. The index resolves it: My Service Journey is a 2022 to 2024 initiative with
different owners, unrelated to her Embedded AI work. Same for Service Catalog. Both removed from
consideration. `notes/drive-figma-inventory.md` and `notes/strategy.md` say otherwise and are now
wrong on this point.
