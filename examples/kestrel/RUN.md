# Run: Gusta, AI support agent rollout

> **FICTIONAL EXAMPLE.** Kestrel, Gusta, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

**The question:** which ticket types can the AI support agent resolve on its own?
**Scope:** support tickets only, in in-app chat.
**Data:** `data/ticket_types.json`: 16 ticket types (including Other, for tickets that match no type), monthly volume, accuracy (every ticket in the last 30 days where Kestrel is used, a daily 50-ticket test where it isn't), cost of a wrong call, and 3 example tickets per type (message, Kestrel's proposal, the customer support rule and the grading AI's verdict). Made by `notebooks/make_data.py`.

| Step | Skill | Output |
|---|---|---|
| 1. Data review | `1-pm-data-discovery` (Initial review) | [01-data-review.md](01-data-review.md) |
| 2. Discovery guide | `2-pm-discovery-interview` | [02-discovery-guide.md](02-discovery-guide.md) |
| 3. Discovery notes | the PM, in the call | [03-discovery-notes.md](03-discovery-notes.md) |
| 4. Research synthesis | `1-pm-data-discovery` (Answer) | [04-synthesis.md](04-synthesis.md) |
| 5. Spec: solution concept | `3-pm-problem-to-solution-concept` | [05-solution-concept.md](05-solution-concept.md) |
| 6. Design | `4-pm-solution-design` | [06-screen-specs.md](06-screen-specs.md), [design/](design/) |
| 7. Prototype | `5-pm-mvp-build` | [build/mvp.html](build/mvp.html), tests in [build/](build/) |
| 8. MVP review | `6-pm-mvp-review` | [07-mvp-review.md](07-mvp-review.md) |

## Decisions I made (and what I turned down)

| Decision | Why | What I turned down |
|---|---|---|
| Decide per ticket type, not one setting for all | Accuracy runs from 86% to 100% across types; one setting is wrong for most of them | A single confidence threshold |
| Three outcomes, not two | "AI-assisted human" keeps a support agent on the 9 types that are good but not safe to send unchecked | Only "on" or "off" |
| AI-assisted human from 60% at any risk; Human only below that | A support agent checks every draft, so risk decides only what can go out unchecked; below 60% a draft costs more time to fix than it saves, and can mislead the support agent | Sending High-risk types to a human by default, which wastes the drafts that are right 9 times in 10 |
| Count wrong answers that reach customers, not just accuracy | Leadership asks "what could go wrong"; 9 a month, all on low or medium-cost tickets, is an answer they can sign | Showing accuracy alone |
| Recommend, but let her decide: a setting per row, with a warning above the recommendation | She owns the call; the dashboard shows what an override costs in wrong answers | Locking the recommendation |
| One page: rules, a table, three numbers, examples | The decision is the table; each example shows the customer support rule and the grading AI's verdict, so anyone can check Kestrel | A dashboard with filters and charts |
