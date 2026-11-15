# 4. Research synthesis (pm-1, Answer: one claim at a time)

> **FICTIONAL EXAMPLE.** Palmer, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

| Claim (from the notes) | In data terms | Result |
|---|---|---|
| "Logins and payslips are safe" | Accuracy on 50 test tickets | **Supported:** Password reset 100%, Missing payslip 100%, Can't log in 98% |
| "Nothing that moves money without a person" | Money types and their accuracy | **Supported by the data:** none of the 4 money types reaches 98% except Change bank details, which still goes to a person to approve |
| "It should save real hours" | Tickets resolved alone × 8 minutes | **Supported:** 1,483 tickets (49.7%), 198 hours a month |

Code: [build/test_mvp.js](build/test_mvp.js).
