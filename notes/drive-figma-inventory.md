# Drive inventory — the Figma files

Folder: `Projects`, shared with ehudfisher@gmail.com.
https://drive.google.com/drive/folders/1GIZUU6nGSqM-Ldon3xOFs49h03nfS1P0
Inventoried 7 September 2026. Not yet downloaded.

**The export work is largely already done.** The brief lists "export all six Figma files" as the
headline September task. Most of it exists here already as `.fig` and `.jam` files. What remains
is verifying coverage, not doing the exports.

---

## Top level

| Folder | Maps to |
|---|---|
| `Service AI` | The Embedded AI area. Contains most of the six. |
| `RTC` | Real-Time Classification, project 1 |
| `MSJ` | My Service Journey. **Not in the brief at all.** See below. |
| `Case Management` | Unclear scope, one file |
| `A3` | Not yet opened |
| `Service Catalog - Build & Connect` | Not yet opened |
| `github.zip` | Already pulled and analysed, see `github-prototypes-finding.md` |

## Service AI

Loose files: `ECA Service Einstein GPT Agent Components (Copy) (Copy).fig`,
`Knowledge for Service Combined Experience.fig`

### AR — Article Recommendations, project 3
- `AR.fig`
- `Service AI Article Recommendations EAR.fig`
- `💬 Service AI Service Replies.fig`
- `AR4 Everything.jam`
- `KGER/` subfolder, **not yet opened**

KGER is Knowledge Generated Email Response, which the prototypes repo confirms is the engine
behind the lead case study. This subfolder is the highest-value unopened thing in the Drive.

### Auto-Email — project 6, Service Reply for Email
- `Embedded Agents.fig`
- `Knowledge Based Email Reply.jam`

### SR — Service Replies, project 4
- `💬 Service AI Service Replies.fig` plus two copies

### Summary — project 5, Work / Handoff Summary
- `🛠️ ✅ Unified Summaries Service AI.fig`
- `🛠️ Work & Case Summaries Service AI.fig`
- `UT Case Summary.fig` — "UT" almost certainly usability testing, which would make this a
  research artifact rather than a design file. Worth opening early.

### Service Analytics
Not yet opened. Possibly where metrics live.

## RTC — project 1, the second case study
- `RTC.fig`
- `RTC Flows.jam`

This fills the one gap in the prototypes repo, which had no Real-Time Classification module.
Between this and the repo, all six projects now have some material.

## MSJ — My Service Journey

A substantial project that appears nowhere in the handoff brief. Fourteen files, versioned by
Salesforce release:

`250 - MSJ - Spade & TTV.fig`, `252 - MSJ.fig`, `254 - MSJ.fig`, `256 + Vision - MSJ.fig`,
`260 - My Salesforce Journey.fig`, `MSJ - Components.fig`,
`250 Service Adoption - Jason.fig`, `[Service Cloud] Agentforce for Setup - Email to Case.fig`,
plus FigJam files: `MSJ 260+ Brainstorm.jam`, `MSJ - 250 - Spade.jam`,
`254 Research for MSJ_ Gamification Ranks.jam`

Three things stand out. It spans at least five release cycles, which is longer than most of the
six. It has a components file, meaning she built a design system for it. And it has genuine
research artifacts including gamification ranks research, plus vision work in `256 + Vision`.

**RESOLVED 7 Sep.** The Salesforce Drive index confirms My Service Journey is a 2022-2024 initiative
with different owners, unrelated to her Embedded AI work. Out of consideration. Original note kept
below for the record.

~~**Question for Stav:** what is MSJ, and why is it not on the list of six?~~ A project with vision
work, a component library and its own research across five releases may be a stronger case study
than some of the six. It should at least be a deliberate exclusion rather than an oversight.

## Case Management
- `Case Management.fig`

---

## What to do next

1. Open `Service AI/AR/KGER/`. Lead case study, highest value.
2. Open `UT Case Summary.fig`. If it is usability testing, it is the research evidence the brief
   says is missing.
3. Open `Service Analytics`. Most likely home of anything numeric.
4. Ask about MSJ, A3 and Service Catalog.
5. Download everything. It is in Ehud's Drive already, so it survives her losing access, but
   `.fig` and `.jam` files are Figma archives and need Figma to open. Confirm they still import.

## Caveat worth checking now, not in October

A `.fig` export is only useful if it opens. Import one into Figma this week and confirm it
restores with its pages, components and version history intact. Finding out in October that the
exports are broken would be the worst possible outcome, and it is a fifteen-minute check.

---

## Second pass, 8 September: two folders I had never opened

I listed A3 and Service Catalog in the top-level inventory and then never looked inside either.
Correcting that, and both change something.

### A3 — the Registry files exist after all

- `A3 Registry Setup.fig`, 122MB
- `A3 Workshop.jam`
- `A3 Record Companion Registry.jam` — **added 6 September**, weeks after everything else here,
  which suggests it is the most current thing in the whole Drive

My note in `document-requests.md` saying the A3 Registry file "was not in any folder I inventoried"
was simply wrong. It was in the A3 folder, which I never opened. The A3 case study is not missing
its design source.

### Service Catalog — much larger than the index implied, and it contains research

Nineteen files, several between 150MB and 210MB. Release numbers run 244 to 250, so it sits before
the Embedded AI work rather than years before it.

What is in there:

- **`Service Cloud _ Service Catalog - Customer Research 2.0.fig`** — customer research
- `Service Catalog - Screen library.fig` — a screen and component library
- `🍤 246 SOBA builder experience.fig` — a second builder experience, distinct from A3's
- `Service Cloud _ Self Service Workshop Assets.fig` — workshop material
- `250 - Catalog Item Access - UX review.fig` — a UX review
- **`_SLDS vs Kondo.fig`** — an evaluation of the Salesforce design system against an alternative
- `Eligibility Rules.fig`, `250 CSP planing.fig`, `Service Catalog Demo - Alpha insurance.fig`

The index excluded all of this as "old 2022-2024 initiatives, different owners", which is the same
reasoning that turned out to be wrong for MSJ.

## The "no research exists" alarm was half wrong

I raised the absence of any research, usability study or readout as the most important signal in
the document index. That still holds **for documents**. It does not hold for the Drive.

Research artifacts are here, they are just Figma and FigJam files rather than written reports:

- `Service Cloud _ Service Catalog - Customer Research 2.0.fig`
- `254 Research for MSJ_ Gamification Ranks.jam`
- `UT Case Summary.fig`, where UT is very likely usability testing
- `A3 Workshop.jam` and `Service Cloud _ Self Service Workshop Assets.fig`
- `AR4 Everything.jam`

So the correct statement is narrower and more useful: **her research was done on canvases, not
written up as reports.** That is common for designers and it is not a gap in her practice. It does
mean every research artifact needs a PDF export to be usable, and it moves those files up the
export priority list considerably.

It also means the second document sweep should look for readouts and metrics, but should not
expect to find research there.
