# Write a program that reads in the coefficients of a quadratic equation and prints the roots when real
# roots exist and the message “No real roots” otherwise.
# If you fancy a greater challenge, in the case of no real roots, return the complex roots instead.

import math

## Quadratic Function = ax^2 + bx + c
a = int(input("Key in the value for a: "))
b = int(input("Key in the value for b: "))
c = int(input("Key in the value for c: "))

# For real root to exist b^2 - 4ac must be more than or equal 0 
condition = (b**2) - (4*a*c)

if condition >= 0: 
    print("Real roots exist")
    root_1 = (-b + math.sqrt((b**2) - (4*a*c)))/2*a
    root_2 = (-b - math.sqrt((b**2) - (4*a*c)))/2*a

    print("Root 1 is: ", root_1)
    print("Root 2 is: ", root_2)

# Otherwise real roots will not exist
else : 
    print("No real roots")
    real_root = -b/(2*a)
    complex_root = math.sqrt(-((b**2) - (4*a*c)))/(2*a)

    print(f"Root 1 is: {real_root} + i{complex_root}")
    print(f"Root 1 is: {real_root} - i{complex_root}")