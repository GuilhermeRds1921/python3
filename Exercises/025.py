# Create a program that reads a person's name
# and checks if they have "Silva" in their name.

name = input('Enter your full name: ')
name = name.upper().split()

print('SILVA' in name)
