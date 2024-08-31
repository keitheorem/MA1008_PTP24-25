# Write a program that reads in a number between 1 and 7 and prints “Monday” for 1, “Tuesday” for
# 2, …, “Sunday” for 7, and “Illegal input” if the number is out of range.

# Receive input from user
number = int(input("Key in a number for the corresponding day of the week: "))

if number == 1:  
    print("Monday")

elif number == 2:  
    print("Tuesday")
    
elif number == 3:  
    print("Wednesday")

elif number == 4:  
    print("Thursday")

elif number == 5:  
    print("Friday")

elif number == 6:  
    print("Saturday")

elif number == 7:  
    print("Sunday")

else: 
    print("Illegal input")