# Develop a program that makes the computer play Jokenpô with you

from random import randint
print('\t\t\t\t\t==== Rock Paper Scissors ====')
you = int(input(''' 
[ 3 ] Rock!
[ 2 ] Paper!
[ 1 ] Scissor!
Chose your move:'''))
pc = randint(-3,-1)
itens = ('none','Scissor', 'Papaer', 'Rock')
if (you + pc) == 0:
    print('You chose: {}'.format(itens[you]))
    print('PC chose: {}'. format(itens[pc * -1]))
    print('Draw!')
elif (you + pc) == 2 or (you + pc) == -1:
    print('You chose: {}'.format(itens[you]))
    print('PC chose: {}'.format(itens[pc * -1]))
    print('You WIN! ')
else:
    print('You chose: {}'.format(itens[you]))
    print('PC chose: {}'.format(itens[pc * -1]))
    print('You Lose! ')
