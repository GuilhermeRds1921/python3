# Create a program that reads a person's full name and displays:
# The name in all uppercase and lowercase letters.
# The total number of letters (excluding spaces).
# The number of letters in the first name.

name = input("Enter your full name: ")

print(name.upper())
print(name.lower())

# Count the number of letters (excluding spaces)
spaces = int(name.count(' '))
letters = int(len(name))
total_letters = int(letters - spaces)
print('Your full name has {} letters'.format(total_letters))

# Count the number of letters in the first name
name_parts = name.split()
print('Your first name has {} letters'.format(len(name_parts[0])))
