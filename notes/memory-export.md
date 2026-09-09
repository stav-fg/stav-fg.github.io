# Memory export

Claude's memory files are stored per machine and per project path, so they do not travel.
This is a copy of what they held on Ehud's Mac as of 9 September 2026. A fresh session on
another computer should read this file and re-save these as memories if it wants them to
persist locally.

---

## salesforce-ownership-records-unreliable.md

---
name: salesforce-ownership-records-unreliable
description: "Don't use document ownership or authorship records to judge what Stav owned at Salesforce — ownership rotates constantly. Trust Ehud's account instead."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4bd3fead-9072-4e0d-bc59-c8096868909a
  modified: 2026-09-07T17:47:38.579Z
---

On [[stav-portfolio-project]], never use "whose name is on the document" as evidence of what Stav
did or did not own. Ownership at Salesforce changes very frequently, so a PRD authored or owned by
someone else says nothing about whether she led the design. When Ehud says she owned a major piece,
take that as fact and stop looking for documentary confirmation.

**Why:** I excluded the MSJ project from case-study consideration on the grounds that the Drive
index showed "different owners". That was the wrong test and it nearly cost a candidate project
with a component library, vision work and its own research. Ehud corrected it directly.

**How to apply:** Rank candidate case studies by story quality and evidence richness, never by
documentary ownership. When ownership is unclear, ask Ehud rather than inferring from records.
The same caution applies to inferring project dates from file owners or folder metadata.

---

## stav-handoff-brief-doc.md

---
name: stav-handoff-brief-doc
description: "URL of the canonical Stav portfolio handoff brief, plus the reliable way to read a private Google Doc in this setup."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4bd3fead-9072-4e0d-bc59-c8096868909a
  modified: 2026-09-07T10:32:13.579Z
---

"Stav — Portfolio & CV Revival: Claude Code Handoff (v3, canonical)":
https://docs.google.com/document/d/1JBz4zb7uzwHzN7XaM8d9cEk1Rce6pCGow5qWE-zkgRc/edit

It is private, so WebFetch returns 401 and there is no Drive connector in this environment. The way that works: the Claude in Chrome extension against Ehud's Brave browser, navigating to the `/mobilebasic` variant of the doc URL and calling `get_page_text`. The normal `/edit` view renders to canvas and returns only UI chrome; the `export?format=txt` fetch hangs.

Used by [[stav-portfolio-project]].

---

## stav-portfolio-project.md

---
name: stav-portfolio-project
description: "Ongoing project — rebuilding Stav Fisher Gross's design portfolio and CV for big tech, driven by a canonical handoff brief in Google Docs."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4bd3fead-9072-4e0d-bc59-c8096868909a
  modified: 2026-09-07T10:31:58.138Z
---

Ehud (the user) is running a portfolio + CV revival for Stav Fisher Gross, a product designer with ~14 years of experience, targeting big tech (Google, Meta, Microsoft, Amazon, Apple). The canonical spec is [[stav-handoff-brief-doc]], a Google Doc that supersedes all earlier versions. Read that doc at the start of any session on this project rather than re-deriving.

Hard deadline: Stav's Salesforce access ends end of September 2026 (last day). At that point all metrics, usability findings, research artifacts and internal before/after states for her six Embedded AI projects become unrecoverable. Section 6 of the brief is the pull list. Nothing else in the project is time-boxed.

Track decision, confirmed 2026-09-07: IC, roughly 90% confidence, open to leadership. This keeps Webiks (not Asperii) as the third case study.

Build decisions already made: four case studies (Service Reply for Email as lead, Real-Time Classification, Webiks, Air Force as a "founded a design function" story); Paw Pal cut; coded site built with Claude Code, GitHub repo, GitHub Pages; plain ATS-safe single-column CV as a separate artifact. the anchor customer must not be named. the clinic client must be redacted from every clinic management screenshot.

**Why:** These were deliberate decisions, not defaults, and re-litigating them wastes the limited time before the access deadline.

**How to apply:** Treat the brief as the source of truth. Follow [[stav-working-preferences]] for all interviewing and copy.

---

## stav-working-preferences.md

---
name: stav-working-preferences
description: "How Ehud wants interviewing and copy handled on the Stav portfolio project — one question at a time, plain prose, a specific banned-word list."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4bd3fead-9072-4e0d-bc59-c8096868909a
  modified: 2026-09-07T10:32:05.164Z
---

On [[stav-portfolio-project]], and stated in the brief as a firm preference:

- Ask one question at a time. Never a batched list.
- Short, direct prose. No padding. No em dashes.
- Avoid AI tells: X-not-Y contrasts, triplet rhythms, question-answer crutches, "in today's landscape" openers, "all about" frames, overclaimed coinages.
- Never use: delve, tapestry, mosaic, testament, robust, leverage, unleash, "it is important to note", "in conclusion".
- Copy should sound like Stav, not like a portfolio template.

**Why:** The portfolio has to read as human work by an AI-fluent designer. Copy that reads as machine-generated undercuts the whole positioning argument. Batched questions produce thin answers.

**How to apply:** Applies to every message in project sessions, not only to the finished portfolio copy.

