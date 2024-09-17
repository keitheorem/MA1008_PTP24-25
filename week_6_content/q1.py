# Write a program that would prompt for a string and then print the ASCII value of each character in
# the string.

string = input("Key in a string to receieve the ASCII Value: ")

for i in string: 
    print(ord(i))