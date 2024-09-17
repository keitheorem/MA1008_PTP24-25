# Write a program to calculate the circumference and area of a circle given the radius, and output the
# results in the format as in this example:
# Radius of circle = 10.00, circumference = 62.83, area = 314.16
# Note that all the numbers have a fixed number of decimal places, and no redundant spaces before
# the number.

import math

# Accept user input 
radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Output the results with two decimal places
print(f"Radius of circle = {radius:.2f}, circumference = {circumference:.2f}, area = {area:.2f}")