---
name: 5-pm-mvp-build
description: "Turn the agreed screens into a working first version, fast: one HTML file, numbers calculated by code. Use when building or changing the prototype."
---

# Build: the working first version

**Role:** make the agreed screens work end to end, with real numbers, so the customer can try the flow.
**Users:** me and the customer in the MVP review; the engineer who later takes it to production.
**Target:** the whole flow clicks through with no errors; every number matches the concept's test cases.
**Grounding:** the agreed screens from `4-pm`; the solution concept (workflow, AI / code / people split, success criteria, test cases) from the Notion page in the run notes, fetched fresh; `design-system`; `product-glossary`; `0-pm-standard`.
**Tone:** match the agreed screens exactly.

## Step 1: First build
- **Input:** the screens, the concept, the data.
- **Output:** one plain HTML file with inline JS and CSS (no framework, no build step), plus a test file and a headless check.
- **Happy path:** build all agreed screens in one go, so the flow can be tried end to end. Calculations sit in plain functions that tests can import. Use the data provided directly. Add a small animation when the step changes; exports leave out buttons and the prototype frame.
- **Edge cases:**
  - No real data: use a small synthetic file, clearly labelled on screen. Build it source first: write the reference the examples depend on (the policy, rulebook, price list or catalogue), then derive every example from it, so each example quotes its source by ID, every outcome follows from the source, and a test checks the quotes. Read each example as a domain expert would: does the input, the response and the verdict hold together?
  - The concept leaves a number undefined: stop and name it, don't invent a formula.
- **Acceptance criteria:**
  - when the brief gives data or rules, tests check them exactly (every row, every rule outcome); when it gives wording rules (banned words, no em dashes), a check enforces them
  - interactive controls recalculate everything that depends on them, and the tests cover the override paths, not just the default
  - every number is calculated by code, following the concept's AI / code / people split
  - text that quotes a number (a reason, a label, a warning) reads it from the same value as the number it describes, so the two never disagree when the number changes
  - anything the user may want to check (a rule, a source document) is one click away from where it is cited, opening at the exact item
  - the concept's test cases pass
  - a headless check (about 10 seconds): the page loads, the main flow clicks through, no errors
  - a first-time user can tell in five seconds what each screen is for and what to do next
- **Handoff:** tell me how to open it; screenshots only if I ask. If the work is public, a live link (static hosting) and checks that run on every push make it easy to review.

## Step 2: Change one thing at a time
- **Input:** my feedback.
- **Output:** an edited file (never regenerate the whole file), with tests and the headless check rerun.
- **Happy path:** each change takes about two minutes.
- **Edge cases:** a change will take longer: tell me first and suggest a smaller step.
- **Acceptance criteria:** tests and the headless check pass after every change. A change to wording or examples leaves the numbers untouched unless I ask; prove it by comparing the data before and after.
- **Handoff:** back to me, or to `6-pm-mvp-review` when the flow is ready to show.

## Later, only if I ask
- Branch and PR with screenshots, how to run it and test results
- Dark mode and mobile layout
- A clickable demo that replays precomputed answers
- Hand-off: one PR per screen behind a feature flag, engineer review, staging, then release and measure against agreed targets
