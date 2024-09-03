## A vending machine has 5 buttons from A to E, depending on the input from the user, the following drinks will be dispensed 
## A - Green Tea - $0.80 
## B - Iced Lemon Tea - $0.90
## C - Milo - $1.00
## D - Coffee - $0.75 

## Write a program that receives the amount of money that the user has inserted into the machine, the choice of drink 
## and outputs the drink choice as well as the change

## Example: 
##  $2.00 and button C is pressed  
##  "Dispensing Milo..."
##  "Change of $1.00 dispensed" 

## Get user input 
amount = float(input("Enter the amount received from user: "))
choice = str(input("Enter the choice of drink (A-D): "))

if choice == "A":

    # Deduct amount 
    amount -= 0.80

    # To deal with user keying in negative value
    if amount < 0: 
        print("Not enough credit")
    
    else:
        print("Green Tea is dispensing")
        print("Change of",amount,"is dispensing")

elif choice == "B": 
    amount -= 0.90
    if amount < 0: 
        print("Not enough credit")
    
    else:
        print("Iced Lemon Tea is dispensing")
        print("Change of",amount,"is dispensing")

elif choice == "C": 
    amount -= 1.00
    if amount < 0: 
        print("Not enough credit")
    
    else:
        print("Milo is dispensing")
        print("Change of",amount,"is dispensing")

elif choice == "D": 
    amount -= 0.75
    if amount < 0: 
        print("Not enough credit")
    
    else:
        print("Coffee is dispensing")
        print("Change of",amount,"is dispensing")

else: 
    print("Invalid option, please run program again and input with valid option (A-D)")

    