# Create a program that reads a person's full name
# and displays the first and last names separately.

name = input('Enter your full name: ')
name = name.split()

# Get the first and last name
first_name = name[0]
last_name = name[-1]

print('First name:', first_name)
print('Last name:', last_name)
