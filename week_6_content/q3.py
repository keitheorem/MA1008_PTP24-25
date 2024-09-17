# Write a program that reads in a word and prints True if the word contains all the vowels and
# False otherwise.

word = input("Key in a word to check if it contains all vowels: ")

j = 0
for i in word:
    i = i.lower()
    if i in 'a' or i in 'e' or i in 'i' or i in 'o' or i in 'u':
        j = j + 1


if j == len(word):
    print("True")