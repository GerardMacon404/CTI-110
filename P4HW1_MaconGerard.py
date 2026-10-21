# Gerard Macon
# 10/21/2026
# P4HW1
# This program collects test scores, validates the scores,
# drops the lowest score, calculates the average,
# and displays the corresponding letter grade.

"""
Pseudocode

1. Ask the user how many scores they want to enter.
2. Create an empty list to store scores.
3. Use a loop to collect scores.
4. Validate each score:
      - Score must be between 0 and 100.
      - If invalid, display an error message and ask again.
5. Add valid scores to the list.
6. Find the lowest score.
7. Remove the lowest score from the list.
8. Calculate the average of the remaining scores.
9. Determine the letter grade.
10. Display the results.
"""

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create empty list
score_list = []

# Collect scores
for score_num in range(1, num_scores + 1):

    score = float(input(f"\nEnter score #{score_num}: "))

    # Validate score
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        score = float(input(f"Enter score #{score_num} again: "))

    score_list.append(score)

# Find lowest score
lowest_score = min(score_list)

# Remove lowest score from list
score_list.remove(lowest_score)

# Calculate average
average = sum(score_list) / len(score_list)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n")
print("------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")
