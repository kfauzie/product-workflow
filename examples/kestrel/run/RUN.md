# Run: Gusta, AI support agent rollout

> **FICTIONAL EXAMPLE.** Kestrel, Gusta, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

**The question:** which ticket types can the AI support agent resolve on its own?
**Scope:** support tickets only, in in-app chat.
**Data:** `data/ticket_types.json`: 15 ticket types, monthly volume, results on 50 test tickets each, cost of a wrong call, and 3 example tickets per type (message, Kestrel's proposal, the playbook rule and the grading AI's verdict). Made by `notebooks/make_data.py`.

| Step | Skill | Output |
|---|---|---|
| 1. Data review | `pm-1-data-discovery` (Initial review) | [01-data-review.md](01-data-review.md) |
| 2. Discovery guide | `pm-2-discovery-interview` | [02-discovery-guide.md](02-discovery-guide.md) |
| 3. Discovery notes | the PM, in the call | [03-discovery-notes.md](03-discovery-notes.md) |
| 4. Research synthesis | `pm-1-data-discovery` (Answer) | [04-synthesis.md](04-synthesis.md) |
| 5. Spec: solution concept | `pm-3-problem-to-solution-concept` | [05-solution-concept.md](05-solution-concept.md) |
| 6. Design | `pm-4-solution-design` | [06-screen-specs.md](06-screen-specs.md), [design/](design/) |
| 7. Prototype | `pm-5-mvp-build` | [build/mvp.html](build/mvp.html), tests in [build/](build/) |
| 8. MVP review | `pm-6-mvp-review` | [07-mvp-review.md](07-mvp-review.md) |

## Decisions I made (and what I turned down)

| Decision | Why | What I turned down |
|---|---|---|
| Decide per ticket type, not one setting for all | Accuracy runs from 86% to 100% across types; one setting is wrong for most of them | A single confidence threshold |
| Three outcomes, not two | "AI-assisted human" keeps a support agent on the 4 types that are good but not safe to send unchecked | Only "on" or "off" |
| Any High-risk type needs 98%+ even for AI-assisted human | A wrong refund or a missed payroll costs the customer real money | Treating money like any other answer |
| Count wrong answers that reach customers, not just accuracy | Leadership asks "what could go wrong"; 9 a month, all on low or medium-cost tickets, is an answer they can sign | Showing accuracy alone |
| Recommend, but let her decide: a setting per row, with a warning above the recommendation | She owns the call; the dashboard shows what an override costs in wrong answers | Locking the recommendation |
| One page: rules, a table, three numbers, examples | The decision is the table; each example shows the playbook rule and the grading AI's verdict, so anyone can check Kestrel | A dashboard with filters and charts |
