# Write a program that prompts for a sentence and then output the number of (1) words, (2) upper
# case letters, (3) lower case letters, (4) digits, and (5) other characters. (Words are strings separated
# by white spaces.)

sentence = input("Key in a String: ")

#initialise counter 
word = 0
upper = 0 
lower = 0
digit = 0
other = 0

for i in sentence: 
    if 97<=ord(i)<=122 or 65<=ord(i)<=90:
        word += 1
    
    elif i.isdigit(): 
        digit += 1
    
    else: 
        other += 1
    
    if i.isupper():
        upper += 1

    if i.islower():
        lower += 1

print("Word Counter:", word)
print("Upper Case Letter Counter:", upper)
print("Lower Case Letter Counter:", lower)
print("Digits Counter:", digit)
print("Other Characters Counter:", other)