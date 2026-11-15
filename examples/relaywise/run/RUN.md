# Run: Pellmore, Support Operations

> **FICTIONAL EXAMPLE.** Relaywise, Relay Agent, Relay Studio and Pellmore are invented. The use case and all data are synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

**Customer:** Pellmore, a B2B software company with 24 support agents. We talk to its Head of Support Operations.
**The ask, word for word:** "Can we switch auto-resolve on for more ticket types?"
**Data:** `data/tickets_monthly.csv` (12 months × 10 categories), `data/eval_results.csv` (2,390 past tickets checked in shadow mode), `data/inputs.json` (what the prototype reads). All made by `notebooks/make_data.py`; numbers in these pages from `notebooks/example_numbers.py` and the prototype's tests.

| Step | Skill | Output |
|---|---|---|
| 1. Data review | `pm-1-data-discovery` (Initial review) | [01-data-review.md](01-data-review.md) |
| 2. Discovery guide | `pm-2-discovery-interview` | [02-discovery-guide.md](02-discovery-guide.md) |
| 3. Discovery notes | the PM, in the call | [03-discovery-notes.md](03-discovery-notes.md) |
| 4. Research synthesis | `pm-1-data-discovery` (Answer) | [04-synthesis.md](04-synthesis.md) |
| 5. Spec: solution concept | `pm-3-problem-to-solution-concept` | [05-solution-concept.md](05-solution-concept.md) |
| 6. Design: screen specs and screens | `pm-4-solution-design` | [06-screen-specs.md](06-screen-specs.md), [design/](design/) |
| 7. Prototype | `pm-5-mvp-build` | [build/mvp.html](build/mvp.html), tests in [build/](build/) |
| 8. MVP review | `pm-6-mvp-review` | [07-mvp-review.md](07-mvp-review.md) |

## Decisions I made (and what I turned down)
The skills do the legwork; these were the judgement calls.

| Decision | Why | What I turned down |
|---|---|---|
| Reframe the ask from "more auto-resolve" to "which categories are safe, and what's the saving net of mistakes" | Auto-resolving everything loses £151k a year once wrong answers are costed; the ask as stated would have hurt her | Building a bulk "switch on" for more categories |
| Decide per category, not one setting for the whole team | Accuracy ranges from 81.6% to 98.7% across categories; one setting is wrong for most of them | A single global confidence threshold |
| Judge accuracy by its lower bound, not the average | Two categories have fewer than 100 checked tickets; their averages look fine but can't be trusted yet | Ranking categories by raw accuracy |
| Price wrong answers, especially serious ones | Leadership's question is "what do we bank, and what could go wrong"; a saving without the risk won't get approved | Showing hours saved alone |
| A middle mode: the AI drafts, an agent approves | Captures 35% of the time on risky categories with almost no wrong answers reaching customers | Only "auto" or "off" |
| Ship with a guardrail and a rollout plan, not a report | Approval depends on being able to switch it off; the plan is what VP and Finance sign | A longer analysis deck |
