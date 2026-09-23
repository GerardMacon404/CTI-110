# Gerard Macon
# 09/23/2026
# P2HW1
# Calculates and displays travel expenses in a formatted report.

budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

remaining = budget - gas - hotel - food

print("\n------------Travel Expenses------------")
print(f"{'Location:':15}{destination}")
print(f"{'Initial Budget:':15}${budget:.2f}")
print(f"{'Fuel:':15}${gas:.2f}")
print(f"{'Accommodation:':15}${hotel:.2f}")
print(f"{'Food:':15}${food:.2f}")
print("---------------------------------------")
print(f"\n{'Remaining Balance:':18}${remaining:.2f}")