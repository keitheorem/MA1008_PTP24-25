# Write a program to read in a sentence of your choice and print every word in the sentence, one
# word per line. Words are separated by one or more spaces, or a punctuation. Provide two different
# solutions:
# i. Use the string method split().
# ii. Without using the string method split()


## First solution with split
sentence = "Hello World Many"

words = sentence.split()

for word in words: 
    print(word)


## Second solution without split
list_words = []
word = ""
for i in sentence: 
    word += i

    if i == " ":
        list_words.append(word)
        word = ""
        
list_words.append(word)
    
for word in list_words: 
    print(word)
