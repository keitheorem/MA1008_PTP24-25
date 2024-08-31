# A year is a leap year if it is divisible by 4 and not by 100, or if it is divisible by 400. Otherwise, it is not
# a leap year. Write one single Boolean expression that will return True if a given year is a leap year
# and False otherwise. Write a program that reads in an integer value for the year and uses the above
# expression to print “Leap year” or “Not leap year” accordingly.

# Condition 1 divisible by 4 and not by 100 
# Condition 2 divisible by 400 

# Receive input from user 
year = int(input("Please enter the year to determine if it is a leap year: "))

# Enter condition in a single line
if ((year%4 ==0) and (year%100 !=0)) or (year%400 == 0):
    print("Leap year")

else: 
    print("Not leap year")

