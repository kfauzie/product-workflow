---
name: pm-1-data-discovery
description: "Look at a customer's data before and during discovery to find the findings worth putting in front of them, and turn each into an interview question. Two steps: Initial review (before the interview) and Answer (test a claim or answer one question, e.g. to synthesise what the customer said)."
---

# Data discovery

**Role:** give the PM questions they couldn't ask without the data. People talk more when they react to their own numbers than to hypotheticals.
**Users:** the PM before and after the interview; the customer, who reacts to the findings.
**Target:** 2 to 5 real findings, each a question for the customer; every number traceable to code.
**Grounding:** the data file (given by me, or found in Notion or Slack via MCP); `company-context-overview` (which product produced it, what decisions it feeds); `company-context-glossary` (columns, units); `pm-0-standard` (communication guide).
**Tone:** plain words, one number per finding, guesses labelled as guesses.

## Ground rules
- Run code for every number, never estimate by reading the file, and keep the code.
- Stay generic: look for patterns, not for a known story.
- The data may not be perfect. Flag quality issues briefly; only dig in if a gap is big enough to change the findings.
- Say where each measure comes from (live use, a test sample, an estimate) and how big the base is. A figure from a small test and one from a full month of real use should never look the same.
- Be suspicious of numbers that are too neat (every value round, totals that add up perfectly): real data rarely looks like that.

## Step 1: Initial review (before the interview)
- **Input:** the data file and the customer's ask, word for word. Start with `python3 tools/lens.py profile <csv>` if the file is a wide export (one row per item, with measures repeated across columns for each option or period); otherwise analyse by hand.
- **Output (one page):**
  1. The data: the first five rows (if wide, the identifiers, the descriptors and one set of measures, saying how many columns are left out); the data in two lines; a one-line data quality check and whether it changes the findings.
  2. Findings: each a plain-words headline with one number and what it's compared against.
  3. Why it might matter: one line each, labelled as a guess.
  4. The question it becomes: it names the problem, never the requested solution or who would use it. "The data shows X. What's behind that?", then a follow-up that names the thing ("How do you handle [X] today?").
  5. Clarifications to confirm, as questions (which option or period they use, units, what a blank means).
  6. Looked at, nothing to ask about.
  7. Follow-ups the PM can ask Claude Code.
- **Happy path:** understand the file (what one row is, the identifiers, descriptors and measures, the dimensions packed into column names, anything ambiguous). Then look for three kinds of finding:
  - **What's changed:** recent vs older records, by count and by value.
  - **What's concentrated:** a small share of items, or one segment, carrying most of the value or risk. Check by value as well as count.
  - **What's missing or odd:** gaps, duplicates, stale or unscored records. Treat oddities as clues to past mistakes or workarounds.
  For each, check whether the choice of option or period changes the picture.
- **Edge cases:**
  - The file doesn't fit the wide layout (`lens` raises ShapeError): analyse by hand.
  - Nothing relevant to the customer's need: say so. Never pad.
  - A data gap that wouldn't change an answer goes in the quality check, not the findings.
- **Acceptance criteria:** 2 to 5 findings; each has one number, its comparison and its code; no question names a solution.
- **Handoff:** the findings and questions go into the run notes, then to `pm-2-discovery-interview`.

## Step 2: Answer (after the interview, or any time)
- **Input:** one claim the customer made, or one question, plus the data.
- **Output:**
  1. The claim or question in data terms, with anything ambiguous flagged
  2. The choices made and why (e.g. option, period, by count or by value)
  3. The result, with the code and rows used. For a claim: supported, not supported or unclear
  4. Anything surprising or contradicting what they said, as a follow-up question
- **Happy path:** one claim at a time, each tested and logged in the run notes.
- **Edge cases:** the data can't answer it: say what's missing and who might have it.
- **Acceptance criteria:** every verdict has the code and rows behind it.
- **Handoff:** the tested claims go to `pm-3-problem-to-solution-concept` as evidence.
