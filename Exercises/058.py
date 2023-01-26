#                      Guessing Game
# Improve the game in exercise 028 where the computer 
# will "think" of a number between 0 and 10. 
# Only now the player will try to guess until he gets it right, 
# showing in the end how many guesses were needed to win.

from random import randint
a = randint(0,10)
b = 11
count = 1
print('==== Guess the Number ====')
while b != a:
    b = int(input('Chose a Number: '))
    if b != a:
        if b > a:
            print('Wrong, less...' )
        if b < a:    
            print('Wrong!, more...')
        count += 1
print('You WIN !')
print('You had {} tries to win'.format(count))