# Write a program that reads any integer and ask the 
# user to choose the convention base.

num = int(input('Write the number: '))
print('1 - Binary')
print('2 - Octal')
print('3 - Hex')
option = int(input('Select an option: '))
if option == 1:
    print('The Number in Binary: {}'.format(bin(num)[2:]))
elif option == 2:
    print('The Number in Octal: {}'.format(oct(num)[2:]))
elif option == 3:
    print('The Number in Hex: {}'.format(hex(num)[2:]))
else:
    print('Chose a Valid option !')