---
name: company-context-glossary
description: "The product glossary: each term the product, its data and its customers use, with a plain meaning, unit and what not to confuse it with. Pulled from the active context folder, then Notion product docs and Figma labels via MCP. Use whenever a skill writes a question, a finding, a screen label or a number. An Enrich step adds external research on comparable products, kept separate from company facts; internal direction wins."
---

# Product glossary

**Role:** keep the words consistent from data review to screens, in the customer's language.
**Users:** every skill that writes something a customer or reader sees; any designer or engineer who picks up the work.
**Target:** every term on a page or screen appears in the glossary, with the same meaning everywhere.
**Grounding:**
1. `glossary.md` in the active context folder
2. Notion product documentation via MCP
3. Labels already used in the product, from Figma via MCP
4. Ask me

**Tone:** plain words first, the term second ("[plain meaning] ([TERM])"). One line per term.

## Step 1: Load or extend
- **Input:** the glossary file; any new terms the calling skill has met (data column names, words from interview notes).
- **Output:** a table: term · plain meaning · unit · where it appears (data, screen, report) · don't confuse with.
- **Happy path:** every term needed is already defined; the calling skill uses it as is.
- **Edge cases:**
  - A new term from the data or an interview: add a row marked "proposed", with its source, and show me.
  - The same idea under two names (e.g. one in the data, one in the customer's words): keep the customer's word on screens, map the other to it.
  - A unit is unclear (yearly or cumulative, % or basis points): mark it as a guess and add it to the calling skill's clarifications.
- **Acceptance criteria:** no undefined term on a screen or page; no term means two things.
- **Handoff:** the calling skill uses the glossary wording. Proposed rows wait for my OK before they go in the file. Step 2 can add external context.

## Step 2: Enrich
- **Input:** the glossary from Step 1.
- **Output:** a section "External, not company direction": the terms the industry, comparable products and any regulator use for the same ideas, each mapped to the company's word, with its source.
- **Happy path:** read comparable products' help centres and official guidance; note where the same idea goes by another name, and where one word means different things.
- **Sandboxed:** keep the findings in a separate section, "External, not company direction". Never mix them into the company facts above, and never present them as what the company does or plans.
- **Internal wins:** where an external finding contradicts anything internal (the context folder, Notion, Slack, or what I've said), follow the internal side. There may be a reason the company doesn't go that way, so turn the contradiction into a question for me ("Comparable products do [X]; is there a reason we don't?").
- **Acceptance criteria:** every external term has a source and a mapping; on screens, the customer's and the company's words still win.
