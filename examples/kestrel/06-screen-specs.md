# 6. Design (pm-4)

> **FICTIONAL EXAMPLE.** Kestrel, Gusta, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

One page: [design/1-overview.png](design/1-overview.png) (Password reset expanded), and with an override on Refund request: [design/2-override.png](design/2-override.png).

| Part | Shows | Acceptance criteria |
|---|---|---|
| Header | This page, Kestrel, customer, user, job to be done | Short labelled lines, no paragraph |
| Three numbers | Share handled by AI, hours saved, wrong answers reaching customers | Match the table to the ticket |
| Decision rules | AI, AI-assisted human, Human, colour-coded | Above the table |
| Setting | A dropdown per row, defaulting to the recommendation; "Setting overridden" tag; a warning above the recommendation; "Apply all recommendations" | The three numbers update live |
| Table | One row per type: estimated tickets a month, expected accuracy, cost of a wrong call with an example, recommendation, reason | Every row follows the rule |
| Examples | Recent tickets under each row (3, or 5 for Password reset) as lines, one per ticket, in four columns: customer request, Kestrel's reply, customer support rule, evaluation (grading AI). The grading AI's Wrong tickets first; the heading counts them ("2 of 5 wrong"). Colour only on the verdict pill (Wrong on a light red tint, Correct as green text); rows are white; Override verdict is a neutral button | Password reset open by default; clicking a row expands it; types below 100% show a Wrong example; on a phone each ticket stacks with its four labels |
