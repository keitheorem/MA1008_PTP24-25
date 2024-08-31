# Write a Python program that requests the number of hours one worked in a month and then prints
# out the gross pay, taxes, and net pay. Assume that the pay structure and tax rate are as follows:
# • Basic pay rate = $10.00 per hour
# • Overtime (>160 hours) = one and a half time of the basic pay rate
# • Tax rate = 10% for first $1000, 20% for next $500, and 30% for the rest

# Receive inputs from user
hours = int(input("Key in the number of hours worked for this month: "))
overtime_pay = 0 

## Total Pay Calculation
if hours > 160: 
    overtime_hours = hours - 160 
    overtime_pay = overtime_hours * 10.0 * 1.5
    hours = 160

basic_pay = hours * 10.0
total_pay = basic_pay + overtime_pay 

print("The gross pay for this month is: $", total_pay)

## Taxes Calculation 

# Handle cases where pay is less than $1000
if total_pay <= 1000: 
    tax = total_pay * 10/100 

# Handle cases where pay is between 1000 and 1500 
if 1500 >= total_pay > 1000:
    tax = (1000*(10/100))  +  (total_pay-1000)*(20/100) 

# Handle cases where pay is above 1500 
if total_pay >= 1500: 
    tax = (1000*(10/100)) + (500*(20/100)) + (total_pay-1500)*(30/100)

print("The taxes for this month is: $", tax)

# Compute net pay i.e. pay after taxes
net_pay = total_pay - tax

print("The net pay for this month is: $", net_pay)
