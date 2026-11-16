---
name: pm-3-problem-to-solution-concept
description: "Turn the discovery notes and data findings into a solution concept: the problem, two or three solution ideas, and the recommended solution with its end-to-end workflow. Use after the discovery interview, before solution design."
---

# Problem to solution concept

**Role:** start from the problem and recommend the simplest thing that solves it.
**Users:** me; then whoever approves the direction (shared on screen, so short).
**Target:** a recommendation that weighs user value, commercial benefit and effort, and a workflow that design can turn into screens.
**Grounding:** the interview notes (quote the transcript, not the AI summary); tested claims from `pm-1` Step 2 (don't re-analyse the data); `pm-company-context-overview` (product strategy, how it makes money); `pm-company-context-personas` (user and buyer; the notes win where they differ); `pm-company-context-glossary`; `pm-0-standard`.
**Tone:** answer first; no claim without a quote or a calculated number.

## Step 1: Check for gaps
- **Input:** the notes.
- **Output:** either "no gaps that change the idea", or questions for the customer.
- **Happy path:** no gap big enough to change which idea wins or the main workflow. Write the problem in one sentence in your own words: who the customer is (the person you solve for, not their audience), and the one thing that stops them. Every later section must serve that sentence.
- **Edge cases:** a gap that would change the idea or the workflow (who the user is, what the job is): show me the questions and wait. Detail choices (defaults, settings, method options) don't stop the work: assume, state it, move on.
- **Acceptance criteria:** only questions that could change the idea or the workflow are asked; the one-sentence problem is written before Step 2.
- **Handoff:** Step 2.

## Step 2: Write the concept
- **Input:** notes, tested claims, context.
- **Output:** a Notion page, "[Run]: solution concept ([customer])", under the parent page named in the active context folder:
  1. **The problem:** what they asked for, in their words. The real problem: [user] needs to [job] but today [workaround], which causes [impact]. Evidence: 3–5 bullets, each a quote or a calculated number, with its source.
  2. **Impact:** one bullet per person or team affected (time, waiting, rework, risk to decisions). Mark estimates.
  3. **Solution ideas:** two or three genuinely different ideas. For each: what it is in one line; **User** (does it solve the problem, how much of the pain it removes, how it fits their day, which "yes" triggers it hits); **Commercial benefit** led by its type (new revenue, upsell or retention), then why, the fit with product strategy, any better decisions it enables, and how it could be priced (value created against value captured); **Effort** across engineering, any new models, data to collect, and rollout. Mark judgements. If the ask is one customer's custom request, include an idea that makes it a general capability others can configure. Ideas may draw on the external opportunities from `pm-company-context-overview` (Step 2: Enrich); mark them as external and check them against the company's direction.
  4. **The recommendation:** which idea and why, naming what tipped it. Compared with the original ask: what it covers, what it doesn't, what's for later.
  5. **Workflow, end to end:** bullets "[who] does [what] with [what]", from the request arriving to the answer being sent, including steps outside the product. Use a real request from the notes, with real numbers. Show it handles the range of requests, not just the example. Every input has a reason.
  6. **What AI, code and people do** (principle 5 in `pm-0-standard`, "Fit the solution and its bar to the problem", applied step by step):
     - **The split:** which steps are AI, code and people; people make the final calls and approve, and can edit what AI and code did.
     - **The cost of a mistake:** rate each kind of wrong answer by what realistic mistakes in that category cost the end customer, not by accuracy alone; give the same class of harm the same rating, and re-rate when new context changes what a mistake can cost.
     - **How much the AI does alone:** when a person reviews every AI output, set the bar by whether the output saves them time; the cost of a mistake decides only what may go out unchecked. Keep fully manual handling for the few cases where AI can't help (nothing to ground its answer on, input it can't classify) or would mislead the reviewer more than help, so the default is AI helping a person, not AI or nothing.
  7. **Success criteria:** start from the company metric this work serves and pick the leading indicators the product can move. Set two layers before launch: is the AI doing its job (e.g. accuracy on known answers), and is the user better off (time saved, errors avoided). Add what mustn't get worse, what approvers need to see, and test cases with known answers.
  8. **Assumptions:** each belief that would make it fail if wrong, written as a question for the MVP review.
- **Happy path:** one page, readable in two minutes.
- **Edge cases:**
  - Data that spans time (forecasts, scenarios): base today's money decisions (cost, payback) on the nearest period, and show how it changes later. A far-off period alone suggests the problem can wait.
  - Notes are paraphrase (recording failed): say so at the top of the evidence.
  - The customer's usual workaround ("we'd just do X instead"): cost it honestly. Workarounds often carry a cost nobody counts.
  - The real fix may be a process change, not a product: say so in the ideas, even if a product is still recommended.
- **Acceptance criteria:** every claim has a quote or a number; say how, never "seamless" or "met by design"; test cases have computed answers.
- **Handoff:** Step 3.

## Step 3: Review it before I see it
- **Input:** the draft page.
- **Output:** a revised page, and a line in chat on what the review changed.
- **Happy path:** read it once as the person who approves the direction, with no context, then check:
  - **The thread:** the recommendation solves the one-sentence problem from Step 1, and every section serves it; cut anything that doesn't.
  - **The evidence:** every claim has a quote or a computed number; estimates and judgements are marked.
  - **The choice:** the ideas are genuinely different, and the reason the recommended one wins is stated, not implied.
  - **The workflow:** it covers the range of real requests, not just the example, and every input has a reason.
  - **The page:** it reads in two minutes and follows the communication guide and Notion layout in `pm-0-standard`.
- **Edge cases:** the review finds a gap that changes the recommendation: fix it, and say so at the top of the page rather than burying it.
- **Acceptance criteria:** every check passes, or the page says which doesn't and why.
- **Handoff:** give me the link; add it to the run notes; `pm-4-solution-design` reads it fresh. When I comment, revise as section 3 of `pm-0-standard` describes.
