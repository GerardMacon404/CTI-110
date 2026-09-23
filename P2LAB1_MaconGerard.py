# Gerard Macon
# 09/23/2026
# P2LAB1
# Calculates the diameter, circumference, and area of a circle.

import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))

# Calculate values
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results
print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"\nThe circumference of the circle is {circumference:.2f}")
print(f"\nThe area of the circle is {area:.3f}")