# Write a program that calculates the length of a word from 
# the input and prints it out together 
# with the word in the format:

# "word has N letters"

# There will always be more than one letter in the word.

# Sample Input 1:
# serendipity

# Sample Output 1:
# serendipity has 11 letters

word = input()
len_ = len(word)
print(word,"has",len_,"letters")