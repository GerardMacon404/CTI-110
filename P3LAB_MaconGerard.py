# -------------------------------------------------
# Name: Gerard Macon
# Date: 10/05/2026
# Assignment: P3LAB
# Description:
# This program accepts a monetary amount from the
# user and calculates the most efficient number
# of dollars, quarters, dimes, nickels, and pennies.
# -------------------------------------------------

# Get amount from user
amount = float(input("Enter the amount of money as a float: $"))

# Convert to pennies
money = int(amount * 100)

# Special case for zero
if money == 0:
    print("No change")
else:

    dollars = money // 100
    money = money - (dollars * 100)

    quarters = money // 25
    money = money - (quarters * 25)

    dimes = money // 10
    money = money - (dimes * 10)

    nickels = money // 5
    money = money - (nickels * 5)

    pennies = money

    # Display results
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(dollars, "Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(quarters, "Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(dimes, "Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(nickels, "Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(pennies, "Pennies")