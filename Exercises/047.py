# Develop a program that shows on the screen 
# all the even numbers that are in the range between 1 and 50.

for i in range(1,51):
    if i % 2 == 0:
        print(i, end = ' ')