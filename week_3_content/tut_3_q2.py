# 2. Write a program to evaluate the polynomial a4x^4 + a3x^3 + a2x^2 + a1x + a0 via these steps:
# i. Read in the coefficients of the polynomial
# ii. Read in the value of x
# iii. Compute and print the value of the polynomial given the above values

# Solution 1 

# Request Inputs from the users
a4 = int(input("Key in the value for a4: "))
a3 = int(input("Key in the value for a3: "))
a2 = int(input("Key in the value for a2: "))
a1 = int(input("Key in the value for a1: "))
a0 = int(input("Key in the value for a0: "))
x = int(input("Key in the value for x: "))

result = (a4*x**4) + (a3*x**3) + (a2*x**2) + (a1*x) + a0

print(result)


# # Solution 2
# order = int(input("Key in the order of the polynominal: "))
# x = int(input("Key in the value for x: "))
# coefficient_list = []
# result = 0

# for i in range(order + 1): 
#     coefficient = int(input(f"Key in the value of a{i}: "))
#     coefficient_list.append(coefficient)

# for y in range(len(coefficient_list)): 
#     result += coefficient_list[y] * x ** y
    
# print(result)

