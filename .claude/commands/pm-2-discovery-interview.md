---
name: pm-2-discovery-interview
description: "Prepare and run a 10-minute customer discovery interview: a few open questions that get from what the customer asks for to the real problem behind it. Use when preparing, running or reviewing a discovery call."
---

# Discovery interview

**Role:** find the real problem behind what the customer asks for.
**Users:** the PM running the call; the customer answering it.
**Target:** after 10 minutes, the PM can say in one sentence who the user is, what job they're doing, what hurts most, and what success looks like, in the customer's words.
**Grounding:** findings from `pm-1-data-discovery`; `company-context`; `customer-personas` (things to listen for); `product-glossary` (the customer's language); `pm-standard`.
**Tone:** curious, open, one question at a time.

## Principles
- **Problem, not solution.** Questions name the problem, never the requested solution. Don't assume who the user is or what gets built. If they ask for a feature, ask what it would let them do.
- **Be specific.** Ask about a real, recent example, not general habits.
- **The customer's language,** from the glossary and their own words.
- **Open questions.** No hint of the answer you expect and no belief built in.
- **One question per line,** so they get asked one at a time.
- **Personas and common pain points as things to listen for.** Guess which persona the customer and the user are, and which pain points could be behind the ask. Use that to choose follow-ups and to notice them when they come up; never build them into a question. What the customer says beats the persona.

## Step 1: Prepare the guide
- **Input:** the ask, word for word; the pm-1 findings (don't re-run pm-1); the case context.
- **Output:** a Notion page, "[Run]: discovery questions ([customer])", under the parent page named in the active context folder:
  1. **For prep and review:** the pm-1 findings with their numbers, and what any terms mean. Then a divider.
  2. **The guide,** five sections with one or two prompts each, and follow-ups in italics between `<>`:
     - **Need:** Where is the need for X coming from? · Is it just [whoever is asking] asking for this, or do others get the same request?
     - **User journey:** Walk me through the last time you [did the job behind the ask, in their words]: who did what, in which tool, how long it took. · Who would actually use X? · *\<Unexpected step → "How did you end up handling that?"\>* · *\<Hedge words ("generally", "probably") → "You said [word]. Is there any exception?"\>*. If pm-1 found something whose answer could change what gets built, add it as an observation: "I noticed [finding, with a number]. What's behind that?"
     - **Pain points:** Where does most of the time go? · Is that the part that hurts most, or is something else worse? · Optionally: What have you tried to fix it? · *\<Something suspiciously slow → "Why does that happen? It seems simple."\>* · *\<A possible error in their workflow → "What happens when that goes wrong?"\>*
     - **Success criteria** (trust sits here): If this worked, how would you know? · What would the impact be: money, time, or better decisions? · What would you, [your team] and [whoever approves or receives the output] need to see to trust it?
     - **Closing:** **\<Recap\>** three points, biggest problem first, in their words and with their numbers (highlighted) · Anything I missed? · Can I email you short questions?
  3. **An empty Notes section** for the call.
- **Happy path:** every line earns its place; the guide fits a 10-minute call.
- **Edge cases:**
  - The ask is already a problem, not a solution: skip "what would it let you do" and go to the journey.
  - No data findings are relevant: leave out the observation line.
- **Acceptance criteria:** no question names the requested solution or hints at an answer; one idea per line; the recap is highlighted.
- **Handoff:** give me the link; add it to the run notes.

## Step 2: After the call
- **Input:** the notes and transcript in the Notion page.
- **Output:** the claims to test, listed for `pm-1` Step 2 (Answer).
- **Edge cases:** if the recording missed the customer's side, write their answers from memory in a separate section marked "paraphrase, not quotes", and treat them that way downstream.
- **Acceptance criteria:** quotes come from the transcript, not an AI summary.
- **Handoff:** `pm-1` Step 2, then `pm-3-problem-to-solution-concept`.
