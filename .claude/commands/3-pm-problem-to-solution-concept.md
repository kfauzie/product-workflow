---
name: 3-pm-problem-to-solution-concept
description: "Turn the discovery notes and data findings into a solution concept: the problem, two or three solution ideas, and the recommended solution with its end-to-end workflow. Use after the discovery interview, before solution design."
---

# Problem to solution concept

**Role:** start from the problem and recommend the simplest thing that solves it.
**Users:** me; then whoever approves the direction (shared on screen, so short).
**Target:** a recommendation that weighs user value, commercial benefit and effort, and a workflow that design can turn into screens.
**Grounding:** the interview notes (quote the transcript, not the AI summary); tested claims from `1-pm` Step 2 (don't re-analyse the data); `company-context` (product strategy, how it makes money); `customer-personas` (user and buyer; the notes win where they differ); `product-glossary`; `0-pm-standard`.
**Tone:** answer first; no claim without a quote or a calculated number.

## Step 0: Check for gaps
- **Input:** the notes.
- **Output:** either "no gaps that change the idea", or questions for the customer.
- **Happy path:** no gap big enough to change which idea wins or the main workflow; carry on.
- **Edge cases:** a gap that would change the idea or the workflow (who the user is, what the job is): show me the questions and wait. Detail choices (defaults, settings, method options) don't stop the work: assume, state it, move on.
- **Acceptance criteria:** only questions that could change the idea or the workflow are asked. Before Step 1, write the problem in one sentence in your own words: who the customer is (the person you solve for, not their audience), and the one thing that stops them. Every later section must serve that sentence.
- **Handoff:** Step 1.

## Step 1: Write the concept
- **Input:** notes, tested claims, context.
- **Output:** a Notion page, "[Run]: solution concept ([customer])", under the parent page named in the active context folder:
  1. **The problem:** what they asked for, in their words. The real problem: [user] needs to [job] but today [workaround], which causes [impact]. Evidence: 3–5 bullets, each a quote or a calculated number, with its source.
  2. **Impact:** one bullet per person or team affected (time, waiting, rework, risk to decisions). Mark estimates.
  3. **Solution ideas:** two or three genuinely different ideas. For each: what it is in one line; **User** (does it solve the problem, how much of the pain does it remove, does it lead to a better commercial decision, how it fits their day, which "yes" triggers it hits); **Commercial benefit** led by its type (new revenue, upsell or retention), then why and the fit with product strategy; **Effort** across engineering, any new models, data to collect, and rollout. Mark judgements.
  4. **The recommendation:** which idea and why, naming what tipped it. Compared with the original ask: what it covers, what it doesn't, what's for later.
  5. **Workflow, end to end:** bullets "[who] does [what] with [what]", from the request arriving to the answer being sent, including steps outside the product. Use a real request from the notes, with real numbers. Show it handles the range of requests, not just the example. Every input has a reason.
  6. **What AI, code and people do:** AI for flexibility (messy input, free text, interpretation), code for fixed logic (every number, rules, checks), people for judgement and approval. What AI and code do is visible and editable; a person checks before anything goes out. When a person reviews every AI output, set the bar by whether the output saves them time, not by whether it is safe to send: risk decides only what may go out unchecked. Keep fully manual handling for the few cases where AI can't help at all (nothing to ground its answer on, or input it can't classify) or where its output would mislead the reviewer more than help, so the default is AI helping a person, not AI or nothing. Rate the impact of a wrong answer by what realistic mistakes in that category cost; give the same class of harm the same rating, and re-rate when new context changes what a mistake can cost.
  7. **Success criteria:** a target, what mustn't get worse, the time or cost it saves, what approvers need to see, and test cases with known answers.
  8. **Assumptions:** each belief that would make it fail if wrong, written as a question for the MVP review.
- **Happy path:** one page, readable in two minutes.
- **Edge cases:**
  - Money decisions today (cost, payback): use the nearest year in the data, and show how it changes later. A far-off year alone suggests the problem can wait.
  - Notes are paraphrase (recording failed): say so at the top of the evidence.
  - The customer's usual workaround ("we'd just do X instead"): cost it honestly. Workarounds often carry a cost nobody counts.
  - The real fix may be a process change, not a product: say so in the ideas, even if a product is still recommended.
  - Judge an AI's output by the harm that reaches the end customer, not by accuracy alone: a small error rate on a high-stakes task can outweigh a big saving.
- **Acceptance criteria:** every claim has a quote or a number; say how, never "seamless" or "met by design"; test cases have computed answers.
- **Handoff:** give me the link; add it to the run notes; `4-pm-solution-design` reads it fresh.
