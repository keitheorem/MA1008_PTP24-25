# Write a program to read in a Python variable and print "Valid" if it is a valid Python variable and
# "Invalid" otherwise. For this exercise, you can assume that Python keywords do not exist, i.e.
# you don’t have to check against them.

variable_name = input("Enter variable name: ")

# Check if the first character is a letter or underscore
if not (('a' <= variable_name[0] <= 'z') or ('A' <= variable_name[0] <= 'Z') or (variable_name[0] == '_')):
    print("Invalid")
else:
    # Check the rest of the characters for valid letters, digits, or underscores
    for char in variable_name:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or (char == '_')):
            print("Invalid")
            break
    else:
        print("Valid")
