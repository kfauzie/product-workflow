# 4. Research synthesis (pm-1, Answer: one claim at a time)

> **FICTIONAL EXAMPLE.** Relaywise, Relay Agent, Relay Studio and Pellmore are invented. The use case and all data are synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

| Claim (from the notes) | In data terms | Choices | Result |
|---|---|---|---|
| "Turning on more automation saves hours" | Net saving if every category is auto-resolved, wrong answers costed | Dec volumes; £32 an agent hour; £15 minor, £400 serious wrong answer | **Not as stated:** auto everything nets **−£151k** a year (921 wrong answers a month, 245 serious) |
| "Order status was safe" | Accuracy lower bound and serious-error rate | Shadow mode, 400 tickets | **Supported:** at least 95.0% accurate, 0.3% serious errors |
| "Billing disputes isn't ready" | Same | 300 tickets | **Supported:** at least 83.2% accurate, 4.9% serious errors; as drafts for agents to approve it nets **£28k** a year instead of **−£243k** auto-resolved |
| "We could hit 20% fewer agent hours" | Agent hours saved a month ÷ current agent hours | Recommended plan | **Exceeds it on paper:** 1,313 hours a month, about 9.4 of 24 agents (39%); worth checking against real handle times in the pilot |

Code: [notebooks/example_numbers.py](notebooks/example_numbers.py) and [build/test_mvp.js](build/test_mvp.js).
