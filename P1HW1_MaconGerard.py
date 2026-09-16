# Gerard Macon
# 9/16/2026
# P1HW1
# This program calculates exponents and performs
# addition and subtraction using user input.

print("-----Calculating Exponents-----\n")



base = int(input("Enter an integer as the base value: "))

exponent = int(input("Enter an integer as the exponent: "))



power_result = base ** exponent



print()

print(base, "raised to the power of", exponent, "is", power_result, "!!")



print("\n-----Addition and Subtraction-----\n")



start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
subtract_num = int(input("Enter an integer to subtract: "))


final_result = start_num + add_num - subtract_num


print()

print(start_num, "+", add_num, "-", subtract_num, "is equal to", final_result)