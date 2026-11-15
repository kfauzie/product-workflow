"""FICTIONAL: synthetic data for the Kestrel example. Kestrel, Gusta, their customers and every ticket are invented.

Writes data/ticket_types.json: 15 ticket types with monthly volume (in-app chat), results on 50 test tickets,
risk if wrong, a one-line reason, and 3 example tickets. Each example has the customer's
message, Kestrel's reply, the rule from Gusta's support playbook that applies, and the grading AI's verdict with a reason.
Also writes data/support_playbook.json (read by build/playbook.html) and .md, the fictional playbook every answer is graded against.
Run from examples/kestrel:  python3 notebooks/make_data.py
"""
import json
# name, tickets a month, correct of 50, cost, cost example, moves money,
# examples: (customer request, Kestrel's reply, playbook rule id, correct, one-line reason)
# Gusta's customer support playbook. FICTIONAL: Kestrel's answers are graded against these rules.
# (section, [(rule id, rule)])
PLAYBOOK = [
 ("Every ticket", [
   ("GEN-1", "Check the person's role on the account (account owner, admin or employee) before helping with any change. If they can't make it, say who can."),
   ("GEN-2", "Check the account itself (pay runs, HMRC submissions, invoices, plan history, settings) before answering. Never answer from general knowledge alone."),
   ("GEN-3", "When the customer does something themselves, give the exact place in Gusta, e.g. Settings > Company."),
   ("GEN-4", "Never promise a date, refund or outcome this playbook doesn't allow."),
   ("GEN-5", "Hand over to a support agent when the customer asks for a person, staff pay is late, no rule covers the question, or it needs tax, legal or employment-status advice, a data request, or a suspected bug looked at."),
   ("GEN-6", "Plain words, no jargon, one question at a time."),
 ]),
 ("Signing in", [
   ("ACC-1", "Forgotten password: send one reset link. If it hasn't arrived, ask the customer to check their junk folder and, in Gmail, the Promotions tab for an email from Gusta."),
   ("ACC-2", "Reset links expire after 30 minutes and only the newest one works. Say both every time you send one."),
   ("ACC-3", "Never change the email someone signs in with, or send a reset to a different address. Only the account owner can change it, under Settings > Users."),
   ("ACC-4", "Accounts lock for 15 minutes after 5 wrong passwords. Explain the wait and send a reset link."),
   ("ACC-5", "Lost 2-step codes: offer the backup codes saved at setup. Without them, hand over to a support agent to check identity. Never switch off 2-step verification in chat."),
   ("ACC-6", "Can't sign in on the mobile app only: check the app version first. If it's out of date, ask them to update before anything else."),
 ]),
 ("Payslips", [
   ("PAY-1", "Payslips are on each employee's record under Documents. Admins can resend them from there."),
   ("PAY-2", "Employees get their payslips in the Gusta employee app once each payroll is finalised. Share the employee app guide."),
   ("PAY-3", "Payslips missing for a recent run: check the run is finalised and the payslip release date before anything else."),
   ("PAY-4", "Send payslips only to the email address on the employee's record, never to an address given in chat."),
 ]),
 ("Company details", [
   ("CO-1", "Only the account owner can change the registered office in Gusta, and only once the change is registered at Companies House."),
   ("CO-2", "HMRC holds a separate PAYE correspondence address. When a customer moves, remind them to check it with HMRC as well as updating Gusta."),
   ("CO-3", "Payslips show the business address set under Settings > Company, not the registered office."),
 ]),
 ("Employees", [
   ("EMP-1", "Before a new employee's first pay run, Gusta needs their National Insurance number, date of birth, start date, bank details and a P45 or starter checklist."),
   ("EMP-2", "No P45: the employee's answer on the HMRC starter checklist (statement A, B or C) sets the tax code. Never guess a code."),
   ("EMP-3", "Part-time staff: set their contracted hours. Salary is pro rata to the full-time week."),
   ("EMP-4", "Each employee is on one pay schedule. Weekly-paid staff need a weekly schedule; if the account has none, create it first under Settings > Pay schedules."),
 ]),
 ("Bank details", [
   ("BANK-1", "A new company paying account needs the account owner's approval and a verification call from Gusta. It applies from the next pay run; any payment file already made must be recreated."),
   ("BANK-2", "Never act on an emailed or messaged request to change an employee's bank details. The admin must confirm with the employee by phone, on the number already on file."),
   ("BANK-3", "No bank changes within 3 working days of payday. Hand over to a support agent for a manual check."),
 ]),
 ("Billing", [
   ("BILL-1", "Duplicate charge: confirm it on the invoice, then refund the duplicate in full."),
   ("BILL-2", "Cancellations take effect at the end of the current billing month. That month is still charged."),
   ("BILL-3", "Annual plans: refunds for unused months are pro rata and reviewed by a support agent before they're paid."),
   ("BILL-4", "Explain invoice charges line by line, using the invoice breakdown. Each employee paid in a month is charged at the per-employee rate."),
   ("BILL-5", "Invoices are under Settings > Billing > Invoices."),
   ("BILL-6", "Before explaining a price change, check the account's plan history and the number of employees paid."),
 ]),
 ("Pay runs", [
   ("RUN-1", "BACS payment file rejected: check the bank authorisation first. If it has expired, show how to renew it and give the deadline to resubmit for payday."),
   ("RUN-2", "FPS rejected by HMRC: name the employees and the field at fault (often the National Insurance number), say pay isn't affected, then resubmit once fixed."),
   ("RUN-3", "Before suggesting any rerun, check whether the payment was already sent. If it was, never rerun; hand over to a support agent."),
   ("RUN-4", "A new pay date applies from the next pay period. Runs must be approved 3 working days before payday for BACS."),
   ("RUN-5", "Payday on a weekend or bank holiday: pay on the working day before, and bring the approval deadline forward to match."),
   ("RUN-6", "A pay date can't be brought forward inside the 3-working-day BACS window. Hand over to a support agent."),
 ]),
 ("Tax forms", [
   ("TAX-1", "P60s are under Reports > Year end. Admins send them to employees from there; employees must have them by 31 May."),
   ("TAX-2", "A P60 differs from the payslips: check for corrections sent to HMRC in that tax year before answering."),
   ("TAX-3", "CIS subcontractors aren't employees: they aren't paid through payroll and get monthly CIS statements, not payslips or P60s. Never give the employee process for them."),
 ]),
 ("Cancelling", [
   ("CAN-1", "Before cancelling: run the final payroll, mark the last FPS as final with the date the business stopped employing staff, issue P45s, export the records (Reports > Export all), and the account owner confirms."),
   ("CAN-2", "Records stay available, read-only, for 6 years after cancelling, then are deleted. Remind customers they must keep payroll records for 3 years after the tax year ends."),
 ]),
 ("Holiday and leave", [
   ("HOL-1", "Statutory holiday is 5.6 weeks a year. Part-time is pro rata: 3 days a week is 16.8 days."),
   ("HOL-2", "Holiday pay for the first 4 weeks includes regular overtime and commission, averaged over the last 52 weeks of pay, not just basic pay."),
   ("HOL-3", "Irregular-hours and part-year workers build up holiday at 12.07% of the hours they work each pay period."),
   ("HOL-4", "Leave is recorded on the employee's record under Leave."),
 ]),
 ("Reports", [
   ("REP-1", "Payroll summary: default to the last full tax year (6 April to 5 April) unless the customer gives dates."),
   ("REP-2", "\"Last quarter\" means the most recent full calendar quarter."),
   ("REP-3", "Only the account owner and admins can export salaries."),
 ]),
 ("Pensions", [
   ("PEN-1", "Staff aged 22 or over earning more than £10,000 a year are enrolled automatically, after any postponement (up to 3 months) the employer has set."),
   ("PEN-2", "Opt-outs within a month of enrolment get their deductions refunded in the next run. Never encourage an opt-out."),
   ("PEN-3", "Contributions are worked out on qualifying earnings (£6,240 to £50,270), so they change with pay. Check for pay changes that month before confirming a deduction."),
 ]),
]
RULE = {i: r for _, rs in PLAYBOOK for i, r in rs}

T = [
 ("Password reset", 468, 50, "Low", "Low: customer stays locked out a little longer", False, [
   ("Reset email never came and payroll's due Friday.", "I've sent a new reset link to the email you sign in with. If it isn't in your inbox in a few minutes, check your junk folder and, in Gmail, the Promotions tab for an email from Gusta.", 'ACC-1', True, 'Sent one new link and named the junk folder and Promotions tab.'),
   ("I've lost access to my old work email. Can you send the reset to my personal one?", "I can't send it to a different address. Your account owner can change the email you sign in with under Settings > Users; then I'll send a reset link there.", 'ACC-3', True, "Didn't send a reset to an unverified address; pointed to the account owner."),
   ('Link says expired, I clicked it straight away.', "Sorry about that. I've sent you a fresh reset link.", 'ACC-2', False, "Didn't say only the newest link works; the customer opened an older email and it failed again.")]),
 ("Can't log in", 268, 49, "Low", "Low: customer stays locked out longer, which can hold up payroll", False, [
   ('Got a new phone and my authenticator codes are gone.', "You can sign in with one of the backup codes you saved when you set up 2-step verification. If you don't have them, I'll pass you to a support agent, who will check your identity before resetting it.", 'ACC-5', True, "Offered backup codes and a verified handover; didn't switch off 2-step in chat."),
   ("It says I'm locked out after too many tries.", "Your account locked after 5 wrong passwords. It unlocks by itself in 15 minutes; I've sent a reset link so you can choose a new password then.", 'ACC-4', True, 'Explained the 15-minute wait and sent a reset link.'),
   ('The app just spins since the update, but the website works.', "Try signing out of the app, clearing its cache in your phone's settings, and signing in again.", 'ACC-6', False, 'Skipped the version check; the app was 3 versions behind and needed updating.')]),
 ("Missing payslip", 342, 50, "Low", "Low: employee waits longer for a payslip", False, [
   ("Can you resend Sam's March payslip?", "I've resent Sam's March payslip to the email address on Sam's employee record. You can also resend it yourself from Sam's record, under Documents.", 'PAY-4', True, "Sent it only to the email on Sam's record."),
   ('Where do my staff download their payslips?', "Your staff get their payslips in the Gusta employee app once each payroll is finalised. Here's a guide to share with them: Getting started with the employee app.", 'PAY-2', True, 'Pointed to the employee app and shared the guide.'),
   ("Two staff say they've got no payslip this month.", "I've resent this month's payslips to both of them.", 'PAY-3', False, "Didn't check the release date: payslips were set to appear on payday, two days later, so nothing was missing.")]),
 ("Update company address", 97, 50, "Medium", "Medium: company details wrong in Gusta or with HMRC (the tax authority), so letters go astray", False, [
   ("We've moved office. How do I change the address on payslips?", 'Payslips show your business address, which you can change under Settings > Company > Business address. If your registered office has moved too, update it at Companies House first, then in Gusta.', 'CO-3', True, 'Pointed to the business address for payslips, and the right order for the registered office.'),
   ('Our accountant changed our registered office at Companies House. Does payroll update?', 'Not by itself. As the account owner, update it under Settings > Company > Registered office. Also check the PAYE address HMRC holds for you, as payroll letters go there.', 'CO-2', True, 'Covered the separate PAYE address HMRC holds.'),
   ('Can you change our registered office to 14 Mill Lane?', 'Done: your registered office is now 14 Mill Lane.', 'CO-1', False, 'Changed it for an admin, not the account owner, and before it was registered at Companies House.')]),
 ("Add a new employee", 251, 48, "Medium", "Medium: new starter set up wrongly: tax code, pay or pay schedule", False, [
   ('New starter on Monday, no P45 yet. What tax code?', "Ask them to fill in HMRC's starter checklist. Their answer to statement A, B or C sets the tax code, and Gusta applies it when you add them under Employees > Add employee.", 'EMP-2', True, 'Used the starter checklist instead of guessing a code.'),
   ('New starter is part time, 3 days a week.', 'When you add them, set their contracted hours to 3 days a week. Gusta then pays 3/5 of the full-time salary.', 'EMP-3', True, 'Set contracted hours so the salary is pro rata.'),
   ('Adding a weekly-paid warehouse worker to our monthly payroll.', 'Add them under Employees > Add employee and choose your monthly pay schedule.', 'EMP-4', False, 'Put a weekly-paid worker on the monthly schedule; the account had no weekly schedule, so one was needed first.')]),
 ("Change bank details", 154, 49, "High", "High: pay sent from or to the wrong account, possibly a fraudster's", True, [
   ("We've switched banks. What do I need to change?", "Your account owner can add the new paying account under Settings > Bank account, and our team confirms it on a short verification call. It applies from your next pay run, so recreate any payment file you've already made.", 'BANK-1', True, 'Covered owner approval, the verification call and the payment file.'),
   ('Got an email from Jo with new bank details. Can you update them before Friday?', 'Before changing anything, please call Jo on the number already on file to confirm the new details. Emailed requests are a common way fraudsters divert salaries.', 'BANK-2', True, 'Asked for a call-back on the number on file before any change.'),
   ("We've changed our company account number and payroll goes out tomorrow.", "I've started the change so tomorrow's payment comes from the new account. Your account owner needs to approve it first.", 'BANK-3', False, 'Payday was 1 working day away; inside 3 days it should have gone to a support agent for a manual check.')]),
 ("Refund request", 121, 46, "High", "High: money refunded or withheld wrongly", True, [
   ('Charged twice this month??', "I can see two identical charges on your November invoice. I've refunded the second one in full.", 'BILL-1', True, 'Confirmed the duplicate on the invoice, then refunded it in full.'),
   ('We cancelled on 20 February but were still billed for February.', "Sorry about that. I've refunded February's charge in full.", 'BILL-2', False, 'February was still due: the cancellation only took effect at the end of February.'),
   ('Can I get my money back for the rest of our annual plan?', 'Annual plans can get a pro-rata refund for unused months. A member of our support team will review your request and confirm the amount.', 'BILL-3', True, 'Sent the pro-rata refund for a support agent to review.')]),
 ("Payroll run failed", 189, 45, "High", "High: staff paid late or twice, or pay reported wrongly to HMRC", True, [
   ('HMRC rejected my submission and staff are already paid.', "Your staff's pay isn't affected; only the report to HMRC was rejected. Priya Shah's National Insurance number is in the wrong format. Correct it on her record, then resubmit the FPS from Payroll > Submissions.", 'RUN-2', True, "Named the employee and field, and said pay wasn't affected."),
   ('The payment file failed and payday is Friday.', 'Your bank authorisation for BACS payments expired on 1 November. Renew it under Settings > Bank account > Authorisation, then resubmit by the end of today so staff are paid on Friday.', 'RUN-1', True, 'Found the expired authorisation and gave the BACS deadline.'),
   ("Payroll didn't go through and staff are asking where their pay is.", 'Sorry about that. Rerun payroll from Payroll > Runs and your staff will be paid.', 'RUN-3', False, "Didn't check the payment: it had already been sent, so a rerun would pay staff twice.")]),
 ("Tax form question", 298, 47, "High", "High: wrong figures or forms go to staff or HMRC", False, [
   ('Where are the P60s for my staff?', "They're under Reports > Year end. You can send each employee their P60 from there; they need to have them by 31 May.", 'TAX-1', True, 'Gave the right place and the 31 May deadline.'),
   ("My P60 doesn't match my payslips added up.", 'Your P60 includes a correction made in November, after your tax code changed, which was sent to HMRC separately. Payslips before November show the old figures.', 'TAX-2', True, 'Found the November correction before answering.'),
   ('Do my subbies get a P60?', "Yes: add them under Employees and they'll get a P60 at year end with everyone else.", 'TAX-3', False, 'Treated CIS subcontractors as employees; they get monthly CIS statements, not P60s.')]),
 ("Cancel subscription", 88, 50, "High", "High: account closed wrongly, or final HMRC steps missed", False, [
   ('Closing the business at the end of the month. What do I need to do?', "Sorry to see you go. Run your final payroll, mark the last FPS as final with the date you stopped employing staff, give everyone a P45, and export your records under Reports > Export all. Once your account owner confirms, I'll set up the cancellation.", 'CAN-1', True, "Covered final payroll, final FPS, P45s, export and the owner's confirmation."),
   ('Please cancel at the end of this month.', "I've set your cancellation for the end of this billing month; this month is still charged. Before then, export your records under Reports > Export all.", 'BILL-2', True, "Cancelled for the end of the billing month and said it's still charged."),
   ('Moving to another provider. What happens to our data?', 'Your records are deleted when your account closes, so export anything you need first.', 'CAN-2', False, "Records stay read-only for 6 years, not deleted at closing, and it didn't mention the 3-year record-keeping rule.")]),
 ("Change pay date", 132, 47, "High", "High: staff paid on the wrong day", True, [
   ('Can we pay on the 25th instead of the last day of the month?', 'Yes. Change it under Settings > Pay schedules; it starts from your next pay period. Approve each run 3 working days before the 25th so the BACS payment arrives on time.', 'RUN-4', True, 'Started it from the next pay period and gave the BACS deadline.'),
   ("Payday's a bank holiday. When do we pay?", "Pay on the working day before. I've moved this month's pay date to Friday, so approve the run by Tuesday for BACS.", 'RUN-5', True, 'Moved pay to the working day before and brought the deadline forward.'),
   ("Can we bring this month's payday forward to tomorrow?", "Done: this month's pay date is now tomorrow.", 'RUN-6', False, 'Tomorrow was inside the 3-working-day BACS window; staff would have been paid late.')]),
 ("Invoice question", 177, 49, "Low", "Low: customer misunderstands a charge", False, [
   ("Why is this month's invoice higher?", 'You paid 2 more employees this month, Lena and Tom, added on 12 November. Each employee paid in a month is charged at the per-employee rate, on the second line of your invoice.', 'BILL-4', True, 'Explained the line from the invoice breakdown.'),
   ('Where do I download invoices for my accountant?', "They're under Settings > Billing > Invoices. Here's October's.", 'BILL-5', True, 'Sent the invoice and showed where invoices are kept.'),
   ('Why did our price go up?', 'Gusta raised prices for all customers this year.', 'BILL-6', False, "Didn't check the plan history: they had moved to a bigger plan in September.")]),
 ("Holiday pay calculation", 170, 43, "High", "High: staff paid too much or too little holiday pay", False, [
   ('How much holiday does a 3-day-a-week employee get?', 'Statutory holiday is 5.6 weeks a year, so someone working 3 days a week gets 16.8 days.', 'HOL-1', True, 'Gave the pro-rata figure.'),
   ("Why is Dan's holiday pay more than his normal week?", "That looks like an error. Dan's holiday pay should match his basic pay, so I'd reduce it.", 'HOL-2', False, 'Dan works regular overtime, which must be included; the higher figure was right.'),
   ('Our casual staff, how much holiday do they get?', 'For irregular-hours workers, holiday builds up at 12.07% of the hours they work each pay period. Gusta works this out when you set their contract to irregular hours.', 'HOL-3', True, 'Applied the irregular-hours rule.')]),
 ("Export payroll report", 131, 50, "Low", "Low: customer gets wrong or incomplete figures", False, [
   ('My accountant needs payroll totals for the tax year.', "Here's your payroll summary for the last full tax year, 6 April to 5 April, as a spreadsheet. Tell me if your accountant needs different dates.", 'REP-1', True, 'Defaulted to the last full tax year.'),
   ('How do I export last quarter?', 'Go to Reports > Payroll summary, set the dates to April to June, and click Export.', 'REP-2', False, 'The ticket came in October; the most recent full quarter was July to September.'),
   ('Can I get a list of all employees with their salaries?', "Here's the list of your 24 employees with their salaries.", 'REP-3', True, 'Checked the person is an admin before exporting salaries.')]),
 ("Pension deduction question", 96, 44, "Medium", "Medium: pension deducted wrongly, too much or too little", False, [
   ('Why has pension been taken from our new starter?', "Staff aged 22 or over earning more than £10,000 a year are enrolled automatically. You postpone enrolment by 3 months, and Sam's postponement ended in October, so deductions started this month.", 'PEN-1', True, "Explained enrolment using the account's postponement setting."),
   ('New guy wants to opt out. Can I stop it?', "He opts out himself through the pension provider. If he does within a month of enrolment, record it on his record under Pension and his deductions are refunded in the next run. You can't encourage him to opt out.", 'PEN-2', True, "Covered the opt-out window and refund, and didn't encourage it."),
   ("Amy's pension looks wrong this month.", "This month's pension deduction is the same as last month's, so it looks right.", 'PEN-3', False, "Didn't check her pay: a pay rise hadn't reached the pension calculation, so the deduction was too low.")]),
 ("Other (no matching type)", 140, 29, "High", "High: customer acts on an answer no rule covers", False, [
   ('Is my cleaner self-employed or staff?', "If they set their own hours and bring their own equipment, they're self-employed, so you don't need to add them to payroll.", 'GEN-5', False, 'Gave an employment-status judgement instead of handing over to a support agent.'),
   ('An ex-employee wants a copy of all the data we hold on him.', "That's a subject access request, which you need to answer within a month. I'll pass you to a member of our support team, who can help you export his records.", 'GEN-5', True, 'Handed the data request over to a support agent.'),
   ('The tax on one payslip looks wrong. Is it a bug?', "Gusta's tax calculations follow HMRC's rules, so the figure is right. Check the employee's tax code.", 'GEN-5', False, 'Dismissed a possible bug instead of handing over to a support agent.')]),
]
# accuracy: where Kestrel is used (AI or AI-assisted human), every ticket from the last 30 days (= tickets a month); where it isn't (Human), a daily test on 50 recent tickets
LIVE = {
 'Password reset': (468, 467),
 "Can't log in": (268, 263),
 'Missing payslip': (342, 340),
 'Update company address': (97, 96),
 'Add a new employee': (251, 242),
 'Change bank details': (154, 152),
 'Refund request': (121, 111),
 'Payroll run failed': (189, 170),
 'Tax form question': (298, 280),
 'Cancel subscription': (88, 87),
 'Change pay date': (132, 124),
 'Invoice question': (177, 174),
 'Holiday pay calculation': (170, 146),
 'Export payroll report': (131, 129),
 'Pension deduction question': (96, 84),
 'Other (no matching type)': (50, 29),
}
REASON = {
 "Password reset": "{p} accurate and a wrong call costs little",
 "Can't log in": "{p} accurate and a wrong call costs little",
 "Missing payslip": "{p} accurate and a wrong call costs little",
 "Update company address": "{p} accurate and a wrong call is easy to fix",
 "Add a new employee": "{p} accurate: good, but not enough to send unchecked",
 "Change bank details": "{p} accurate, but a wrong call is costly, so a support agent checks",
 "Refund request": "{p} accurate; moves money, so a support agent checks every draft",
 "Payroll run failed": "{p} accurate; staff pay is at stake, so a support agent checks",
 "Tax form question": "{p} accurate, but a wrong figure is costly, so a support agent checks",
 "Cancel subscription": "{p} accurate, but a wrong call is costly, so a support agent checks",
 "Change pay date": "{p} accurate; moves money, so a support agent checks",
 "Invoice question": "{p} accurate and a wrong call costs little",
 "Holiday pay calculation": "{p} accurate: enough for a useful draft, checked by a support agent",
 "Export payroll report": "{p} accurate and a wrong call costs little",
 "Pension deduction question": "{p} accurate: a useful draft, not enough to send unchecked",
 "Other (no matching type)": "Only {p} accurate: no playbook rule covers these",
}
pct = lambda n: (f"{LIVE[n][1] / LIVE[n][0] * 100:.0f}%" if LIVE[n][0] == 50 else f"{LIVE[n][1] / LIVE[n][0] * 100:.1f}%")
out = {"label": "FICTIONAL and SYNTHETIC: Kestrel example, not real data",
       "product": "Kestrel", "customer": "Gusta", "channel": "In-app chat", "minutes_ai": 10, "minutes_assisted": 5,
       "types": [{"name": n, "tickets": v, "tested": LIVE[n][0], "correct": LIVE[n][1], "risk": c, "risk_example": ce, "reason": REASON[n].format(p=pct(n)),
                  "examples": [{"message": a, "proposed": b, "rule_id": rl, "rule": RULE[rl], "correct": ok, "verdict_reason": rs} for a, b, rl, ok, rs in ex]}
                 for n, v, k, c, ce, mm, ex in T]}
json.dump(out, open("data/ticket_types.json", "w"), indent=1)
json.dump({"label": "FICTIONAL and SYNTHETIC: Gusta support playbook, not real", "customer": "Gusta",
           "sections": [{"name": sec, "rules": [{"id": i, "rule": r} for i, r in rs]} for sec, rs in PLAYBOOK]},
          open("data/support_playbook.json", "w"), indent=1)
with open("data/support_playbook.md", "w") as f:
    f.write("# Gusta customer support playbook (FICTIONAL)\n\nThe rules Kestrel follows and the grading AI checks every answer against. Synthetic, made by `../notebooks/make_data.py`.\n")
    for sec, rs in PLAYBOOK:
        f.write(f"\n## {sec}\n" + "".join(f"- **{i}** {r}\n" for i, r in rs))
print(len(T), "types,", sum(t[1] for t in T), "tickets a month")
