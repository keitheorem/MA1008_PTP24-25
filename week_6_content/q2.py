# Write a program that prints the multiplication table between 1 to 12 in a neat table of the form
# 1 2 3 … 11 12
# 2 4 6 … 22 24
# 3 6 9 … 33 36
# : : :
# : : :
# 11 22 33 … 121 132
# 12 24 36 … 132 144
# You are required to use f string to format the output.

for i in range(1, 13):
    for j in range(1,13):
       print(f"{i * j:^4}", end=" ")
    
    print(" ")