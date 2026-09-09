# Session brief, 7 September 2026

Everything done in one working session, written for a debrief. Ordered so the things needing a
decision come before the things that are just done.

---

## 1. Decisions I made that you should review

These are judgment calls, not tasks. Each is reversible and each could reasonably have gone the
other way.

**I did not publish the aerial defense screenshots.** The deck's before/after pair is the clearest
design argument in her whole record and it is redacted to the XXXX standard. But it still shows
real map geography with legible place names, response timings, and impact-ellipse geometry. That
is exactly the category the declined security-officer recommendation covered, and a private slide
deck is not the same risk as a public URL under her real name. I drew an abstract diagram of the
same design change instead. If you disagree, the screens are in `source-material/deck-slides/`.

**I authored the repo commits as Stav, with Claude as co-author.** You asked for her name. Git's
author field is who the work belongs to and `Co-Authored-By` records who did it, so the history is
hers and honest at the same time. The caveat stands: do not point at *this* repo's history as
evidence of her process, because the commits are ours. She has 84 real ones that do the job better.

**I pulled all source material out of the repo before the first push.** A `<user>.github.io` Pages
repo must be public. The commit as it stood would have published the handoff brief, which contains
the anchor customer named outright, alongside an instruction never to name them, the client-name redaction problem, her
contact details and the full strategy, plus the deck with unredacted clinic screenshots. Notes and
drafts are tracked but sanitised of internal identifiers.

**I removed the two Salesforce case study pages rather than shipping them.** With the draft
callouts stripped, they were headings and unanswered questions. Their scaffolding is in
`notes/interview-scaffold.md`. They remain listed on the index, marked and unlinked, because
omitting the Salesforce work entirely would make a fourteen-year career look like it stopped in
2018.

**I left the two lorem ipsum screens out of the Aircraft Maintenance study**, and removed three
section headings that lost all their content in the strip. Both recorded rather than quietly
dropped.

**I put a noindex on the site.** It went live before a go-live date exists, and an unfinished
portfolio cached under her real name is all downside. Comes off in one commit.

---

## 2. What I found that changes the plan

**The prototypes repo is the strongest evidence in the project, and the brief does not know it
exists in this form.** 84 commits on main, 175 across branches, sole author, 15 June to 30 July
2026, 36,802 insertions. A monorepo replacing static Figma handoff with interactive LWC builds on
the internal design system. Root-level agent instructions, authored agent skills, and an MCP server
declaring a Figma-to-code conversion tool. Commit messages that are pixel-level design decisions
made directly in the implementation, plus a front-end routing fix.

The build plan proposed manufacturing evidence of AI fluency by rebuilding an old design. That
evidence already exists, is from this year, is real employer work, and needs no metrics.
Full analysis in `notes/github-prototypes-finding.md`, draft case study in
`drafts/case-study-prototypes.md`.

**Most of the September Figma work is already done.** The Drive folder holds `.fig` and `.jam`
exports covering Service AI, RTC, Case Management and MSJ. They are in your Drive, so they survive
her losing access. Inventory in `notes/drive-figma-inventory.md`. Three folders remain unopened,
including KGER, which sits behind the lead case study.

**MSJ is a project nobody has mentioned.** Fourteen files across five Salesforce release cycles,
with a component library, vision work and gamification research. Larger than some of the six.

**Five brief corrections.** Drill Management is Webiks work, not Air Force service work, so it
cannot be the proof artifact for case study 04. The Carbonmade dates in section 4b are upload
dates, not project dates, and are wrong by up to four years. Paw Pal is already gone from the live
site. The Webiks slot is far cheaper than assumed because two written case studies already exist
for it. All in `notes/open-questions.md`, section E.

---

## 3. The strategic argument, which is the thing most worth debriefing

Written up properly in `notes/strategy.md`. Three claims:

1. **The job search has the same deadline as the artifact pull, and it is not in the plan.**
   Referrals and internal advocacy decay from the day she leaves. None of it waits for the
   portfolio. Her LinkedIn is the highest-traffic artifact she owns, is 4.5 years stale, and
   currently says she leads the design team at Asperii. Fixing it is an afternoon and outranks
   every remaining portfolio item.
2. **The metrics hunt should be looking for three usable numbers, not forty.** An interviewer
   cannot verify a figure from a previous employer and knows it. What numbers buy is a concrete
   case study and proof she was close to the outcome. Where nothing exists, change the sentence:
   a stated absence survives questioning, a vague quantitative claim does not.
3. **Effort should not be spread evenly across four case studies.** She presents one for 45
   minutes. Make Service Reply for Email genuinely deep and let the others be competent and short.

I also flagged that cutting Paw Pal, which was correct on quality, leaves a portfolio that is
entirely dense enterprise and military desktop software with no consumer or mobile range.

---

## 4. What I built

**The site**, live at `https://stav-fg.github.io`, static, no build step, no dependencies.
Six pages, 42 tracked files, 5.9MB. Pages weigh 5 to 13KB.

- Two written case studies, drafted from real source material.
- About and CV pages, which did not exist while the nav linked to them.
- A design system in one tokenised stylesheet, light and dark.
- An SVG diagram of the aerial defense ellipse change, themed and described.
- Open Graph metadata and a 1200×630 card drawn from the site's own type.
- A favicon built from the live-threat ellipse rather than a monogram.
- A 404 page.

**The tracker**, at `https://claude.ai/code/artifact/ecc654d3-6f79-4c26-9e2f-777f07f1b718`.
Four phases ordered by what expires first, three states per row because "confirmed this does not
exist" is a real answer, notes per row for holding a number when she finds one, and a countdown.
Private until shared.

**The working record**, all in `notes/` and `drafts/`.

---

## 5. Accessibility work, and why it got priority

Accessibility ownership is one of the three positioning claims. A reviewer at Google or Microsoft
who runs a contrast checker over her portfolio and finds failures does specific damage to a
specific claim.

Audited every token pair used in the stylesheet. `--ink-faint` failed WCAG AA in both themes:
3.60:1 on ground and 3.30:1 on hovered rows in light, 4.07 and 3.74 in dark. It carries eyebrows,
metadata, captions and hints, so that is real text failing. Solved for replacements preserving
hue. Everything now passes 4.5:1.

Also verified: heading order with no skipped levels, one `h1` per page, landmarks present, `lang`
set, skip link with a real target, no duplicate ids, no vague link text, `aria-current` on nav,
visible focus states, reduced-motion honoured, alt text and intrinsic dimensions on images.

---

## 6. Things I got wrong and had to redo

**I downloaded her entire image library incorrectly.** I asked the CDN for a 4000×4000 box, which
pads and upscales every asset into a square. All 37 came back square, none at its true aspect
ratio. Fetching the bare asset id returns the real original. Refetching also revealed that six of
eleven files per project were the same background texture repeated byte for byte, so "37 images"
was really 18. Payload went from 20.3MB to 5.7MB.

**My own callout-stripping script broke three sections.** Removing the draft callouts from the
Aircraft Maintenance page left "Who I was designing for", "Results" and "Takeaways" as headings
with nothing beneath them. Caught on a structural scan, not by looking, which is the lesson.

**The Open Graph card took three attempts.** Quick Look renders HTML at its own aspect and upscales
a non-square SVG to fill, so both early versions cropped badly. Fixed by making the source SVG
square with the card in the centre band.

**The Command Line Tools install.** Your first `xcode-select --install` left a stale lock file that
made every later attempt a silent no-op. I cleared it, which then broke the headless install,
because the package only appears in `softwareupdate --list` while that marker exists. Recorded in
the README so nobody loses an hour to it twice.

---

## 7. What I deliberately did not do

- **Write any Salesforce case study content.** No source material exists and inventing it would
  poison the interview.
- **Publish the aerial defense screens.** See section 1.
- **Touch her live Carbonmade site**, which still has unedited template text on it.
- **Push anything without checking.** Every push was preceded by a scan for internal identifiers,
  customer names and contact details.
- **Place the drill and clinic imagery.** Neither is a planned case study, so their 13 images sit
  unused in `assets/` pending a decision on the case study set.

---

## 8. Where things stand

| Thing | State |
|---|---|
| Site | Live, noindexed, 8 commits |
| Case studies written | 2 of 4, both needing her voice |
| Case studies unwritten | 2, blocked on interviews |
| Case study proposed | 1, the prototypes repo, drafted and unblocked |
| CV | Drafted, 7 open decisions |
| LinkedIn | Untouched, and it is the priority |
| Tracker | Published, private, needs sharing with Stav |
| September pull | Not started |
| Interviews | Not started |

**The three things I would do first when you are back:** confirm the strategy call about the job
search track, share the tracker with Stav, and get her LinkedIn fixed this week.
