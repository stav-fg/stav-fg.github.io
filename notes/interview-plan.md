# Interview plan

Prepared 8 September, before Stav joins. Ordered so that if she has twenty minutes we get the
things only she can give, and if she has two hours we get the case study she will present.

**Rule, from the brief and it is firm: one question at a time. Never a batched list.** This
document is my running order, not a script to read out.

**Priority principle:** ask first for what is both cheap to answer and unblocks the most. That is
almost never the interesting question.

---

## Tier 0 — gating. Under five minutes, unblocks everything downstream.

These are one-line answers that currently hold up entire pieces of work.

1. **What is My Service Journey, and did you lead it?**
   Blocks the fourth case study slot. It is the largest body of design work in the Drive, the only
   one with a component library, a vision file and its own research, and the only candidate that
   is not dense operational software. One sentence decides whether it is in or Service Replies
   takes the slot.

2. **Webiks: Senior Product Designer or Product Designer?**
   Three sources, two answers, and the one that disagrees is LinkedIn, which is what a recruiter
   cross-checks. Blocks the CV.

3. **Which phone number is right?** Two versions on record, one digit apart.

4. **Asperii: did it end in 2021 or April 2022?** LinkedIn says April 2022, the CV and her site say
   2021. Blocks the CV.

5. **Which AI tools do you actually use, and for what?**
   Not a logo list. The current CV lists Adobe XD, Axure, InVision and Zeplin and no AI tooling at
   all, on a CV whose entire argument is AI fluency. This is the single most damaging section on
   it and the cheapest to fix.

6. **What did owning accessibility actually involve?** Standards, audit tooling, review gates,
   training others. Google and Microsoft screen for this explicitly and the site currently
   asserts it in one sentence.

---

## Tier 1 — the prototypes repo. Do this before the product case studies.

Why first: it is the only case study with no document dependency, its evidence is already
verified, and it is the piece I would put at the top of the portfolio. Everything needed is
three answers.

7. **What was actually broken before you built it?**
   The single most important question in the whole interview. The repo proves what she built. It
   says nothing about what it cost her beforehand. I want the concrete version: a specific thing
   that got built wrong from a Figma file, a review cycle that kept looping, a state nobody
   noticed was undefined until QA. Without this the case study opens on a solution.

8. **What changed after?** Did engineers use it, did review cycles shorten, did anyone else adopt
   the pattern, did it survive you leaving. One sentence of qualitative signal carries the whole
   section. "The PM stopped asking for a spec" would be enough.

9. **What would you do differently?** Was the monorepo the right shape, did the prototypes drift
   from production, did building in code cost you exploration breadth.

---

## Tier 2 — the case study she will present, in depth.

Pick one and go deep rather than covering four shallowly. She presents one study for 45 minutes
in a portfolio review, and only that one has to be excellent.

Default is **KGER / MKGER multi-intent**, unless she would rather present RTC.

Ask in this order, one at a time:

10. What was broken before this existed? Not "replies were slow." What an agent physically did
    with a multi-part customer email: where they looked, what they copied, how long it took.
11. Who was the user, specifically? The admin who configures it is probably a separate design
    problem worth naming.
12. What did you own, and what did PM and engineering own?
13. **What was the hardest design decision, and what did you choose against?**
    The obvious candidate is how much reasoning to surface by default. Every rejected alternative
    is interview currency.
14. What did you get wrong first, and what changed it? A reversed decision is worth more than a
    clean one.
15. **How did the design handle the model being wrong?** Confidence, correction, fallback, undo.
    This is the centre of the study. The agent signs their name to something they did not write.
16. What shipped, and what got cut?
17. What happened after launch? Acceptance rate and edit rate especially, because edit rate is a
    design metric and not just a model one.

---

## Tier 3 — the other three, lighter.

Same eight questions, but expect and accept shorter answers. These are evidence for the arc, not
studies she has to present.

- **Real-Time Semantic Classification.** Extra question: how do you make a model comparison legible
  enough that someone who is not a data scientist can choose, and live with the choice?
- **Email Reply Automation.** Extra question: what was the guardrail, and how does a person
  supervise something that has already replied to a customer?
- **A3 Registry.** Extra questions: what did legal actually object to, and what changed in the
  design because of it? A design constrained by legal review is rare and memorable, and nobody
  else will have it.

---

## Tier 4 — cross-cutting. Ask once, near the end.

18. **What changed in how you design because the material is probabilistic rather than
    deterministic?**
    The brief calls this the single most valuable answer in the whole interview and I agree. It is
    the thing a designer without AI experience cannot say. Protect time for it.
19. Sole designer across six teams: how did you triage? That is a leadership story whether or not
    the title says lead.
20. India, Israel and San Francisco: what did that force you to change about your process?
21. IC or leadership going forward? Recorded as 90% IC. Worth confirming directly with her rather
    than through Ehud.

---

## Things not to spend her time on

- Anything I can get from a document. Do not ask her to narrate a PRD.
- Anything already answered in the handoff brief.
- Metrics. She should look those up rather than recall them, and a wrong remembered number is
  worse than no number.
- The Air Force and Webiks studies, unless there is time left. Both are already drafted from real
  source material and need editing rather than interviewing.

## One thing to tell her rather than ask

The two case studies already on the site are written in my voice, not hers. That is expected at
this stage. The last pass before go-live is hers, and it is the pass that matters most.
