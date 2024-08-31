# Write a program that asks the user to input the (x,y) coordinate of a point on a 2D plane and then
# compute and report which quadrant it is in. Recall that points in quadrant 1 have positive x and y,
# points in quadrant 2 have negative x and positive y, points in quadrant 3 have negative x and y,
# whereas points in quadrant 4 have positive x and negative y.
# Note also that you have to check if the given point lies on the x-axis, y-axis, or at the origin. Hint:
# define a small epsilon, say epsilon = 1e-7, to differentiate this; beware of computing equality for
# floating point numbers.

import matplotlib.pyplot as plt 

## Request input from user
x = float(input("Key in the value for x: "))
y = float(input("Key in the value for y: "))


## Conditions requested by question
if x > 0 and y > 0: 
    print("The point lies on the quadrant 1")

elif x < 0 and y > 0: 
    print("The point lies on the quadrant 2")

elif x < 0 and y < 0: 
    print("The point lies on the quadrant 3")

elif x > 0 and y < 0: 
    print("The point lies on the quadrant 4")

elif x == 0 and y == 0: 
    print("Point is on the origin")

elif x == 0: 
    print("The point lies on the y-axis")

elif y == 0: 
    print("The point lies on the x-axis")

maximum = max(x,y)
minimum = min(x,y)

## Plot to show (not required for question, used as visual aid)
plt.figure(figsize=(5,5))
plt.plot(x, y, 'ro')  # 'ro' means red color, round points
plt.title(f'Point ({x}, {y})')
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.axvline(0, color='black', linewidth=1)  # y-axis
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()