# ------------------------------------------------------
# P4LAB_MaconGerard
# Gerard Macon
# 10/19/2026
#
# Pseudocode:
# 1. Import the turtle module.
# 2. Create a screen and set the background color.
# 3. Create a turtle and set its color.
# 4. Draw a square using a FOR loop.
# 5. Move turtle to the top of the square.
# 6. Draw a triangle using a WHILE loop.
# 7.Keep the window open until clicked.
# ------------------------------------------------------

import turtle

# set up screen
screen = turtle.Screen()
screen.bgcolor("lavender")  # Purple-themed background

# Create turtle
house = turtle.Turtle()
house.color("purple")  # Purple turtle

# Move to starting position
house.penup()
house.goto(-50, -100)
house.pendown()

# Draw square for using FOR loop
for side in range(4):
    house.forward(100)
    house.left(90)
# Move to top of square
house.goto(-50, 0)
# Draw triangle using WHILE loop
count = 0
while count < 3:
    house.forward(100)
    house.left(120)
    count += 1

# Keep window open
screen.exitonclick()