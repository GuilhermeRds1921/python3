# Develop a program that plays even or odd with the computer. 
# The game will only be stopped when the player loses, 
# showing the total number of consecutive victories he has won at the end of the game.

from random import randint
while True:
    print('=' * 30)
    print('\nLets Play Even or Odd! \n')
    count = 0
    while True:
        print('=' * 30)
        num = int(input('Choose a number: '))
        pc = randint(0,10)
        sum = num + pc
        count += 1
        choice = str(input('Choose Even or Odd [E/O]: ')).upper()
        if sum %2 == 0 and choice =='E':
            print(f'You Chose {num} and pc {pc} = {sum}')
            print('You Win!! Lets Play Again')

        elif sum %2 != 0 and choice == 'O':
            print(f'You Chose {num} and pc {pc} = {sum}')
            print('You Win!! Lets Play Again')
            
        else:
            print(f'You Chose {num} and pc {pc} = {sum}')
            print('You Lose ')
            print(f'You make {count} points ')
            break
    break
