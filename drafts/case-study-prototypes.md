# Draft: "I stopped shipping Figma files"

A case study that does not exist yet and probably should lead the portfolio. Reasoning is in
`notes/strategy.md`, section 2.

**Status:** everything below marked `[FACT]` is verifiable from the repo itself and needs no
interview. Everything marked `[ASK]` needs Stav. The page cannot ship until the `[ASK]` items are
answered, because without them this is a description of a repo rather than a design story.

**Confidentiality:** none of the source, internal hostnames, internal usernames or live URLs can
appear. What follows is written to be publishable as-is.

---

## Working title options

1. **I stopped shipping Figma files** — plain, and the strongest claim she can make.
2. **The handoff that stopped being a handoff**
3. **Eighty-four commits** — good if the commit history becomes a visual.

My preference is the first. It is a sentence a hiring manager repeats to a colleague.

## Fact bar

- **Role:** Product Design Lead, Embedded AI, Service Cloud
- **When:** June to July 2026 `[FACT]`
- **What:** A prototype monorepo replacing static design deliverables
- **Built with:** Lightning Web Components, the internal design system, Vite `[FACT]`

## Lead paragraph, draft

> Design handoff at enterprise scale is a stack of Figma frames and a document explaining what the
> frames mean. Engineers interpret it, something ships, and the gap between the two is discovered
> late. I replaced mine with prototypes that run: one URL, real components from the design system,
> every state clickable. Over six weeks I shipped eighty-four commits to it, and the last one was
> a bug fix.

## The argument

### What was wrong `[ASK]`
The repo proves what she built. It does not say what it cost her before she built it. This needs
the concrete version: a specific thing that got built wrong from a Figma file, or a review cycle
that kept looping, or a state nobody noticed was undefined until it reached QA.

Without this the case study opens on a solution. This is the single most important `[ASK]` here.

### What she actually did `[FACT]`
- A monorepo where each prototype is its own namespace, all served from one live URL, so reviewers
  get a link rather than a file.
- Prototypes covering five of the six projects in her area: the knowledge-grounded email reply and
  its two drafting variants, multi-intent detection, record companions with a full-screen builder,
  service replies, and work and case summaries.
- Built on the real design system rather than a redraw of it, so what reviewers clicked was made
  of the same components engineering would use.
- A deploy branch, so publishing was part of her own loop rather than someone else's.

### The AI-fluency part, which is the point `[FACT]`
This is where the claim stops being a claim.

- The repo carries agent instructions at its root, so it is written to be operated by coding agents
  and not only by people.
- She authored reusable skills for it, including repo setup and first deploy, which is
  infrastructure for other people rather than for herself.
- It declares an MCP server wiring in Salesforce's own developer tooling, including a
  Figma-to-code conversion tool.

A designer who configures Figma-to-code conversion through an agent server, and writes skills so
the repo can be driven by an agent, does not need a paragraph claiming AI fluency.

### The commit history as evidence `[FACT]`
84 commits on the main branch, 175 across all branches, sole author, 15 June to 30 July 2026.
36,802 insertions across 513 file changes. A feature branch, properly merged.

What the messages show, and this is the part worth quoting on the page:

- `feat(...): 4px gap above intent count line`
- `feat(...): widen knowledge panel to 470px, shrink middle column`
- `feat(...): intent filter dividers, green and grey state icons`
- `feat(...): align setup page, modal and active table with Figma`
- `feat(...): builder edit/save/activate flow, verified live`
- `fix(...): SPA 404 fallback so path-form deep links recover to hash route`

Three things a reviewer notices. She commits pixel-level decisions herself instead of filing them
as tickets. "Verified live" recurs, so she deployed and checked her own work. And the last one is
not a design commit at all.

### What it changed `[ASK]`
The hole in the middle. Needed: did engineers actually use it, did review cycles shorten, did
anyone else adopt the pattern, did it survive her leaving. Even one sentence of qualitative
signal. "The PM stopped asking for a spec" would carry this whole section.

### What she would do differently `[ASK]`
The deck ends both its case studies this way and it is what interviewers probe for. Candidates:
whether the monorepo was the right shape, whether prototypes drifted from production, whether
building in code cost her exploration breadth.

## Why this leads

Every other case study answers "what did you do." This one answers "what would you be like to work
with next year," which is the question a hiring manager is actually asking.

It is also the only piece from 2026. Without it, two thirds of the visible portfolio predates 2019
and the two recent studies are the two that are unwritten. One current piece at the top reframes
the older work as where she came from rather than what she does.

And it needs no metrics. Everything load-bearing here is verifiable from a repo that already
exists, which makes it the only case study not blocked by the 30 September deadline.

## Visual options

1. **The commit log**, redacted. A rendered list of messages with scopes stripped. Unusual on a
   design portfolio and immediately legible.
2. **A cadence chart.** 26 commits in week 25, then 7, 12, 2, 2, 31, 4. Bursty, which is what real
   project work looks like.
3. **A sanitised rebuild** of one flow with invented data, embedded live. Most work, most payoff,
   and it doubles as the "prototype rebuild" the build plan already wanted.

Option 3 is the one that makes the piece unarguable, because the reader can click it.

## Risks

- **Employer sensitivity.** The framing has to be about her practice, never about Salesforce's
  roadmap. No internal names, hosts, URLs or customers.
- **Overclaiming.** She did not invent prototype-driven design. The claim is that she did it, at
  scale, inside a large organisation, against the grain of an existing handoff process. That is
  enough, and it is true.
- **Engineers reading it.** Some will look at LWC prototypes by a designer and be sceptical. The
  commit history handles that, which is a reason to show it rather than describe it.
