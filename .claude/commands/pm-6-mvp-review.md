---
name: pm-6-mvp-review
description: "Generate quick follow-up questions to confirm the working version solves the customer's problem: checks on the assumptions and on the cases it must handle. Use before showing the working version to the customer."
---

# MVP review

**Role:** confirm the solution works for the customer, not sell it.
**Users:** me running the review; the customer and whoever approves the output.
**Target:** a yes or no on "does it solve the problem", what sign-off needs, and the sample needed to test the AI parts.
**Grounding:** the solution concept (problem, workflow, assumptions) from the Notion page in the run notes, fetched fresh; the working version; `customer-personas` (what the approver typically needs); `product-glossary`; `pm-standard`.
**Tone:** open questions, in the customer's own terms, one idea each.

## Step 1: Plan the evaluation
- **Input:** the concept's AI / code / people split.
- **Output:** for each thing the AI does: what "right" looks like, which cases matter most (common requests, tricky wording, ones it should refuse or flag), and roughly how many examples are needed to trust it.
- **Happy path:** the plan shapes question 3.
- **Edge cases:** the AI does nothing judgement-based: say so, and skip the sample request.
- **Acceptance criteria:** the sample asked for matches the plan exactly.
- **Handoff:** Step 2.

## Step 2: Write the questions
- **Input:** the plan and the concept's assumptions.
- **Output:** a Notion page, "[Run]: MVP review ([customer])", under the parent page named in the active context folder, with an empty Notes section at the end. Questions in this order, each specific to the case:
  1. **Does it solve the problem?** Whether the team could have used it for their last real request (one request), e.g. "Could your team have used this for the last [request] you got?"
  2. **Trust and sign-off.** What the approver needs before an answer goes out. Name what the approver's persona typically needs only as a follow-up, after they answer.
  3. **Real examples for testing.** The sample the plan needs, in their terms, naming the tricky cases, e.g. "Could you send us 20 or so recent [requests], with the answers your team sent? Please include a few unusual ones."
  - **Assumptions:** keep each concept assumption whose answer could change the solution, in its wording from the concept, after question 3. Drop the rest and say in chat which and why. Don't add new ones.
  4. **Defaults (optional, last).** Name each default: "By default, it [does A], [leaves out B] and [assumes C]. Would your team use the same defaults?"
- **Happy path:** short enough to follow on first hearing.
- **Edge cases:** value, method and sign-off questions often overlap: keep one per area and merge the rest.
- **Acceptance criteria:** no hint of the expected answer; only questions that could change the solution.
- **Handoff:** give me the link; add it to the run notes.

## Step 3: Check the sample yourself, don't ask
- **Input:** the sample the customer sends.
- **Output:** a short test report.
- **Happy path:** run each case through the working version; note which it can't answer and which hit gaps in the data.
- **Edge cases:** the sample doesn't cover enough cases (different askers, options, segments): ask for more.
- **Acceptance criteria:** every case has a result.
- **Handoff:** feedback goes back into `pm-4` screens and `pm-5` build.
