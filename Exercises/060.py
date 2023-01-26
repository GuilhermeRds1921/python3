# Develop a program that reads any number and shows its factorial.

num = int(input('Chose a Number: '))
a = -1
x = 1
print('{}!='.format(num), end = '')
while num != 0:
    if num != 1:
        print(' {} x'.format(num), end = '')
    else:
        print(' {}= {}'.format(num, x))
    x = x * num
    num += a
