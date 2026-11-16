---
name: company-context-overview
description: "Load the company and product context every other skill grounds on: what the company does, its products and what each outputs, who buys, market and regulation, competitors, how it makes money. Pulled from the active context folder, then Notion and Slack via MCP, then asked. Use at the start of any discovery, concept, design or build step. An Enrich step adds external research on comparable products, kept separate from company facts; internal direction wins."
---

# Company context

**Role:** the shared memory of the company I'm working in, so no skill relies on the model's general knowledge.
**Users:** every other skill in this repo; me, when I check what the skills assumed.
**Target:** every fact has a source (a file, a Notion page, a Slack message, or "given by me"). Nothing is filled from memory.
**Grounding:** in this order, stop at the first that answers:
1. The active context folder named in `CLAUDE.md` (`company.md`)
2. Notion via MCP: company overview, product, pricing and strategy pages
3. Slack via MCP: product announcements and customer channels
4. Ask me

**Tone:** factual and short, one line per fact, with its source.

## Step 1: Load
- **Input:** the active context folder; Notion and Slack MCPs if they're connected.
- **Output:** a short context brief with these fields, each with its source:
  - one-line description and mission
  - products: for each, what it does, what it outputs, who uses it
  - who buys, and what they value (time saved, cost avoided, better decisions)
  - market forces and regulation the customers face
  - competitors and how the company differs
  - how it makes money (pricing, upsell, renewal)
- **Happy path:** `company.md` exists and covers every field. Use it as is.
- **Edge cases:**
  - A field is missing: search Notion, then Slack. If it's still missing, list it under "Not known" and ask me. Never fill it in from memory.
  - Sources disagree: use the newest dated one and flag the conflict.
  - An MCP isn't connected: say which, and carry on with the folder and my answers.
- **Acceptance criteria:** every field has a value and a source, or sits under "Not known". No product capability is claimed without a source.
- **Handoff:** the brief goes to the calling skill, or to Step 2. Background only: don't build features from it unless I ask.

## Step 2: Enrich
- **Input:** the brief from Step 1.
- **Output:** a section "External, not company direction": three to five comparable or adjacent products; for each, what they offer, how they charge and who they serve, with a public source (their website, help centre, pricing page, public reviews). Then two or three opportunities the company may not have considered, each with the external evidence behind it.
- **Happy path:** search for products that do the same job, or an adjacent one, for a similar buyer; read their public pages; paraphrase, never copy.
- **Sandboxed:** keep the findings in a separate section, "External, not company direction". Never mix them into the company facts above, and never present them as what the company does or plans.
- **Internal wins:** where an external finding contradicts anything internal (the context folder, Notion, Slack, or what I've said), follow the internal side. There may be a reason the company doesn't go that way, so turn the contradiction into a question for me ("Comparable products do [X]; is there a reason we don't?").
- **Edge cases:** a source can't be read directly (blocked, paywalled): say so, and mark what came only from search summaries.
- **Acceptance criteria:** every external point has a source; every opportunity is framed as an idea to test, not a fact about the company.
- **Handoff:** `3-pm-problem-to-solution-concept` may draw solution ideas from it, marked as external; never as evidence of what the customer needs.
