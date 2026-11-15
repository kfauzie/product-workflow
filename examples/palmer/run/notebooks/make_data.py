"""FICTIONAL: synthetic data for the Palmer example. Palmer, its customers and every ticket are invented.

Writes data/ticket_types.json: 15 ticket types with monthly volume (in-app chat), results on 50 test tickets,
cost of a wrong call, whether the type moves money, and 3 example tickets with the agent's proposed reply.
Run from examples/palmer/run:  python3 notebooks/make_data.py
"""
import json
# name, tickets a month, correct of 50, cost, cost example, moves money, 3 examples: (ticket, agent's reply or action, correct, note if wrong)
T = [
 ("Password reset", 468, 50, "Low", "Low: customer stays locked out a little longer", False, [
   ("I've forgotten my password and the reset email isn't arriving.", "Sent a new reset link and asked them to check spam for an email from Palmer.", True, ""),
   ("Can you reset my password? I changed jobs and lost access to my old email.", "Explained that the account owner must change the login email first, and how to ask them.", True, ""),
   ("Reset link says expired.", "Sent a fresh link and explained links expire after 30 minutes.", True, "")]),
 ("Can't log in", 268, 49, "Low", "Low: customer tries again or asks for a person", False, [
   ("My 2-step code isn't arriving by text.", "Sent the code by email instead and showed how to update the phone number.", True, ""),
   ("It says my account is locked.", "Unlocked after the failed-attempt timeout and sent a reset link.", True, ""),
   ("I can't log in on my phone but it works on my laptop.", "Told them to clear the app cache.", False, "The app needed an update; clearing the cache didn't fix it")]),
 ("Missing payslip", 342, 50, "Low", "Low: employee is pointed to the wrong month", False, [
   ("One of my staff can't find her March payslip.", "Showed where payslips sit under Employees > Documents and how to resend March.", True, ""),
   ("Where do employees download payslips?", "Linked the employee app guide and the resend option.", True, ""),
   ("Payslip for last Friday isn't showing.", "Explained payslips appear once the payroll run is approved, and that it is still in draft.", True, "")]),
 ("Update company address", 97, 50, "Medium", "Medium: tax letters go to the old address", False, [
   ("We've moved office, how do I change our address?", "Updated the registered address after confirming the account owner, and noted tax letters follow in 1 to 2 weeks.", True, ""),
   ("Change our trading address to 14 Mill Lane.", "Updated the trading address and left the registered address unchanged, as asked.", True, ""),
   ("Our address on payslips is wrong.", "Showed that payslips use the trading address and updated it.", True, "")]),
 ("Add a new employee", 251, 48, "Medium", "Medium: employee set up on the wrong pay schedule", False, [
   ("How do I add someone starting Monday?", "Walked through Add employee and the tax details needed before the first run.", True, ""),
   ("New starter is part time, 3 days a week.", "Set up a part-time contract with pro-rata salary.", True, ""),
   ("Adding a weekly-paid worker to our monthly payroll.", "Added them to the monthly schedule.", False, "Should have created a weekly pay schedule first")]),
 ("Change bank details", 154, 49, "High", "High: payroll paid from or to the wrong account", True, [
   ("We've switched banks, need to update the account payroll is paid from.", "Drafted the change and asked for owner approval and a verification call before it takes effect.", True, ""),
   ("Employee gave me new bank details.", "Drafted the update on the employee record, flagged for a person to check against the signed form.", True, ""),
   ("Change our company account number, urgent, payroll is tomorrow.", "Drafted the change for tomorrow's run.", False, "Changes inside 3 days of a run need a manual check; it should have flagged the deadline")]),
 ("Refund request", 121, 46, "High", "High: wrong refund paid out", True, [
   ("You charged us twice this month.", "Confirmed the duplicate charge and proposed a refund of the second payment.", True, ""),
   ("We cancelled in January but were billed in February.", "Proposed a full refund for February.", False, "Cancellation took effect at the end of February, so no refund was due"),
   ("Can I get a refund for the unused months on our annual plan?", "Explained the annual plan terms and proposed a pro-rata refund for review.", True, "")]),
 ("Payroll run failed", 189, 45, "High", "High: staff paid late", True, [
   ("Payroll failed with a bank error.", "Identified an expired bank authorisation and showed how to renew it, then rerun.", True, ""),
   ("Run failed, says tax code missing for 2 employees.", "Listed the 2 employees and where to add their tax codes.", True, ""),
   ("Payroll didn't go through and staff are asking where their pay is.", "Told them to rerun payroll.", False, "Payment was already sent; rerunning would have paid staff twice")]),
 ("Tax form question", 298, 47, "Medium", "Medium: customer files with the wrong figure", False, [
   ("Where do I find the year-end tax forms for my staff?", "Showed Reports > Year end and how to send forms to employees.", True, ""),
   ("Why is the tax on this form different from the payslips?", "Explained the form includes a correction made in November.", True, ""),
   ("Do I need to file anything for a contractor?", "Said contractors are filed the same way as employees.", False, "Contractors use a different form")]),
 ("Cancel subscription", 88, 50, "High", "High: account and payroll history closed by mistake", False, [
   ("We're closing the business, how do I cancel?", "Explained the final payroll steps, how to export records, then drafted the cancellation for approval.", True, ""),
   ("Cancel at the end of this month please.", "Drafted the cancellation for the end of the month and listed what to export first.", True, ""),
   ("Thinking of cancelling, what happens to our data?", "Explained records are kept for 6 years and can be exported any time.", True, "")]),
 ("Change pay date", 132, 47, "High", "High: staff paid on the wrong day", True, [
   ("Can we pay staff on the 25th instead of the last day?", "Showed how to change the pay date from next month and the bank cut-off.", True, ""),
   ("Bank holiday on payday, can we pay a day early?", "Moved this month's pay date one working day earlier.", True, ""),
   ("Move this month's pay date to tomorrow.", "Moved the pay date to tomorrow.", False, "Tomorrow is past the bank cut-off; staff would have been paid late")]),
 ("Invoice question", 177, 49, "Low", "Low: customer is confused about a charge", False, [
   ("What is this extra charge on our invoice?", "Explained the charge is for 2 employees added mid-month.", True, ""),
   ("Can I get a copy of last month's invoice?", "Sent the invoice and showed where invoices are kept.", True, ""),
   ("Why did our price go up?", "Said prices rose for all customers.", False, "Their price rose because they moved to a bigger plan")]),
 ("Holiday pay calculation", 170, 43, "Medium", "Medium: employee underpaid for leave", False, [
   ("How is holiday pay worked out for part-time staff?", "Explained pro-rata holiday based on contracted days.", True, ""),
   ("Employee says her holiday pay is too low.", "Said the calculation was correct.", False, "Overtime should have been included in her holiday pay"),
   ("How do I record 2 days of leave?", "Showed how to add leave on the employee's calendar.", True, "")]),
 ("Export payroll report", 131, 50, "Low", "Low: wrong date range exported", False, [
   ("Need a payroll summary for our accountant.", "Exported the summary for the last tax year as a spreadsheet.", True, ""),
   ("How do I export last quarter?", "Showed the date filter on Reports and exported Q3.", True, ""),
   ("Can I get a list of all employees with salaries?", "Exported the employee list with salaries.", True, "")]),
 ("Pension deduction question", 96, 44, "Medium", "Medium: wrong deduction explained to staff", False, [
   ("Why has pension been taken from a new starter?", "Explained automatic enrolment after the waiting period.", True, ""),
   ("Employee wants to opt out of the pension.", "Showed how to record the opt-out and refund the first deduction.", True, ""),
   ("Pension amount looks wrong this month.", "Said it was correct.", False, "A salary change hadn't been passed to the pension calculation")]),
]
out = {"label": "FICTIONAL and SYNTHETIC: Palmer example, not real data",
       "company": "Palmer", "channel": "In-app chat", "minutes_per_ticket": 8, "test_tickets_per_type": 50,
       "types": [{"name": n, "tickets": v, "correct": k, "cost": c, "cost_example": ce, "moves_money": mm,
                  "examples": [{"ticket": a, "reply": b, "correct": ok, "note": note} for a, b, ok, note in ex]} for n, v, k, c, ce, mm, ex in T]}
json.dump(out, open("data/ticket_types.json", "w"), indent=1)
print(len(T), "types,", sum(t[1] for t in T), "tickets a month")
