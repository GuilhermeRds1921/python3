#           Guessing Game
# Write a program where the computer "thinks" of an integer between 0 and 5
# and asks the user to guess which number was chosen.
# The program should display whether the user won or lost.

from random import randint

computer_choice = randint(0, 5)

user_guess = int(input("Enter a number between 0 and 5: "))

if user_guess == computer_choice:
    print("You guessed correctly!")
else:
    print("You guessed wrong.")

print(f"The number was {computer_choice}.")
