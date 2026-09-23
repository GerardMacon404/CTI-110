# Gerard Macon
# 09/23/2026
# P2LAB2
# Uses a dictionary to store vehicle MPG values and calculates gas needed.

# Create dictionary
vehicles = {
"Camaro": 18.21,
"BMW": 52.36,
"Model S": 110,
"Silverado": 26
}

# Get and display keys
keys = vehicles.keys()
print(keys)

# Ask user for vehicle
vehicle = input("\nEnter a vehicle to see its mpg: ")

# Display MPG
mpg = vehicles[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

# Ask for miles
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons = miles / mpg

# Display result
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")# Gerard Macon
# 09/23/2026
# P2LAB2
# Uses a dictionary to store vehicle MPG values and calculates gas needed.

# Create dictionary
vehicles = {
"Camaro": 18.21,
"Prius": 52.36,
"Model S": 110,
"Silverado": 26
}

# Get and display keys
keys = vehicles.keys()
print(keys)

# Ask user for vehicle
vehicle = input("\nEnter a vehicle to see its mpg: ")

# Display MPG
mpg = vehicles[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

# Ask for miles
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons = miles / mpg

# Display result
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")