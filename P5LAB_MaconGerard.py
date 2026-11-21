# -------------------------------------------------
# Name: Gerard Macon
# Date: 11/18/2026
# Assignment: P5LAB
# Description:
# This program simulates a self-checkout machine.
# A random amount owed is generated, the user enters
# a cash payment, and the program calculates and
# displays the change in dollars, quarters, dimes,
# nickels, and pennies.
# -------------------------------------------------

import random

# Pseudocode:
# Generate random amount owed
# Display amount owed
# Ask user for cash amount
# Calculate change owed
# Call disperse_change function
# Display change in dollars, quarters, dimes,
# nickels, and pennies


def disperse_change(amount):

    money = round(amount * 100)

    if money == 0:
        print("No change")

    else:
        dollars = money // 100
        money %= 100

        quarters = money // 25
        money %= 25

        dimes = money // 10
        money %= 10

        nickels = money // 5
        money %= 5

        pennies = money

        if dollars > 0:
            if dollars == 1:
                print("1 Dollar")
            else:
                print(f"{dollars} Dollars")

        if quarters > 0:
            if quarters == 1:
                print("1 Quarter")
            else:
                print(f"{quarters} Quarters")

        if dimes > 0:
            if dimes == 1:
                print("1 Dime")
            else:
                print(f"{dimes} Dimes")

        if nickels > 0:
            if nickels == 1:
                print("1 Nickel")
            else:
                print(f"{nickels} Nickels")

        if pennies > 0:
            if pennies == 1:
                print("1 Penny")
            else:
                print(f"{pennies} Pennies")


def main():

    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${amount_owed:.2f}")

    cash = float(input("How much cash will you put in the self-checkout? "))

    while cash < amount_owed:
        print("Not enough cash.")
        cash = float(input("How much cash will you put in the self-checkout? "))

    change = round(cash - amount_owed, 2)

    print(f"Change is: ${change:.2f}")
    print()

    disperse_change(change)


main()