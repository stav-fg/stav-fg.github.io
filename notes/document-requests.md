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

**Updated 14 September, from Stav.** The multi-model version above is the early design, not the
final one. After the July review she reworked the flow to fit the engineering team's capacity for
the release. The biggest change was supporting a single algorithm instead of selecting and training
several. That is why the export shows one algorithm and no comparison view: nothing is missing from
the export, the comparison was cut. The "which model do we trust" framing above, in the table and in
the 8 September correction, describes the early scope. In the final design the admin decides whether
to trust one model and how much it may do alone, per field. The scope cut belongs in the case study:
what the first version did, what changed under capacity, and what the final design uses as evidence
in place of a comparison. Dates on the page: 2025 to 2026, confirmed by Stav on 16 September.

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

**Updated 16 September, from Stav.** She joined KGER partway through, after its first release. The
2023 pilot, the original launch and the single-intent pipeline all predate her, so none of their
figures or decisions are hers to claim. That includes the pilot's helpfulness figure. Her part is
the move to multi-intent, the expanded view for managing intents and sources, the admin setup page,
and the design for the agent-based successor. Dates on the page: 2025 to 2026.

The single-intent starting point is what she inherited, which makes this a takeover story: a
feature built to answer one question in an email, redesigned to handle all of them. Her own answer
to what she would do differently: the real need was one click to a draft, and product pushed a
faster solution with manual article selection first.

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

1. ~~**`Embedded Service AI Ongoing UX`**~~ **WITHDRAWN 16 September, from Stav.** It was written
   for her by another designer while she was away, and she updated it when she came back. Her
   words in it are edits on someone else's document, so it is not a voice source. Do not chase it.
   The voice problem needs a different answer: her own Slack messages and DMs, where she argued a
   position in her own words, and her answers in conversation. Both are unedited and sound like
   her, which is the property the deck was wanted for and does not have.
2. ~~**`Copy of Work Handoff - Stav Fisher Gross`**~~ **DONE, received 16 September.** Ten products
   and about thirty epics across four product managers, with a prototype link against seven of
   them. It corrected the scope claim from six features to ten product areas across the site, the
   CV and this file's own framing.

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

---

## Received 23 September, from Stav

Five documents in Drive. Their contents stay out of this repo: they name customers and colleagues.

- **MSJ design and research record.** Settles the MSJ question. MSJ is an in-product feature
  discovery and adoption tool for Service Cloud admins. Stav co-designed it as an equal partner
  with a principal designer, October 2023 to November 2024. **Confirmed by Stav, 23 September:**
  she was a co-designer. The two of them worked closely together so the work could keep moving
  across the time difference, since the other designer is in San Francisco. Describe it as
  co-designed, never led alone. It has a 13-participant moderated
  concept evaluation whose findings map to shipped decisions (entitlement lock icon, branded
  feature names, recommendations held back until personal), plus post-launch adoption numbers.
  No study of the gamification concept exists. Take that as settled.
- **Enhanced Summaries usability test.** Her own unmoderated study, 10 participants, October 2025,
  two save/post workflows compared. The only task-based usability test in the whole body of work.
  Makes Summaries a real case study candidate, not a reserve.
- **UserTesting metrics export** behind the study above.
- **Project handoff brief.** Users, before-state, ownership split, hardest decision and first
  mistake for KGER, RTC, A3, MSJ and Service Catalog. Also shows the agentic email reply design is
  hers, as KGER's successor.
- **Adoption and metrics research.** KGER accept and edit rates were never instrumented, by design,
  so they cannot be requested. Customer-facing RTC usage numbers are a known telemetry bug. No
  CSAT or NPS exists for any of these features. Stop asking for all three.

Recommended line-up after this: RTC, KGER with the agentic successor folded in, A3 Registry, MSJ,
Enhanced Summaries. Email Reply Automation stops being a separate study. Service Catalog stays out.

**Also 23 September: usage dashboards** for MSJ, Service Email Assistant, KGER, MKGER, Work
Summaries and Enhanced Summaries, as screenshots in Stav's Drive doc "missing metrics". The numbers
are internal Salesforce data, so they are deliberately not copied into this public repo. Two things
to know before using them: every chart shows zero until tracking began (about February 2026), and
that ramp is not adoption growth. And for Enhanced Summaries, count summaries generated, not
configuration views.
