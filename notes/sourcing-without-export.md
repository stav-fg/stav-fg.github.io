# Sourcing the case studies without exporting anything

Written 8 September, after the Claude on Stav's work machine declined the bulk collection request.

## The refusal was correct and we should not route around it

What I wrote asked a corporate assistant to gather employer documents and move them to a personal
Drive for personal use. That is the shape of data exfiltration regardless of intent, and an
assistant inside Salesforce declining it is the assistant working properly.

`notes/work-machine-prompt.md` is superseded. Do not run it.

The useful part is what the refusal exposed: I had reached for the least legitimate source first,
when the two strongest sources need no permission from anyone.

## Three sources that require no export

### 1. Her own memory. This was always the primary source.

Every question that actually makes a case study good is one only she can answer, and none of them
require a document:

- What was broken before this existed
- What was the hardest decision and what she chose against
- What she got wrong first and what changed it
- How the design handled the model being wrong
- What shipped and what got cut

A PRD cannot answer any of those. It records what was agreed, not what was considered. The
documents were only ever going to be a memory aid, and we are not blocked without them.

### 2. Public Salesforce documentation. Extensive, and it carries the whole product layer.

These features ship. Salesforce documents them publicly, in depth, across Help, Trailhead, its own
blog and third-party writeups. Verified 8 September.

Einstein Service Replies has public Help pages, a Trailhead project on setup, and a Salesforce blog
post. Einstein Case Classification has a Help page specifically on configuring the model, and two
Trailhead modules.

The Case Classification documentation even describes the threshold design publicly, in language
close to what appears on her own board: the more automated the action, the higher the prediction
confidence required, with separate behaviour for suggesting the top values versus selecting and
saving automatically.

**So the safe division is:**
- **Public documentation** carries what the product does, the correct terminology, and the shipped
  configuration surfaces. Citable, accurate, no permission needed.
- **Her account** carries why it is designed that way, what was hard, and what was rejected.

That division is also better portfolio writing than a PRD summary would have been. A case study
that explains a publicly documented product and then tells you the reasoning behind it reads as
confident. One that leans on internal documents reads as an internal document.

### 3. The Figma files she already exported, months ago, to her own Drive.

Everything in `Projects` was exported in August 2026, before this project existed, and it sits in
her personal Drive. That material is already out of the building and it is her own design work.

`tools/figextract.py` reads it. Two files are already done. The rest need downloading onto this
Mac, because the large ones are too big for the Drive connector.

## What to do manually, in order

1. **Download the `.fig` files from her personal Drive onto this Mac.** Priority: `RTC.fig`,
   `A3 Registry Setup.fig`, `KGER.fig`. I extract the text and thumbnails from each.
2. **Run the interview.** `notes/interview-plan.md`, twenty-one questions in tiers, one at a time.
   This is the bottleneck and always was.
3. **I mine the public documentation** per feature and write the product layer from it.
4. **PDF exports, but only where layout is the point** and only for files she is comfortable
   exporting. Far smaller ask than the original one.

## If specific internal documents are genuinely wanted

Ask, through the proper channel. Many companies permit portfolio use of your own work with manager
or Employee Success approval, and some have an explicit process for it. That is a five-minute
conversation and it either produces a clear yes, a scoped yes, or a no worth knowing before her
last day.

What we should not do is look for a phrasing that gets the corporate assistant to comply. If the
answer is no, the case studies get written from her account and the public record, which as above
is a perfectly good way to write them.
