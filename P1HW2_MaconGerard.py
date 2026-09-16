# Gerard Macon
# 09/16/2026
# P1HW2 
# This program calculates travel expenses and displays the remaining budget.

# Ask the user to enter their budget 
budget = float(input("Enter Budget: "))

#Ask the user to enter their travel destination
destination = input("\nEnter your travel destination: ")

# Ask the user to enter gas expenses 
gas = float(input("\nHow much do you think you will spend on gas? "))

#Ask the user to enter accomdation expenses 
accomdation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

# Ask the user to enter food expenses 
food = float(input("\nLast, how much you do need for food? "))

# Calculate total expenses 
total_expenses = gas + accomdation + food 

# Calculate remaining balance 
remaining_balance = budget - total_expenses 

# Display travel expense report 
print("\n ------------Travel Expenses------------")
print("Location:", destination)
print("Intial Budget: ", budget)

print("\nFuel: ", gas)  
print("Accomdation:", accomdation)
print("Food:", food)
print("\nRemaining Balance: ", remaining_balance)