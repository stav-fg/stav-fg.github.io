# Document pick list

Written 7 September 2026 against the index of her Salesforce Drive. I have no access to that
Drive, so each item below has to be exported or shared deliberately.

**Format:** Google Docs, Slides, Sheets and PDFs are all readable. Recordings are not, but their
notes are. Export or copy into the shared personal Drive folder and I can read them directly.

**Redaction:** do not pre-redact. I would rather see the customer name and strip it myself than
have someone remove the detail that made the story.

---

## The pick: an arc, not four features

Confirmed 8 September: she worked on and led features across all of them, so ownership is not a
constraint and the only question is which stories are worth telling.

Three of these line up into a progression, and that changes what the portfolio is. Read together
they are not four AI features. They are one argument about how much authority a machine should
have, told at three points along the scale.

Corrected 8 September on RTC, which I had badly misread. It is not a field getting filled in. It
is multi-model and multi-variable training, comparison and decision, with configuration that
determines what populates each field. That is model-operations UX: the surface where someone
decides which model to trust and what its output is allowed to drive. Rare, hard, and visually
dense.

With RTC restored the four line up as one continuous argument.

| | Case study | The question it answers | Where authority sits |
|---|---|---|---|
| **1** | **Real-Time Semantic Classification** | Which model do we trust, on what evidence, and what does it get to fill? | A human **trains and chooses** |
| **2** | **KGER / MKGER**, multi-intent email reply | Will a person put their name on something a machine wrote? | AI drafts, a human **decides** |
| **3** | **Email Reply Automation**, agentic email | When do you let it send without asking? | AI acts, a human **supervises** |
| **4** | **A3 Registry / Record Companions** | What is the machine permitted to touch at all? | Humans **govern** what AI may do |

Teach it, assist with it, automate it, govern it. Four surfaces along one question: how much
authority does a machine get, and who decides. A designer who can say she designed all four, in
production, for enterprise support, has a thesis rather than a portfolio. That is the single most
valuable framing available in this project, and it is worth more than any individual case study
in it.

RTC also earns its place on craft rather than concept. The other three are largely about judgment
under uncertainty. RTC is the one with genuine interface complexity to show: comparison views,
variable configuration, and the mapping from model output to populated field. A portfolio needs at
least one study where the screens themselves are the evidence, and this is it.

### 1. Real-Time Semantic Classification — the training and trust problem
Multi-model, multi-variable training and comparison, then a decision about which configuration
runs, with each configuration determining what populates each field. The design problem is making
a model comparison legible enough that a non-data-scientist can make that call and live with it.

**Want, in order:**
1. ~~PDF export of `RTC.fig`~~ **DONE, found 9 September.** `Projects/new export/rtc` in Drive holds
   24 frames as PNG and PDF: empty state, toggle-on with activation toast, a five-step configuration
   modal with empty states, six training-in-progress frames, and the config record page in both
   Configuration Details and Models and Training. Uploaded 9 September and missed at the time
   because the folder was not re-checked after the first inventory. `RTC Flows.jam` is still worth
   a PDF, since the decision path is the story and I only have its text.
2. `262 Real Time Semantic Classification PRD`.
3. `260 Real Time Case Classification`, the sibling. Two releases means it evolved, and how it
   evolved is a large part of the story.
4. The earlier draft of the 262 PRD, to diff against the final for anything that got reversed.

### 2. KGER / MKGER — the trust problem
The customer email contains several separate asks. One click produces a grounded reply with its
sources. A second click opens every detected intent and the article behind it, and the agent can
drop an intent or swap a source. Speed on the surface, inspectable reasoning underneath, and the
tension between those two is the design problem.

**Want:** `260 KGER - Customer Intent Mapping PRD`, `EK Support for KGER & MKGER - PBD`,
`264 Multi Intent Brainstorming - Chat`, `KGER/Service Replies Blitz` notes,
`KGER Access Guard Issue`.

### 3. Email Reply Automation — the autonomy problem
The one I underweighted first time. Moving from "AI drafts, a human sends" to "AI sends" is the
highest-stakes decision in the entire area. What is the guardrail, when does it hand back, and how
does a person supervise something that has already replied to a customer? Almost nobody
interviewing at Google has designed that in production.

**Want:** `Email Reply Automation - 264 PRD`, `HLD: Agentic Email Response`, `Agentic Email Reply`,
`Embedded Agents for Emails`, `Automated Email` meeting notes,
`<WIP> Service AI Agentic Automation Gen II - Product Framing`.

### 4. A3 Registry / Record Companions — the governance problem
A registry deciding what AI actors may attach to which records, and what they may do there.
Admin and builder UX rather than agent UX, so it adds a different kind of design problem. It went
through legal twice, and `user-scoped-record-companions-design` suggests per-user scoping, which
means the legal conversation was probably about data access. Design under legal constraint is rare
and memorable.

**Want:** `264 - A3 Registry UI - PRD`, **both** legal documents,
`user-scoped-record-companions-design`, `260 Service Assistant Framework Extensibility PRD`,
the A3 meeting notes.

### Fifth, if the portfolio has room: MSJ, My Service Journey — the range piece

**Name, corrected 8 September.** MSJ is **My Service Journey**, not My Salesforce Journey. Worth
recording that the file in Drive is genuinely titled `260 - My Salesforce Journey.fig`, so either
the export is mislabelled or there are two different things under one abbreviation. Do not assume
the filename is the project.

**This is also the project the Salesforce Drive index explicitly excluded**, under
"everything under 'My Service Journey' ... old 2022-2024 initiatives, different owners". Two of
those three reasons are already known to be unreliable: ownership does not indicate what she led,
and the release numbers on the Figma files run 250 to 260+, which does not sit years before her
Embedded AI work at 260 to 264.

So the index says drop it and the file evidence says look again. That conflict is unresolved and
only Stav can settle it.
Everything else in the portfolio, including the older work, is dense operational software for
people at a console. MSJ appears to be something else: gamification ranks research, a component
library, a vision file, and `250 Service Adoption - Jason.fig` in the same folder, which suggests
it is about driving adoption rather than assisting a task. Motivating behaviour change is a
genuinely different design problem from helping someone finish a case.

It is also the largest body of work in the Drive by a wide margin: 355MB for the 260 file against
40MB for KGER.

**Want:** one sentence on what it is, then `260 - My Salesforce Journey.fig` and
`256 + Vision - MSJ.fig` as PDF, plus `254 Research for MSJ_ Gamification Ranks.jam`.

**Risk:** it is the only pick I cannot evaluate. If it turns out to be an internal onboarding
microsite, it drops and Service Replies takes the slot.

## Reserve

**Service Replies.** Strongest reserve, and first substitute if MSJ falls through.
`Proactive Service Replies PBD` is the interesting one: AI speaking unprompted is a real design
question. `Split Setup for Chat & Voice PRD` adds a modality nothing else in the portfolio has.
Also `Multi-Intent Integration Proposal`, because a proposal names the alternatives that lost.
In reserve only because its core overlaps KGER.

**Summaries.** The handoff angle is the good one: one human handing work to another through a
machine's summary of what happened. `Customizable Case Summary Structure PBD` and
`[Spring '26] Enhanced Summaries Enablement`.

**The prototypes repo.** Not competing for a slot. It is the method behind all four and should run
through them rather than sit beside them.

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

## MSJ is back in, and my reason for cutting it was wrong

I excluded MSJ because the index said "different owners". Ehud corrected the method: ownership at
Salesforce rotates constantly, so whose name is on a document says nothing about who led the
design. Documentary ownership is not a filter and should never have been used as one.

Re-examined on evidence that does not depend on ownership, and the exclusion does not hold:

**The release numbers overlap her current work.** MSJ files run 250, 252, 254, 256, 260 and a
"260+" brainstorm. Her Embedded AI documents run 260, 262, 264. Those are the same numbering
ladder and they meet at 260. MSJ is not a finished older initiative sitting years before her AI
work; it runs right up to it.

**There is Agentforce material in the folder.** `[Service Cloud] Agentforce for Setup - Email to
Case.fig` sits alongside the MSJ files. Agentforce is current-generation branding, not 2022.

**The files are enormous.** `260 - My Salesforce Journey.fig` is 355MB. `254 - MSJ.fig` is 230MB.
`252` is 213MB. For comparison, `KGER.fig` is 40MB. Whatever MSJ is, it is the largest body of
design work in the entire Drive by a wide margin, roughly five times the lead case study.

**It has a component library and a vision file**, which no other project here has.
`MSJ - Components.fig` and `256 + Vision - MSJ.fig`.

**And it has its own research**, `254 Research for MSJ_ Gamification Ranks.jam`, which makes it
the only project in the Drive with a research artifact attached.

Gamification also implies it is not another agent-console feature. The portfolio is currently four
variations on enterprise support tooling with no range anywhere. If MSJ is a different kind of
product, that is worth more than its size.

**What I need is one sentence from Stav about what MSJ actually is**, and whether she led it. Not
a document. On the current evidence it is a strong candidate and possibly the strongest, and I
cut it for a bad reason.

---

## Why the Figma files cannot be read here

Investigated 8 September rather than assumed.

`.fig` and `.jam` are zip containers. Unpacking `RTC Flows.jam` gives `canvas.fig`, `thumbnail.png`,
`meta.json` and an `images/` folder. So far so readable.

`canvas.fig` is then two length-prefixed chunks after a 12-byte header. The first is raw-deflate and
decompresses to the 72KB kiwi schema, which is just field and enum names and identical across files.
The second chunk starts `28 b5 2f fd`, which is **Zstandard**. That one holds the document: every
node, label, sticky and connector.

This machine has no route to zstd. No `zstd` binary, no `zstandard` Python module, no
`compression.zstd` on Python 3.9, no `libzstd` in the dyld shared cache, and `tar` was built without
it. Installing one needs Homebrew, which needs a sudo password.

**What did come out:** `thumbnail.png`, 370x400, a rendered preview of the whole board. For RTC
Flows it shows two parallel decision flows of roughly twenty-plus nodes each, with several branch
points and yellow sticky annotations. Too small to read, but it corroborates the description of
the project as genuinely complex rather than a field being populated.

**Conclusion:** PDF export from Figma is the only practical route, and it is a two-minute action
per file. Downloading the `.fig` files locally would add the thumbnail and any embedded raster
assets and nothing else, because the vector UI stays locked without zstd.
