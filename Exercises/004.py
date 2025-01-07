# Create a program that reads something from the keyboard and displays on the screen
# its primitive type and all possible information about it.

value = input('Variable: ')

print('The type of the variable is: ', type(value))
print('Is it made of spaces: ', value.isspace())
print('Is it numeric: ', value.isnumeric())
print('Is it alphabetic: ', value.isalpha())
print('Is it all uppercase: ', value.isupper())
print('Is it all lowercase: ', value.islower())
print('Is it capitalized: ', value.istitle())
