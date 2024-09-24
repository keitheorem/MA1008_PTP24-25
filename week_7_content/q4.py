# Given a date in the short format “dd/mm/yyyy”, print it in the long form “dd Month, yyyy” where
# “Month” is the month in word. For example, “1/1/2018” is printed as “1 January, 2018”. Solve this
# problem using the result from Q3 and the Python dictionary you created for Q 4 in the Tutorial.

date = input("Enter date in format dd/mm/yyyy: ")


if len(date) != 10: 
    print("Invalid Input")

else:
    date_list = []
    date_list.append(date[0:2])
    date_list.append(date[3:5])
    date_list.append(date[6:11])

month_dictionary = {
    "01":"January",
    "02":"February",
    "03":"March",
    "04":"April",
    "05":"May",
    "06":"June",
    "07":"July",
    "08":"August",
    "09":"September",
    "10":"October",
    "11":"November",
    "12":"December",
}

print(f"{date_list[0]} {month_dictionary[date_list[1]]}, {date_list[2]}")
