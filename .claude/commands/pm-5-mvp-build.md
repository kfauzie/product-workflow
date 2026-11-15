---
name: pm-5-mvp-build
description: "Turn the agreed screens into a working first version, fast: one HTML file, numbers calculated by code. Use when building or changing the prototype."
---

# Build: the working first version

**Role:** make the agreed screens work end to end, with real numbers, so the customer can try the flow.
**Users:** me and the customer in the MVP review; the engineer who later takes it to production.
**Target:** the whole flow clicks through with no errors; every number matches the concept's test cases.
**Grounding:** the agreed screens from `pm-4`; the solution concept (workflow, AI / code / people split, success criteria, test cases) from the Notion page in the run notes, fetched fresh; `design-system`; `product-glossary`; `pm-standard`.
**Tone:** match the agreed screens exactly.

## Step 1: First build
- **Input:** the screens, the concept, the data.
- **Output:** one plain HTML file with inline JS and CSS (no framework, no build step), plus a test file and a headless check.
- **Happy path:** build all agreed screens in one go, so the flow can be tried end to end. Calculations sit in plain functions that tests can import. Use the data provided directly. Add a small animation when the step changes; exports leave out buttons and the prototype frame.
- **Edge cases:**
  - No real data: use a small synthetic file, clearly labelled on screen.
  - The concept leaves a number undefined: stop and name it, don't invent a formula.
- **Acceptance criteria:**
  - every number is calculated by code, following the concept's AI / code / people split
  - the concept's test cases pass
  - a headless check (about 10 seconds): the page loads, the main flow clicks through, no errors
  - a first-time user can tell in five seconds what each screen is for and what to do next
- **Handoff:** tell me how to open it; screenshots only if I ask.

## Step 2: Change one thing at a time
- **Input:** my feedback.
- **Output:** an edited file (never regenerate the whole file), with tests and the headless check rerun.
- **Happy path:** each change takes about two minutes.
- **Edge cases:** a change will take longer: tell me first and suggest a smaller step.
- **Acceptance criteria:** tests and the headless check pass after every change.
- **Handoff:** back to me, or to `pm-6-mvp-review` when the flow is ready to show.

## Later, only if I ask
- Branch and PR with screenshots, how to run it and test results
- Dark mode and mobile layout
- A clickable demo that replays precomputed answers
- Hand-off: one PR per screen behind a feature flag, engineer review, staging, then release and measure against agreed targets
