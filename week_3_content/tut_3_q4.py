# You are given a floating point number which is the number of days. Write a program to
# convert this number to days, hours, minutes and seconds. Here’s an example dialogue:

user_input = float(input('Enter days: '))

days = int(user_input)
hours = int((user_input - days)*24)
minutes = int((((user_input - days)*24) - hours)*60)
seconds = ((((user_input - days)*24) - hours)*60 - minutes)*60
print(days, hours, minutes, seconds)