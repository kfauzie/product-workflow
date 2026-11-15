# 6. Design (4-pm)

> **FICTIONAL EXAMPLE.** Kestrel, Gusta, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

One page: [design/1-overview.png](design/1-overview.png) (Password reset expanded), and with an override on Refund request: [design/2-override.png](design/2-override.png).

| Part | Shows | Acceptance criteria |
|---|---|---|
| Header | This page, Kestrel, customer, user, job to be done | Short labelled lines, no paragraph |
| Three numbers | Share handled by AI, hours saved, wrong answers reaching customers | Match the table to the ticket |
| Decision rules | AI, AI-assisted human, Human, colour-coded | Above the table |
| Setting | A dropdown per row, defaulting to the recommendation; "Setting overridden" tag; a warning above the recommendation; "Apply all recommendations" | The three numbers update live |
| Table | One row per type: tickets, accuracy on 50, cost of a wrong call with an example, recommendation, reason | Every row follows the rule |
| Examples | 3 tickets under each row: customer request, Kestrel proposed, customer support rule, verdict from the grading AI | Password reset open by default; clicking a row expands it; types below 100% show a Wrong example |
