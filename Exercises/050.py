# Develop a program that reads two integers and shows 
# the sum of only those that are even. 
# If the value entered is odd, discard it.

pair = 0
for i in range(1,7):
    num = int(input('Write the {}º number: '.format(i)))
    if num % 2 == 0:
        pair += num

print('The sum of the pairs is: {}'.format(pair))
