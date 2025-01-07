# The same teacher from the previous challenge wants to randomly choose the order of
# student presentations. Create a program that reads the names of four students and displays
# the randomized order.

import random

name1 = input("Enter First Name: ")
name2 = input("Enter Second Name: ")
name3 = input("Enter Third Name: ")
name4 = input("Enter Fourth Name: ")

students = [name1, name2, name3, name4]
random.shuffle(students)

print("The order of presentation is: ")
print(students)

