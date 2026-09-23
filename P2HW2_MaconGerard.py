# Gerard Macon
# 09/23/2026
# P2HW2
# Enter six module grades, store them in a list,
# and display the lowest grade, highest grade,
# sum of grades, and average grade.

# Input grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store grades in list
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculate results
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade: {lowest}")
print(f"Highest Grade: {highest}")
print(f"Sum of Grades: {total}")
print(f"Average: {average:.2f}")
print("--------------------------------")