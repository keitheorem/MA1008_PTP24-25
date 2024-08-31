# Write a program that reads in the length of the three sides of triangle, a, b, and c, and
# computes for the degrees of the three angles using the cosine rule:
# a2 = b2 + c2 – 2bc cos(A)
# where A is the angle opposite the side of length a. You need to import the math library
# and use the acos() function in there. Note that acos() produces an angle in radians.

import math 

# Receive input from user
a = float(input("Key in the value of a: "))
b = float(input("Key in the value of b: "))
c = float(input("Key in the value of c: "))

# Sort the length from shortest to longest (not required for this question)
list_1 = sorted([a,b,c])
smallest_length, medium_length, longest_length = list_1[0], list_1[1], list_1[2]

# To form a triangle, the sum of the two shorter side must be more than the longer side
if longest_length < (smallest_length + medium_length):
    angle = math.acos(-((a**2) - (b**2) - (c**2))/(2*b*c))* (180/math.pi)

    print("The angle is: ", angle, "degrees")

else: 
    print("Invalid Triangle, one of the sides is too long")