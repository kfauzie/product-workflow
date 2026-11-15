# Product workflow: rules for Claude

A discovery-to-prototype workflow for B2B products, run as Claude Code skills in `.claude/commands/`.

## Active context and run
- **Context folder:** `examples/kestrel/context/` (FICTIONAL example). Point this at your own company's folder, or leave it empty and let the skills pull context through MCP.
- **Run folder:** `examples/kestrel/run/`. Change both lines when you start real work.

## Rules
- Company, product, customer and design facts come from the context skills (`company-context`, `product-glossary`, `customer-personas`, `design-system`), which read the context folder, then Notion, Slack and Figma via MCP, then ask me. Never from the model's memory
- Follow `pm-standard` for everything a reader sees
- Work only in the active run folder; read its `RUN.md` first. Nothing carries over between runs: numbers, findings, defaults or customer context
- Every number is calculated by code and can be traced; synthetic data is labelled as synthetic on screen
- Skills hold general method only. Case details go in the run's `RUN.md`
- Don't change a skill unless I ask. When feedback does change one, write the general principle behind it, never the case
- Documents I read or annotate (questions, notes, concept, review) live in Notion under the parent page in the context folder. Create the page and give me the link; don't summarise it in chat
- Unsure which run something belongs to: ask

## Workflow
| Step | Who | Skill | Output |
|---|---|---|---|
| 1. Data and context arrive | Claude | `pm-1-data-discovery` (Initial review; start with `python3 tools/lens.py profile <csv>` for wide exports) | Run folder, `RUN.md` with findings, questions and the ask word for word |
| 2. Discovery guide | Claude | `pm-2-discovery-interview` | Notion page |
| 3. Interview | me | | Notes in that page |
| 4. Research synthesis | Claude | `pm-1-data-discovery` (Answer: one claim at a time) | Tested claims in `RUN.md` |
| 5. Spec: solution concept | Claude | `pm-3-problem-to-solution-concept` | Notion page |
| 6. Design | Claude | `pm-4-solution-design` | Screen specs and images in `design/`, most important first |
| 7. Prototype | Claude | `pm-5-mvp-build` | One HTML file, tests and a headless check in `build/` |
| 8. MVP review | me + Claude | `pm-6-mvp-review` | Notion page; feedback back into design and build |

Show results in chat first and commit once per step, except Notion pages: give the link only.

## Setup
`pip install -q -r requirements.txt` · checks: `node build/test_mvp.js` and `node build/check_mvp.js` in a run folder (Playwright for the headless check)
