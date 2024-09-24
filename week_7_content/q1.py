# Write a program to read in a Python variable and print "Valid" if it is a valid Python variable and
# "Invalid" otherwise. Account for Python keywords. In the case of invalid, issue a message to
# inform the programmer why it is invalid.

import keyword

variable_name = input("Enter a Python variable: ")

if keyword.iskeyword(variable_name):
    print(f"Invalid: '{variable_name}' is a Python keyword.")

elif not variable_name.isidentifier():
    print(f"Invalid: '{variable_name}' is not a valid identifier. Variable names must start with a letter or underscore and contain only letters, digits, or underscores.")
    
else: 
    print("Valid")