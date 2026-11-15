# 6. Design: screen specs (pm-4)

> **FICTIONAL EXAMPLE.** Relaywise, Relay Agent, Relay Studio and Pellmore are invented. The use case and all data are synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

Screens: [design/](design/), captured from the prototype. Borrowed patterns: Stripe (numbers with their method one click away), Linear (calm hierarchy).

| Screen | Example input | Expected output | Happy path | Edge cases | Acceptance criteria | Handoff |
|---|---|---|---|---|---|---|
| 1. Set up | Helpdesk volumes; 2,390 graded tickets; costs | "13,537 tickets, 10 categories" and inputs with sources | Confirm and continue | A category has fewer than 100 graded tickets: flagged, kept with agents | Nothing calculated yet; every input shows its source | → Brief |
| 2. The brief | Confirmed inputs | £349k net a year, hours, wrong answers; mode per category; rollout plan | Read, compare plans, edit the plan, send | Auto everything goes negative: shown, not hidden | Fits one screen; every number has a "how it's calculated" link | → Send, or → Category detail |
| 3. Category detail | One category (Billing disputes) | Accuracy with its lower bound; each mode's hours, wrong answers and £; attach graded tickets | Attach 400 graded tickets; see before and after | File for another category, or too few tickets: say so | The category and plan totals update from the file | → Back to the brief |
| 4. Send for approval | The brief | Drafted message to VP and Finance, PDF | Edit and send | — | Every number in the message matches the brief | → VP and Finance (outside the product) |
