# 4. Research synthesis (pm-1, Answer: one claim at a time)

> **FICTIONAL EXAMPLE.** Kestrel, Gusta, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

| Claim (from the notes) | In data terms | Result |
|---|---|---|
| "Logins and payslips are safe" | Accuracy on 50 test tickets | **Supported:** Password reset 100%, Missing payslip 100%, Can't log in 98% |
| "Nothing that moves money without a support agent" | Money types and their accuracy | **Supported by the data:** all 4 money types are AI-assisted human, so a support agent checks every answer before it goes out |
| "It should save real hours" | AI tickets × 10 minutes + AI-assisted tickets × 5 minutes | **Supported:** 1,483 AI tickets (47.5%) and 1,499 AI-assisted, 372 hours a month |

Code: [build/test_mvp.js](build/test_mvp.js).
