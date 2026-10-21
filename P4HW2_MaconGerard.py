# Gerard Macon
# 10/21/2026
# P4HW2
# This program calculates payroll information for multiple
# employees and displays payroll totals.

"""
Pseudocode

1. Initialize totals and employee counter.
2. Ask user for employee name.
3. While employee name is not "Done":
    - Ask for hours worked.
    - Ask for pay rate.
    - Calculate overtime hours.
    - Calculate overtime pay.
    - Calculate regular pay.
    - Calculate gross pay.
    - Display employee payroll information.
    - Add values to running totals.
    - Increment employee counter.
    - Ask for another employee name.
4. When user enters "Done":
    - Display total employees entered.
    - Display total overtime pay.
    - Display total regular pay.
    - Display total gross pay.
"""

employee_count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name != "Done":

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    print()
    print(f"Employee name: {employee_name}")
    print()

    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay'}")
    print("-" * 90)

    print(f"{hours_worked:<15.1f}"
          f"{pay_rate:<12.2f}"
          f"{overtime_hours:<12.1f}"
          f"{overtime_pay:<18.2f}"
          f"{regular_pay:<18.2f}"
          f"{gross_pay:.2f}")

    print()

    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")