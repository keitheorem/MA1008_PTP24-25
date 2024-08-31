# Write a Python program that reads 3 integers, say a, b, and c, and then computes and reports the
# numerical range covered by them. Note that numerical range is defined as the difference between
# the largest and the smallest values among the 3 numbers.

# Receive inputs from user

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Solution 1, using only if statements

# Find the maximum and minimum from the integers
if a > b and a > c: 
    maximum = a 

if b > a and b > c: 
    maximum = b

if c > a and c > b: 
    maximum = c

if a < b and a < c: 
    minimum = a 

if b < a and b < c: 
    minimum = b

if c < a and c < b: 
    minimum = c

range = maximum - minimum
print("The range is", range)

## Solution 2
# maximum = max(a,b,c)
# minimum = min(a,b,c)
# range = maximum - minimum
# print("The range is", range)

## Solution 3

# list_of_integers = [a,b,c]
# list_of_integers = sorted(list_of_integers)
# range = list_of_integers[-1] - list_of_integers[0]
# print("The range is", range)
