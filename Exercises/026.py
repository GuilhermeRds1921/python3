# Create a program that reads a sentence from the keyboard and displays:
# How many times the letter "A" appears.
# The position where it appears for the first time.
# The position where it appears for the last time.

sentence = input("Enter any sentence: ")
sentence = sentence.lower()

print('Letter A appears:', sentence.count('a'))

print('First "A" position:', sentence.find('a'))

print('Last "A" position:', sentence.rfind('a'))
