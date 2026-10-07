# Gerard Macon
# 10/06/2026
# P3HW2 - Employee Pay
# This Program calculates an employee's regular pay,
# overtime pay, also gross pay.

# Pseucode 
# Get employee name.
# Get hours worked
# Get pay rate
# Check hours if hours worked is greater than 40
# If overtime was worked 
# Calculate overtime hours
# Calculate overtime pay 
# Else: 
# Set overtime hours to 0
# Set overtime pay to 0
# Calculate regular pay
# Calculate gross pay
# Display all results

# Gerard Macon
# 10/06/2026
# P3HW2 - Employee Pay
# This program calculates regular pay, overtime pay,
# and gross pay for an employee.

# Pseudocode:
# Get employee name
# Get hours worked
# Get pay rate
# Determine if overtime was worked
# Calculate regular pay
# Calculate overtime pay
# Calculate gross pay
# Display all results

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

# Display results
print("-" * 80)
print(f"Employee name: {employee_name}")
print()

print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay'}")
print("-" * 80)

print(f"{hours_worked:<15.1f}"
      f"{pay_rate:<12.2f}"
      f"{overtime_hours:<12.1f}"
      f"{overtime_pay:<18.2f}"
      f"{regular_pay:<18.2f}"
      f"{gross_pay:.2f}")