# Run: Ashgrove Partners, Project Lantern

> **FICTIONAL EXAMPLE.** Corvane, Riskline, Retrofit Planner, Ashgrove Partners, Project Lantern and Lantern Group are invented. All data is synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

**Customer:** Ashgrove Partners, a mid-market private equity firm. We talk to their Head of Sustainability.
**The ask, word for word:** "Can the climate output be more useful to the deal side?"
**The deal:** Lantern Group, 14 sites in 4 countries. EV £360m, 6-year hold (2026–2031), IC in 4 weeks.
**Data:** `data/sites.csv` and `data/sites.json` (synthetic Riskline export, made by `notebooks/make_data.py`). Numbers in these pages: `notebooks/example_numbers.py`.

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
| Treat the Head of Sustainability as the customer, the deal team as his audience | His problem is that his work never moves a deal; solving that is what makes the deal team ask for it | Designing for the deal team directly: a second user to onboard, and he loses control of the message |
| Drop "grades vs £" and "timing" as the main problem | The interview showed the deal team already gets £ and isn't blocked by timing; they reject the no-defences assumption | Keeping my pre-call hypotheses because the data review pointed to them |
| Make the defended case the headline, undefended one toggle away | It answers the actual objection with evidence (which defences, who provides them, what standard) instead of asking the deal team to accept an assumption | Showing only the undefended figure, the product's default |
| Count insurance premiums as a cost | "Just insure it" is the common answer; premiums over the hold (£31.6–42.1m) exceed the expected damage (£18.6m) | Treating insurance as a way out of the risk |
| Cut the brief to one page | One answer, why, the defences and the deal terms is what gets acted on; the rest is one click away | A dashboard with every breakdown, control and assumption visible |
| Output deal terms and a spreadsheet, not just a report | Success is the deal team putting the number into its model and terms | A longer narrative report |
