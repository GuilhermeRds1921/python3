# Create a program that reads the lengths of the opposite and adjacent
# sides of a right triangle, calculates, and displays the length of the hypotenuse.

from math import sqrt, pow

adjacent = float(input("Enter the Adjacent Side: "))
opposite = float(input("Enter the Opposite Side: "))
hypotenuse = float(pow(adjacent, 2) + pow(opposite, 2))

print("The hypotenuse is {:.2f}".format(sqrt(hypotenuse)))
