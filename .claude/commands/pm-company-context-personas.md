---
name: pm-company-context-personas
description: "The company's customer personas: what each wants, their common pain points, what makes them say yes, and the terms their sector uses. Pulled from the active context folder, then Notion research and Slack customer channels via MCP. Use in discovery (things to listen for), concepts (user and buyer) and design (know the user). An Enrich step adds external research on comparable products, kept separate from company facts; internal direction wins."
---

# Customer personas

**Role:** a starting picture of the user and the buyer, before the interview replaces it with the real one.
**Users:** `pm-2-discovery-interview`, `pm-3-problem-to-solution-concept`, `pm-4-solution-design`, `pm-6-mvp-review`.
**Target:** each persona has a source. Interview notes always win where they differ.
**Grounding:**
1. `personas.md` in the active context folder
2. Notion via MCP: research notes, sales and customer-success pages
3. Slack via MCP: customer channels
4. Ask me

**Tone:** short and concrete; no invented quotes.

## Step 1: Load
- **Input:** the personas file and any research the MCPs return.
- **Output:** for each persona: role and decisions they own · what they want · common pain points · what makes them say yes (e.g. transparency, speed to value, quantified return) · the terms their sector uses for the main measure.
- **Happy path:** the file covers the user and the buyer of the case in hand.
- **Edge cases:**
  - No persona matches the case: say so, use the closest, and mark the guess.
  - Research is old or from another segment: use it and flag its date and segment.
- **Acceptance criteria:** every persona line has a source. Nothing from a persona appears inside an interview question; personas only guide follow-ups.
- **Handoff:** the calling skill uses the personas to choose follow-ups and frame value, never as evidence. Step 2 can add external context.

## Step 2: Enrich
- **Input:** the personas from Step 1.
- **Output:** a section "External, not company direction": for each persona, how comparable products describe that user and the pain points that recur in public reviews and forums, each with its source.
- **Happy path:** read comparable products' customer stories, public reviews and community threads; paraphrase, never copy, and never invent a quote.
- **Sandboxed:** keep the findings in a separate section, "External, not company direction". Never mix them into the company facts above, and never present them as what the company does or plans.
- **Internal wins:** where an external finding contradicts anything internal (the context folder, Notion, Slack, or what I've said), follow the internal side. There may be a reason the company doesn't go that way, so turn the contradiction into a question for me ("Comparable products do [X]; is there a reason we don't?").
- **Edge cases:** the public picture is thin or from a different segment: say so, and keep it out of interview questions.
- **Acceptance criteria:** every external point has a source; nothing external appears inside an interview question (it only suggests things to listen for).
