# Product workflow

[![checks](https://github.com/kfauzie/product-workflow/actions/workflows/checks.yml/badge.svg)](https://github.com/kfauzie/product-workflow/actions/workflows/checks.yml)

How I go from a customer's ask to a tested, working prototype with Claude Code: discovery notes, research synthesis, spec, design, prototype, then hand-off to engineering. Each step is a skill in [`.claude/commands/`](.claude/commands/), grounded in company, customer and design context pulled through MCP.

**[Open the live prototype ›](https://kfauzie.github.io/product-workflow/)** · [the worked example, step by step](examples/corvane/run/RUN.md) · [decisions I made](examples/corvane/run/RUN.md#decisions-i-made-and-what-i-turned-down)

![The deal climate brief, built end to end with this workflow](examples/corvane/run/design/2-brief.png)

> **The example in [`examples/corvane/`](examples/corvane/) is FICTIONAL.** Corvane, Riskline, Retrofit Planner, Ashgrove Partners, Project Lantern and Lantern Group are invented, and all data is synthetic. It shows the workflow end to end on a realistic B2B case: a physical climate-risk platform and a private equity customer.

## My AI stack

```mermaid
flowchart LR
  subgraph Context["Context via MCP"]
    N[Notion<br/>company, research, docs]
    SL[Slack<br/>customer channels]
    F[Figma<br/>design system]
  end
  subgraph CC["Claude Code + custom skills"]
    S1[Data review] --> S2[Discovery guide] --> S3[Synthesis] --> S4[Spec] --> S5[Design] --> S6[Prototype] --> S7[MVP review]
  end
  Context --> CC
  ME((Me: the judgement calls)) -.-> S2 & S4 & S5 & S7
  S2 & S4 & S7 --> NP[Notion pages]
  S6 --> GH[GitHub: code, tests, CI]
```

- **AI** for what needs judgement on messy input: reading notes, drafting, suggesting.
- **Code** for everything fixed: every number on a screen is calculated and tested, never written by the model.
- **Me** for the decisions: what the problem is, what to cut, what ships.

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

## How I use this at work
- **Day to day:** Claude Code with custom skills and MCPs for GitHub, Slack, Notion and Figma, for customer research, data analysis, specs, design, prototyping and PRs.
- **ExaCare AI:** I built an eval agent (SQL, TypeScript, Claude API, Notion and Linear MCPs, GitHub Actions) that diagnosed failures daily and drove five prioritised fixes a week for the squad.
- **Savvy:** I designed an agent development platform that turned each customer's workflow and data into a first-pass agent, cutting time to the first working agent from a month to a week.

## Try the example
The quickest way is the [live prototype](https://kfauzie.github.io/product-workflow/). To run it locally:
```bash
pip install -q -r requirements.txt && npm install && npx playwright install chromium
```
```bash
tools/open_run.sh
```
```bash
npm test
```
`npm test` runs the known-answer tests and a headless click-through; the same checks run on every push. Regenerate the synthetic data with `python3 notebooks/make_data.py` from `examples/corvane/run`.

## About
Built by Kevin Fauzie, an AI product manager in London: a decade as a PM, a co-founded AI agent startup, a Stanford MBA. [LinkedIn](https://www.linkedin.com/in/kevinardian/)
