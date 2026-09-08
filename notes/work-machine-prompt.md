# SUPERSEDED, do not run

The Claude on the work machine declined this, correctly. It asks a corporate assistant to
gather employer documents and move them to a personal Drive, which is the shape of data
exfiltration whatever the intent.

See `notes/sourcing-without-export.md` for what replaced it. Kept only as a record of what
was asked and why it was the wrong ask.

---

# Prompt for Claude on the Salesforce work machine

Copy everything below the line into a fresh Claude session on that machine.

---

I am a product designer at Salesforce. My last day is 30 September 2026, and after that I lose
access to everything here. I am building a portfolio and I need to get my own design work out
before then. Help me collect and export it.

Ground rules first, and they matter more than speed:

- Only export material I am permitted to take. My own design work and my own documents, not
  anyone else's confidential material, not customer data, not source code, not anything under a
  customer NDA.
- If you are unsure whether something is exportable, list it and ask me rather than exporting it.
- Do not redact anything. I will handle redaction later, and a document that has been pre-edited
  loses the detail that made it useful.
- If something on the list does not exist, say so explicitly. "Not found" is a useful answer and I
  need it recorded, not silently skipped.

**Where everything goes:** a single folder in my personal Google Drive, shared with
ehudfisher@gmail.com. Create subfolders per project. Tell me if you cannot write there and I will
do the moves manually.

---

## Task 1 — Figma exports. Highest value, do these first.

Figma files cannot be read by the person receiving them. They need **PDF**.

For each file: open it, then File > Export frames to PDF. It exports the current page only, so do
it per page for the pages that actually matter, and skip pages that are scratch or duplicates.
Name each PDF `<project> - <page name>.pdf`. PNG exports of individual frames are an acceptable
substitute if PDF is awkward, as long as filenames imply the order.

In priority order:

1. **RTC Flows** (FigJam) — the decision flows. Smallest and highest value.
2. **RTC** — Real-Time Semantic Classification. The multi-model training, comparison, decision and
   configuration screens. Do not export the whole file; export the pages that show the
   comparison and configuration surfaces.
3. **A3 Registry Setup**, plus **A3 Record Companion Registry** and **A3 Workshop** (FigJam)
4. **KGER**, and **Knowledge Based Email Reply** (FigJam)
5. **Embedded Agents** — for the agentic email work
6. **UT Case Summary** — if UT means usability testing, this is research and it is a priority
7. **AR4 Everything** (FigJam)
8. **Service Cloud / Service Catalog - Customer Research 2.0**
9. **254 Research for MSJ: Gamification Ranks** (FigJam)
10. **260 My Service Journey** and **256 + Vision - MSJ**
11. **_SLDS vs Kondo** — the design system evaluation

## Task 2 — Documents. Export as PDF or copy into the shared Drive folder.

Google Docs, Slides and Sheets can be copied or exported directly. For anything that is only a
**recording**, I do not need the recording, only its notes or transcript.

**Real-Time Semantic Classification**
- 262 Real Time Semantic Classification PRD
- 260 Real Time Case Classification
- Any earlier draft or copy of the 262 PRD, kept separate so the two can be compared

**KGER / MKGER**
- 260 KGER - Customer Intent Mapping PRD
- EK Support for KGER & MKGER - PBD, and the superseded OLD_ version, kept separate
- 264 Multi Intent Brainstorming - Chat
- KGER/Service Replies Blitz — notes only
- KGER Access Guard Issue

**Email Reply Automation / agentic email**
- Email Reply Automation - 264 PRD
- HLD: Agentic Email Response
- Agentic Email Reply
- Embedded Agents for Emails
- Automated Email — notes only
- <WIP> Service AI Agentic Automation Gen II - Product Framing

**A3 Registry / Record Companions**
- 264 - A3 Registry UI - PRD
- 260 Service Assistant Framework Extensibility PRD
- A3 Registry UI - Meeting with Legal — notes only
- A3 Registry Setup - Legal Discussion — notes only
- user-scoped-record-companions-design
- A3 Overview, A3 - Registry UI — notes only

**Wanted regardless of project**
- Embedded Service AI Ongoing UX — a presentation I authored. High priority.
- Copy of Work Handoff - Stav Fisher Gross — a spreadsheet I last edited in August

**Reserve, lower priority**
- Service Replies Multi-Intent Integration Proposal
- Service Replies Multi-Intent Detection PBD
- Proactive Service Replies PBD
- Service Replies - Split Setup for Chat & Voice PRD
- Service Replies - Handover
- Customizable Case Summary Structure PBD
- [Spring '26] Enhanced Summaries Enablement

## Task 3 — Search for things nobody has found yet.

A previous sweep of my Drive found no research readouts, no adoption or acceptance metrics, no
accessibility audits and no launch readiness documents. That may be because they are filed under
different words. Search Drive, Quip, Slack and any internal wiki for:

`readout`, `adoption`, `acceptance rate`, `edit rate`, `deflection`, `metrics`, `dashboard`,
`GA readiness`, `launch review`, `usability`, `research`, `study`, `findings`, `accessibility`,
`a11y`, `VPAT`, `QBR`, `business review`, `exec review`

Anything that attaches a number to any of these features is the single most valuable thing you
can find, because I have none. Paginate the searches; the earlier sweep did not.

I especially want:
- Adoption or usage: how many orgs or agents enabled a feature
- Acceptance rate: how often agents took an AI suggestion unedited
- Edit rate: how often they changed it
- Anything from a launch readout, QBR or exec review

## Task 4 — Things only I can write down.

Export anything **I** wrote that shaped a decision, even if it does not look like a design
artifact. Quip docs, long Slack messages, design rationale, critique notes, anything recording a
decision that got reversed. These are the easiest things to lose and among the most useful.

Also: my accessibility work. Any audit, standards document, review checklist or training material
I produced or owned.

## Task 5 — Report back.

When you are done, give me a single summary listing:
1. What you exported, by project, with the destination path
2. What you looked for and could not find, by name
3. Anything you found that I did not ask for but that looks relevant
4. Anything you did not export because you were unsure whether it was permitted

Item 2 matters as much as item 1. Knowing a thing does not exist lets me stop looking for it and
write around it instead.
