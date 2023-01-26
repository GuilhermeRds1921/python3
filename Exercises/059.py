# Develop a program that reads two values and displays a menu. 
# Your program should perform the requested operation in each case
# [ 1 ] Sum
# [ 2 ] Multiply
# [ 3 ] High
# [ 4 ] New Numbers
# [ 5 ] Close

num1 = int(input('Write the First value: '))
num2 = int(input('Write the Second value: '))
opt = 0
val = 0
while opt != 5:
    opt = int(input('\n[ 1 ] Sum\n[ 2 ] Multiply\n[ 3 ] High\n[ 4 ] New Numbers\n[ 5 ] Close\nChose an option: '''))
    if opt == 1:
        val = num1 + num2
        print('The Sum is {}'.format(val))
    elif opt == 2:
        val = num1 * num2
        print('The Multiply is {}'.format(val))
    elif opt == 3:
        if num1 > num2:
            val = num1
            print('The highest is {}'.format(val))
        else:
            val = num2
            print('The highest is {}'.format(val))
    elif opt == 4:
        num1 = int(input('Write the First value: '))
        num2 = int(input('Write the Second value: '))
    elif opt == 5:
        opt = 5
    else:
        print('Chose a valid option ')
print('Bye !')

