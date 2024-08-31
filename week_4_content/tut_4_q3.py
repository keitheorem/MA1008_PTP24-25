# Write a Python program to first read 3 integers representing a person’s birthday (day, month and
# year) followed by another 3 integers representing another person’s birthday. Then, your program has
# to compare the integers, and report who is older, or whether they have the same birthday.
# In this question, you cannot use any logical operators (and, or, and not), as well as mathematical
# operators including multiplication (*) and addition (+). But you can use relational operators for
# comparison.

## Receive input from user 
print("Enter Person 1 birthday details")
day_person_1 = int(input("Please enter the day: "))
month_person_1 = int(input("Please enter the month: "))
year_person_1 = int(input("Please enter the year: "))

print("Enter Person 2 birthday details")
day_person_2 = int(input("Please enter the day: "))
month_person_2 = int(input("Please enter the month: "))
year_person_2 = int(input("Please enter the year: "))


## Compare age starting from year -> month -> day, note the use of elif instead of just using multiple if
if year_person_1 < year_person_2: 
    print("Person 1 is older")

elif year_person_2 < year_person_1: 
    print("Person 2 is older ")

elif month_person_1 < month_person_2: 
    print("Person 1 is older")

elif month_person_2 < month_person_1: 
    print("Person 2 is older ")

elif day_person_1 < day_person_2: 
    print("Person 1 is older")

elif day_person_2 < day_person_1: 
    print("Person 2 is older ")

else: 
    print("They have the same birthday")
