# Develop a program that reads several integers from the keyboard.
# Show the average of all values and which was the highest 
# and lowest value. The program should ask the user 
# if he wants to continue to enter values.

num = 0
op = 'q'
count = 0
sum = 0
higher = 0
lowest = 0
while op != 'N':
    num = int(input('Write a Number: '))
    sum += num
    if num > higher or count == 0:
        higher = num
    if num < lowest or count == 0:
        lowest = num
    op = str(input('Do You wanna write other number? (N/S): ')).upper()
    count += 1
print('The highest number is: {}'.format(higher))
print('The lowest number is: {}'.format(lowest))
print('The average is: {}'.format(sum / count))


