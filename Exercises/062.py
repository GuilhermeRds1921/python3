# Improve exercise 061 by asking the user if he 
# wants to show more terms. 
# The program ends when he says he wants 0 terms.

num = int(input('Write the First Number: '))
ratio = int(input('Write the Ratio: '))
i = 0
while i < 10:
    print('{} '.format(num), end = '')
    num += ratio
    i += 1
    if i == 10:
        aux = int(input('\nHow many terms do you wanna see? '))
        i -= aux
print('Bye! ')