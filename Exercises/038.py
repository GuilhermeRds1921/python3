# Write a program that reads two whole numbers and compare them, 
# showing a message on the screen: 
# - The first value is greater. 
# - The second value is higher. 
# - There is no higher value, the two are the same.


num1 = int(input('Write the First Number: '))
num2 = int(input('Write the Second Number: '))
if num1 > num2:
    print('The First Number is Higher: {} > {}'.format(num1, num2))
elif num2 > num1:
    print('The Second Number is Higher: {} > {}'.format(num2, num1))
else:
    print('These are the Same: {} = {}'.format(num1, num2))