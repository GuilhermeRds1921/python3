# A teacher wants to randomly select one of his four students to erase
# the board. Create a program that helps him, reading their names and
# displaying the name of the chosen student.

import random

student1 = input("Enter the name of the First Student: ")
student2 = input("Enter the name of the Second Student: ")
student3 = input("Enter the name of the Third Student: ")
student4 = input("Enter the name of the Fourth Student: ")

students = [student1, student2, student3, student4]
chosen = random.choice(students)

print("The chosen student is {}".format(chosen))
