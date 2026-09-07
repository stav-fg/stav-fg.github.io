# The prototypes repo changes the argument

Found 7 September 2026, from `github.zip`.

**Handle with care.** This is Salesforce-internal source. It carries internal hostnames
(`an internal GitHub Enterprise host`), her internal username (`her internal username`), her Salesforce email, and
her employer's code. It is gitignored at `source-material/github-export/` and must never be
committed or published. Everything valuable about it can be described without shipping a line of it.

---

## What it is

A monorepo of Salesforce UX prototypes on the internal Design System 2 Starter Kit: LWC, SLDS 2,
Vite. Each prototype is a namespace under `src/modules/`, all served from one live internal URL.

The README describes the purpose in its own words: **"replacing static Figma deliverables with
interactive, ADLC-compliant builds."**

Scale: 110 source files, roughly 18,100 lines across 12 module namespaces.

## It covers five of the six projects

Previously the assumption was that no Salesforce material existed and both case studies started
from zero. That is wrong. Working, interactive prototypes exist for most of the six.

| Project in the brief | Prototype | Route |
|---|---|---|
| P6 Service Reply for Email | `sea` (KGER, Knowledge Generated Email Response) | `/cases/:id` |
| P6, drafting variants | `autoEmail`, `autoEmailSa` (Service Assistant, plan-driven) | `/automated-email(-sa)/:id` |
| P6 multi-intent version | `armidi` (AR Multi-Intent Detection) | `/setup/ar-midi`, `/ar-midi/cases/:id` |
| P2 Registry | `rcm` (Record Companions), setup plus a full-screen builder | `/setup/rcm`, `/rcm/:id` |
| P4 Service Replies | `sr` | `/setup/sr` |
| P5 Work / Handoff Summary | `workSummary`, `es` (Enhanced Summary) | `/setup/work-summary`, `/enhanced-summary/:id` |
| P1 Real-Time Classification | **absent** | — |

Real-Time Classification is the one gap, and it is the second case study. Worth asking whether a
prototype for it exists somewhere else before September closes.

## It is direct evidence for the claim that was hardest to prove

The positioning argument has three claims backed by fact and one that was going to be asserted in
prose: that she is an AI-fluent designer with a prototype-centric process. The build plan proposed
manufacturing evidence for it by rebuilding an old design as a working prototype.

That evidence already exists, and it is better than anything we could have built, because it is
real work for a real employer rather than a portfolio exercise.

In the repo:

- `CLAUDE.md` and `AGENTS.md` at the root, so the repo is written to be worked on by coding agents.
- `.agent/skills/` with authored skills (`repo-setup`, `first-time-deploy`).
- `mcp.json` declaring a Salesforce DX MCP server with the `lwc-experts` and `code-analysis`
  toolsets, and specifically the `guide_figma_to_lwc_conversion` tool.

A designer whose repo configures Figma-to-LWC conversion through an MCP server, and who writes
agent skills so the repo can be operated by an agent, does not need to claim AI fluency in a
paragraph. This is the artifact that proves it.

## What this changes

1. **The prototype idea gets easier and better.** The build plan called for rebuilding an old
   design "as she would do it now." She already does that at work, in production tooling. The
   portfolio piece is a sanitised rebuild of one of these, or a written account of how this repo
   replaced Figma handoff. Either beats an invented exercise.
2. **The two Salesforce case studies are no longer starting from zero.** There is real structure,
   real interaction design and real component work to describe, on top of whatever the interview
   surfaces.
3. **Section 6 needs an addition.** Not just "export the Figma files." Also: the prototype repo
   itself, its history, and any internal write-up of why prototyping replaced static handoff.
4. **The commit history is worth having.** This export is a fresh clone, so the local reflog has
   one entry, but the full history is in the packfile. Once git works on this machine,
   `git log --author` over this repo gives her authorship, cadence and volume, which is exactly
   the "commit history as evidence of process" argument the build plan wanted to make with the
   new portfolio repo. She has already been doing it for real.

## What cannot ship

- The source itself.
- Internal URLs, hostnames, usernames, email addresses.
- Anything naming the anchor customer.
- Screenshots that carry internal chrome, org names, or real case data, unless redacted.

What can ship: that she built interactive LWC prototypes on the internal design system, that they
replaced static Figma deliverables, that she configured agent tooling and Figma-to-LWC conversion
to do it, and a rebuilt, sanitised version of one flow with invented data.

That last one is the strongest single artifact available in this whole project.

---

## The commit history, read 7 September once git worked

84 commits on `main`, 175 across all refs. Sole author throughout: her, on her Salesforce address.
15 June to 30 July 2026, so roughly six and a half weeks. 513 file changes, 36,802 insertions,
13,759 deletions. Branches include a feature branch that was properly merged
(`feat/ar-midi-setup`) and a `gh-pages` branch for deploying the live prototype.

Weekly cadence: 26 commits in week 25, then 7, 12, 2, 2, 31, 4. Bursty, which is what real project
work looks like rather than a portfolio exercise.

The commit messages are the part worth reading. Conventional commits with scopes, and the content
is a designer making design decisions directly in the implementation:

- `feat(arMidi): 4px gap above intent count line`
- `feat(arMidi): widen knowledge panel to 470px, shrink middle column`
- `feat(arMidi): intent filter dividers + green/grey state icons`
- `feat(rcm/setupHome): align setup page + modal + active table with Figma`
- `feat(rcm): builder edit/save/activate flow, verified live`
- `fix(rcm): SPA 404 fallback so path-form deep links recover to hash route`

Three things a hiring manager would notice immediately. She is committing pixel-level refinements
herself rather than filing them as tickets. "verified live" recurs, so she was deploying and
checking her own work. And `fix(rcm): SPA 404 fallback so path-form deep links recover to hash
route` is not a design commit at all; it is a front-end engineering fix.

**This is the strongest single piece of evidence in the entire project.** The portfolio's central
claim is that she is an AI-fluent designer who works prototype-first and drives change. This is 84
commits of her doing exactly that, at work, unprompted, before any of this portfolio existed.

None of it can be published directly. What can be published: the shape of it. Commit counts,
cadence, the kinds of decisions, the fact that a designer owned the deploy. Possibly a redacted
excerpt of the log with internal names stripped.
