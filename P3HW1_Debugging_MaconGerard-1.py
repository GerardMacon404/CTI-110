# -------------------------------------------------
# Name: Gerard Macon
# Date: 10/05/2026
# Assignment: P3HW1
# Description:
# This program collects six module grades,
# calculates the lowest grade, highest grade,
# sum of grades, average grade, and determines
# the corresponding letter grade.
# -------------------------------------------------

# Get grades from user
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Calculate results
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest:.1f}")
print(f"Highest Grade:     {highest:.1f}")
print(f"Sum of Grades:     {total:.1f}")
print(f"Average:           {average:.2f}")
print("--------------------------------")
print(f"Your grade is: {letter_grade}")