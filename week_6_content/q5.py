# An encryption system uses the following rules:
# (1) A letter, upper case or lower case, is replaced by a letter of the same case five places up the
# alphabet. If this falls pass the end of the alphabets, it is wrapped round to the beginning. So “b”
# becomes “g”, and “y” becomes “d”.
# (2) A digit is replaced by a digit larger by 3. If this is greater than 9, it is wrapped round to the other
# end. So 3 becomes 6, and 8 becomes 1.
# (3) All other characters remain unchanged.

# Write a program that reads in a string of characters and produces the encrypted string according to
# the above rules.

string = input("Enter string for encryption: ")
new_string = ""

for i in string: 
    # To deal with lower case letters
    if ord('a')<=ord(i)<=ord('z'):
        i = ord(i) + 5 
        if i>122:
            i = i - (122 - 96)
        
        i = chr(i)
    
    # To deal with upper case letters
    if ord('A')<=ord(i)<=ord('Z'):
        i = ord(i) + 5
        if i>90:
            i = i - (90 - 64)
        
        i = chr(i)
    
    # To deal with digits 
    if i.isdigit(): 
        i = int(i)
        i = i + 3 

        if i > 9: 
            i = i - 10
        i = str(i)
    
    new_string += i

print(new_string)