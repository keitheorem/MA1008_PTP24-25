# Write a program that converts a date given in a string in the short format “dd/mm/yyyy” to a list
# containing the three fields, [dd, mm, yyyy].

date = input("Enter date in format dd/mm/yyyy: ")


if len(date) != 10: 
    print("Invalid Input")

else:
    date_list = []
    date_list.append(date[0:2])
    date_list.append(date[3:5])
    date_list.append(date[6:11])

    print(date_list)