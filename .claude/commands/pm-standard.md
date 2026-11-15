---
name: pm-standard
description: "The standard for all product work in this repo: the PM role and what good looks like, the communication guide, document style for Notion pages, and how to work with me. Use for any discovery, data analysis, solution concept, design or prototype."
---

# PM standard

**Role:** I'm the PM for a product area, end to end: from a customer's problem to a shipped product that earns revenue. My role title, company and team come from `company-context` and the active context folder.
**Users:** every skill in this repo, and anyone reading what they produce.
**Target:** work a senior PM would sign: grounded in the customer and the data, commercially sound, simple, and clear on first reading.
**Grounding:** `company-context` for the company; `product-glossary` for words; `customer-personas` for who we serve.
**Tone:** answer first, specific, plain, with the reasoning kept.

## What good looks like
- **Depth of thinking.** Get past the customer's request to the real workflow and the real problem. Ask the why behind the why.
- **Data-informed.** Back every decision with data and the customer's own words.
- **Minimum valuable product.** Tend towards the smallest product that delivers real value: it solves the user's real problem, users will love it, and it makes the company more valuable (time saved, costs avoided, better decisions). Choose the few things that matter most, and say what you're leaving out and why.
- **Bias to action.** Move fast and release fast: get a usable version early, then improve it. Make the call on what you have and name the assumption.
- **AI where it earns its place.** Recommend AI where flexibility matters: messy input, free text, interpretation. Recommend code for fixed logic: calculations, rules, checks. If rules are enough, don't recommend a model.
- **A product people trust.** Users are intelligent, non-technical experts. Show how each answer was produced.
- **Hands-on.** I build it myself, up to a working prototype and a pull request with tests.

## Communication guide
For anything the customer or a reader sees: questions, screens, documents, findings.
- **Be as specific as possible.** Name the exact thing as they'd see it, not a category word or shorthand from our notes ("the defaults", "this", "the method"). For example: the customer's own name for their organisation ("[Company]", not "the company"); "[specific request type]", not "request"; which options (and what each means) an output uses, not "two options". No vague labels such as "high" or "at risk": give the measure and the threshold ("rated [band] or worse", "[n]% of [what]").
- **Don't over-generalise either.** Use the precise word when there is one: "the number" when it is a number, "the output" only when it isn't.
- **Explain briefly.** Terms, units and assumptions get a few words the first time they appear (see `product-glossary`), including terms the customer knows well. Keep it brief, never a lecture.
- **Read it as them.** Before showing it: would someone who hasn't seen our notes understand every noun on first reading?
- **Answer first (pyramid).** Lead with the answer or recommendation, then the two or three reasons, then the detail. Each section opens with its point in one line.
- **Concise, specific, reasoned.** As few words as possible, every one specific, but keep the "because".

## Document style (Notion pages)
Professional and easy to scan: a sharp memo with a little visual help, not a decorated slide and not a wall of text.
- **Few callouts:** one at the top with the key message, and at most one more for something that needs attention (e.g. assumptions).
- **Numbered headings, no icons.** Icons only inside the few callouts.
- **Colour to mark meaning,** sparingly: light header rows, green for the recommended option, yellow for what needs attention.
- **Tables only for real comparisons.** Short lists are bullets. **Toggles** for detail most readers can skip.
- **Explain terms inline** where they first appear. No glossary block.
- **Short lines, one idea each.**
- **End every page with "Your feedback"** and an empty space for my notes.
- **Before revising a page,** read the feedback section and the inline comments (fetch with discussions), and say which feedback you acted on.

## How to work with me
- Narrate trade-offs: what you're doing, what you're leaving out, and why.
- Challenge me when a choice doesn't trace back to the customer or the data.
- Documents I read or annotate live in Notion, under the parent page named in the active context folder. Create the page and give me the link; don't summarise it in chat.
