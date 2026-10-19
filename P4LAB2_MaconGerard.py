# Gerard Macon
# 10/19/2026
# This program displays a multiplication table
# for a positive integer. Negative integers are not accepted.
# The user can choose to run the program multiple times.


# Pseudocode:
# 1. Ask the user to enter an integer.
# 2. Determine whether the integer is positive or negative.
# 3. If the integer is negative, display a message that
# 4. negative numbers are not accepted.
# 5. If the integer is zero or greater, use a for loop to
# 6. display the multiplication table from 1 through 12.
# 7. Ask the user if they want to run the program again.
# 8. If the user enters "yes", repeat the program.
# 9. If the user enters "no", end the program.
# 10. Display an ending message before exiting.


"""
PSEUDOCODE

1. Set a variable to control the program loop.
2. Start a while loop that continues while the user wants to run again.
3. Ask the user to enter an integer.
4. Check if the integer is negative.
   a. If the integer is less than 0:
      - Display a message that negative values are not accepted.
   b. Otherwise:
      - Use a for loop to display the multiplication table
        from 1 through 12.
      - Multiply the entered number by each value from 1 to 12.
      - Display each multiplication result.
5. Ask the user if they want to run the program again.
6. If the user enters "yes":
   - Continue the while loop.
7. If the user enters "no":
   - Exit the while loop and end the program.
8. Display a goodbye message.
"""

run_again = "yes"

while run_again.lower() == "yes":

    number = int(input("Enter an integer: "))

    if number < 0:
        print("This program does not handle negative numbers.")

    else:
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    run_again = input("\nWould you like to run again? (yes/no): ")

print("Program ended.")