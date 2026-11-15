# Product workflow

How I go from a customer's ask to a tested, working prototype with Claude Code: discovery notes, research synthesis, spec, design, prototype, then hand-off to engineering. Each step is a skill in [`.claude/commands/`](.claude/commands/), grounded in company, customer and design context pulled through MCP.

> **The example in [`examples/corvane/`](examples/corvane/) is FICTIONAL.** Corvane, Riskline, Retrofit Planner, Ashgrove Partners, Project Lantern and Lantern Group are invented, and all data is synthetic. It shows the workflow end to end on a realistic B2B case: a physical climate-risk platform and a private equity customer.

## The workflow, end to end

| Step | Skill | Grounded in | Output | In the example |
|---|---|---|---|---|
| 1. Data review | [`pm-1-data-discovery`](.claude/commands/pm-1-data-discovery.md) (Initial review) | The customer's data; glossary for columns and units | 2–5 findings, each an interview question, every number from code | [01-data-review](examples/corvane/run/01-data-review.md) |
| 2. Discovery notes | [`pm-2-discovery-interview`](.claude/commands/pm-2-discovery-interview.md) | Findings from step 1; personas as things to listen for | A 10-minute guide in Notion; notes from the call | [02-guide](examples/corvane/run/02-discovery-guide.md), [03-notes](examples/corvane/run/03-discovery-notes.md) |
| 3. Research synthesis | `pm-1-data-discovery` (Answer) | The notes; the data | Each claim tested: supported, not supported or unclear | [04-synthesis](examples/corvane/run/04-synthesis.md) |
| 4. Spec | [`pm-3-problem-to-solution-concept`](.claude/commands/pm-3-problem-to-solution-concept.md) | Notes, tested claims, company context, personas | Problem, 2–3 ideas weighed on user, commercial and effort; the recommendation; workflow; AI / code / people split; success criteria; assumptions | [05-solution-concept](examples/corvane/run/05-solution-concept.md) |
| 5. Design | [`pm-4-solution-design`](.claude/commands/pm-4-solution-design.md) | The spec; design system from Figma; glossary | Per screen: input, output, happy path, edge cases, acceptance criteria, handoff; then the screens | [06-screen-specs](examples/corvane/run/06-screen-specs.md), [design/](examples/corvane/run/design/) |
| 6. Prototype | [`pm-5-mvp-build`](.claude/commands/pm-5-mvp-build.md) | Agreed screens; spec's test cases | One HTML file, numbers by code, tests and a headless check | [build/](examples/corvane/run/build/) |
| 7. MVP review | [`pm-6-mvp-review`](.claude/commands/pm-6-mvp-review.md) | The spec's assumptions; the prototype | Questions that could change the solution; the sample needed to test the AI parts | [07-mvp-review](examples/corvane/run/07-mvp-review.md) |
| 8. Hand-off | `pm-5-mvp-build` ("later, if asked") | The prototype and its tests | One PR per screen behind a feature flag, engineer review, staging, release | — |

Every skill also reads [`pm-standard`](.claude/commands/pm-standard.md): what good looks like, the communication guide and the document style.

## How MCPs ground it
Four context skills replace anything company-specific. Each reads the active context folder first, then MCP, then asks me, and never fills a gap from the model's memory:

| Context skill | Pulls from |
|---|---|
| [`company-context`](.claude/commands/company-context.md) | Notion (company, product, pricing pages), Slack (announcements, customer channels) |
| [`product-glossary`](.claude/commands/product-glossary.md) | Notion product docs, labels in Figma |
| [`customer-personas`](.claude/commands/customer-personas.md) | Notion research, Slack customer channels |
| [`design-system`](.claude/commands/design-system.md) | Figma variables, styles and components |

Documents I read or annotate (guide, notes, spec, review) are written to Notion; data, code, screens and the run log stay in the repo.

## How each skill is written
Every skill has the same frame:
- **Header:** Role · Users · Target · Grounding · Tone.
- **Each step:** Input · Output · Happy path · Edge cases · Acceptance criteria · Handoff.

The aim is that the next person, or the next skill, knows exactly what they receive and when it's good enough.

## Principles behind it
- I start with the persona and the job they need to get done, and go simplest first.
- I choose based on user insight, commercial benefit to the company, and implementation effort.
- If it follows fixed logic, it's code. If it needs judgment, it's AI. Every number on a screen is calculated, never written by the model.
- I go after the why behind the why.

## Try the example
```bash
pip install -q -r requirements.txt
```
```bash
tools/open_run.sh
```
Tests, from `examples/corvane/run`: `node build/test_mvp.js` (known answers) and `node build/check_mvp.js` (headless click-through; needs Playwright). Regenerate the synthetic data with `python3 notebooks/make_data.py`.

## About
Built by Kevin Fauzie, an AI product manager in London: a decade as a PM, a co-founded AI agent startup, a Stanford MBA. [LinkedIn](https://www.linkedin.com/in/kevinardian/)
