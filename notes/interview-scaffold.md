# Interview scaffold, Salesforce case studies

Lifted from the two stub pages before they were pulled off the public site.
An unwritten case study that is only a list of unanswered questions is worse
than no page at all, so these do not ship until there are answers.

Rebuild each page from this once the interview has run.


---

## Case study 01 — Service Reply for Email (lead)

**Working lead paragraph, unverified:**

> A support agent gets a customer email containing several separate asks. One click produces a complete reply, grounded in knowledge articles, with its sources attached. A second click opens it up: every intent the system detected, the article backing each one, and the ability to drop an intent or swap its source.


**1. What was broken before this existed?**

Not "replies were slow." What an agent physically did with a multi-part customer email: where they looked, what they copied, how long it took, what they got wrong.

**2. Who was the user, specifically?**

Support agent, admin, end customer, or several with conflicting needs. The admin who configures this is probably a separate design problem worth naming.

**3. What did you own, and what did PM and engineering own?**

**4. What was the hardest design decision, and what did you choose against?**

The obvious candidate: how much reasoning to surface by default. Every alternative that was rejected here is interview currency.

**5. What did you get wrong first, and what changed it?**

Research, testing, or pushback. A reversed decision is worth more than a clean one.

**6. How did the design handle the model being wrong?**

Confidence, correction, fallback, undo. This is the centre of the case study. The agent signs their name to the reply, so the design has to make them accountable for something they did not write.

**7. What shipped, and what got cut?**

**8. What happened after launch?**

Numbers if they exist. Acceptance rate and edit rate especially, because edit rate is a design metric and not just a model one.


---

## Case study 02 — Real-Time Classification

**Working lead paragraph, unverified:**

> AI that classifies a support case and predicts its fields, so an agent does not spend the first minutes of every case doing data entry. The design problem sits in the gap between a prediction and a person who is accountable for it.


**1. What was broken before this existed?**

**2. Who was the user, specifically?**

**3. What did you own, and what did PM and engineering own?**

**4. What was the hardest design decision, and what did you choose against?**

**5. What did you get wrong first, and what changed it?**

**6. How did the design handle the model being wrong?**

Sharper here than anywhere else. A wrong classification is silent. It does not look like an error, it looks like a filled-in field, and it propagates into routing and reporting.

**7. What shipped, and what got cut?**

**8. What happened after launch?**
