# Open questions and unresolved conflicts

Everything here needs a human answer. Nothing here is blocked on me.
Grouped by who can answer it and how urgent it is.

---

## A. Blocked on Salesforce access. Deadline end of September 2026.

The only genuinely time-boxed work in this project. Everything in sections B through E can
happen in October or later.

1. Every metric in Section 6 of the brief, for all six projects. Adoption, acceptance rate,
   edit rate, time saved, deflection, volume, CSAT.
2. Usability findings, recordings, notes.
3. Before-state documentation of the agent workflow.
4. Design critique notes, especially anything recording a reversed decision.
5. All six Figma files, exported whole, including rejected explorations.
6. Accessibility audits, standards docs, review checklists.
7. Any document she wrote that changed a decision.

Not in the brief, added 7 Sep, same deadline:

8. LinkedIn recommendations from Salesforce colleagues. Ask while she is still there.
9. Personal contact details for anyone whose recollection might be needed in October.

---

## B. Answerable in one conversation with Stav. Not blocked on anything.

10. **Webiks title.** Senior Product Designer or Product Designer? The old CV says Senior. Her
    live portfolio About page says Senior. Her LinkedIn says Product Designer. Whichever is
    right, all three have to agree, and LinkedIn is the one a recruiter cross-checks.
11. **Phone number.** The brief has [phone, variant]. Her live site has [phone].
12. **AI tooling.** Which tools she actually uses and for what. The current CV lists Adobe XD,
    Axure, InVision and Zeplin, and no AI tooling at all, on a CV whose whole argument is AI
    fluency. This is the most damaging single section on the CV and the cheapest to fix.
13. **Accessibility specifics.** Which standards, which audit tooling, what the review gate was,
    whether she trained others. Google and Microsoft screen for this explicitly.
14. **Spanish.** Listed on the live site, absent from the brief. Still accurate?
15. **Aircraft Maintenance personas.** She ran the interviews and the base visits. The Clinic
    study has a proper user-characteristics matrix and this one has nothing. Recall, not research.
16. **Aircraft Maintenance outcome.** No results section exists. Eight years on, a qualitative
    account is the realistic ceiling, and it still beats stopping at the solution.

---

## C. Decisions only Ehud and Stav can make.

17. **The one number for the Air Force study.** "Response times have improved" is the
    load-bearing sentence and the weakest one on the page. If any figure was recorded, or even a
    remembered order of magnitude, it changes the study. If none exists, say so plainly. Vague
    claims get picked at; stated absences do not.
18. **Air Force confidentiality.** The recorded position is "limited to what has appeared in news
    coverage." The standing recommendation, declined so far, is a security officer review and
    describing the problem class rather than the mechanics. Worth noting that her existing public
    site already names her unit on its About page, and the deck's aerial defense screens are
    already redacted with placeholders. The exposure is in the words, not the screens.
19. **Which older design to rebuild as the working prototype.** My read: the Aerial Defense
    takeaways are by far the best brief, because "I would have pushed for deeper research" and
    "I would have used much more whitespace" is a genuine design brief she wrote herself fifteen
    years ago. The Clinic takeaways are about delegation and research process, which do not
    translate into a thing you can build. The obstacle is confidentiality, and the way through it
    is to rebuild the problem class with invented data rather than the system.
20. **Go-live date.** Not set.
21. ~~**Geography.**~~ **RESOLVED 9 Sep: central Israel or remote, no relocation.** See
    `notes/strategy.md` section 6 for what it changes.
22. **Whether to keep** the career break line, the second Asperii entry, and the two pre-2012 IDF
    roles on the CV. My recommendations are in `drafts/cv.md`.

---

## D. Fix on the live Carbonmade site now, independent of everything else.

The site is public and the password is off, so anyone she has sent it to is seeing this today.

23. **Unedited template text** on the Aircraft Maintenance page: "You can you this place to talk
    a little bit about the image on the side." Typo included.
24. **Typo** on the Clinic page: "mange a monthly allocation plan."
25. **The About blurb** reads "Experienced product design person," which looks like a half-finished
    edit.
26. **Salesforce is missing entirely** from the About page timeline, which stops at Asperii
    2020-2021. The same problem the CV has. Her most significant four years appear in none of her
    three public artifacts.

---

## E. Corrections to the handoff brief itself.

Found on 7 Sep while reading the source material. The brief is otherwise accurate.

27. **Drill Management is Webiks work**, done for the IDF, dated Jun 2017 to Sep 2018. The build
    plan offers it as a possible proof artifact for the Air Force case study. It does not
    qualify, because it is not from her Air Force service. Aerial Defense is the only candidate.
28. **The Carbonmade project dates in section 4b are upload dates, not project dates.** Aircraft
    Maintenance is listed as May 2022 but ran Jan to Sep 2018. Clinic Management is listed as
    May 2021 but ran Sep 2020 to Nov 2021.
29. **Paw Pal is already gone** from the live site. The decision to cut it is already executed.
30. **The Webiks slot is much cheaper than assumed.** Two complete written case studies already
    exist for it, Aircraft Maintenance and Drill Management. Combined with the deck's Aerial
    Defense material, two of the four planned case studies are already sourced. Only the two
    Salesforce studies start from zero, which means September is exclusively about Salesforce.
31. **Asperii end date.** The brief lists the CV as saying 2020-2021 and LinkedIn as saying Sep
    2020 to Apr 2022. The live site agrees with the CV. LinkedIn is likely correct; the Nov 2021
    date refers to the clinic project ending, not the job.

---

## F. Asset quality, found 7 September while placing images.

32. **Two of the three Aircraft Maintenance screens are filled with lorem ipsum** and
    "Component Name" placeholders. The Reviews list and the grouped-by-category view both show
    eight cards of `Lorem ipsum dolor sit consectetur adipiscing elit` and no real component
    names. They are on her live Carbonmade site in that state today.

    The third screen, the default plane-tasks view, is genuinely strong: real technician roster,
    six progress dials, an interactive aircraft schematic with numbered assignment markers, and a
    ten-step procedure rail. That one is used in the case study.

    The category-grouping chips on the third screen are a real design idea worth showing, with
    live counts per category. The cards beneath them are not.

    **Fix:** re-export those two frames from the original Webiks Figma with plausible content in
    them. If that file is gone, crop to the parts that are real, or drop them. Do not ship
    lorem ipsum on a portfolio; it reads as an unfinished mockup rather than a shipped product.

33. **The Carbonmade downloads needed refetching.** Requesting a square box from the image CDN
    pads and upscales every asset into that square. Fetching the bare asset id with no size
    suffix returns the true original. Six of the eleven "images" in each project were the same
    background texture repeated, byte for byte. Real count is 18 images, not 37, and the
    committed payload dropped from 20.3MB to 5.7MB.

34. **Screens are timestamped May 2022** in their own UI ("May 22, 2022, 16:34:52"), on a project
    that ran January to September 2018. Harmless, but if anyone reads the case study dates against
    the screenshots it looks inconsistent. Worth a line in the caption or a re-export.

35. **The deck's aerial defense before/after screens are strong, and I did not publish them.**
    Both are redacted to the XXXX standard the brief describes, and as a pair they demonstrate the
    single clearest design argument in her whole body of work: in the before, every impact ellipse
    is drawn identically and they overlap into an unreadable cluster; in the after, live threats
    are solid filled shapes and past threats are dashed outlines, and the single mixed table has
    become two, live and other.

    What is still legible despite the redaction: real map geography with place names, response
    timings in the tables, and the ellipse geometry itself. That is the exact category the
    declined security-officer recommendation covered. A private slide deck and a public URL under
    her real name are different risk profiles.

    **Decision needed.** Three options: get the security officer review that was declined, publish
    a cropped detail showing only the ellipse treatment against a blank ground, or publish nothing
    photographic and rely on the abstract diagram now in the case study. I have taken the third
    option as the default because it is safe and it explains the thinking better than a screenshot
    of a Hebrew interface would to a reviewer at Google.

36. **Three sections on the Aircraft Maintenance page had to be removed, not just emptied.**
    "Who I was designing for", "Results" and "Takeaways" existed only as gap callouts. Once those
    came out, all three were headings with nothing beneath them, which reads worse than an absent
    section. They are deleted from the page and listed here instead.

    All three are real weaknesses in the case study, in rising order of how much an interviewer
    will care:
    - **Personas.** The Clinic study has a user-types-and-characteristics matrix; this one names
      technicians, commanders and air crew and never separates their needs.
    - **Takeaways.** The deck ends both of its case studies with an honest "I learned" and
      "I would have". That self-critique is what big tech interviewers probe for and most
      portfolios omit. This study has none.
    - **Results.** No outcome data at all, and the page now stops at what shipped. Eight years on,
      a qualitative account is the realistic ceiling. If nothing can be recalled, say so on the
      page rather than leaving the section off, because a stated absence survives questioning and
      a silent one invites it.
