# 1. Data review (pm-1, Initial review)

> **FICTIONAL EXAMPLE.** Palmer, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

**The data:** 15 ticket types, 2,982 tickets a month in in-app chat; for each, 50 past tickets answered by the agent and graded by the support team.

| # | Finding | Why it might matter (guess) |
|---|---|---|
| 1 | **Half the volume is simple.** Password reset, Missing payslip, Can't log in and Invoice question are 1,255 tickets a month (42%), all 98% accurate or more | Big savings without much risk |
| 2 | **Money types are where the agent is weakest.** Refund request (92%), Payroll run failed (90%) and Change pay date (94%) | The costliest mistakes sit in the least accurate types |
| 3 | **Accuracy alone isn't enough.** Cancel subscription is 100% accurate but a wrong call closes a customer's payroll history | Some types need a person even when the agent is right |

**Questions**
1. The data shows refunds are 92% accurate. What happens today when a refund is wrong?
2. Which ticket types would you never want the agent to send on its own, whatever its accuracy?
