---
name: product-glossary
description: "The product glossary: each term the product, its data and its customers use, with a plain meaning, unit and what not to confuse it with. Pulled from the active context folder, then Notion product docs and Figma labels via MCP. Use whenever a skill writes a question, a finding, a screen label or a number."
---

# Product glossary

**Role:** keep the words consistent from data review to screens, in the customer's language.
**Users:** every skill that writes something a customer or reader sees; the designer and engineer who pick up the work.
**Target:** every term on a page or screen appears in the glossary, with the same meaning everywhere.
**Grounding:**
1. `glossary.md` in the active context folder
2. Notion product documentation via MCP
3. Labels already used in the product, from Figma via MCP
4. Ask me

**Tone:** plain words first, the term second ("average yearly loss (AAL)"). One line per term.

## Step 1: Load or extend
- **Input:** the glossary file; any new terms the calling skill has met (data column names, words from interview notes).
- **Output:** a table: term · plain meaning · unit · where it appears (data, screen, report) · don't confuse with.
- **Happy path:** every term needed is already defined; the calling skill uses it as is.
- **Edge cases:**
  - A new term from the data or an interview: add a row marked "proposed", with its source, and show me.
  - The same idea under two names (e.g. one in the data, one in the customer's words): keep the customer's word on screens, map the other to it.
  - A unit is unclear (yearly or cumulative, % or basis points): mark it as a guess and add it to the calling skill's clarifications.
- **Acceptance criteria:** no undefined term on a screen or page; no term means two things.
- **Handoff:** the calling skill uses the glossary wording. Proposed rows wait for my OK before they go in the file.
