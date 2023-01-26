# Develop a program that reads multiple integers from the keyboard.
# The program will only stop when the user enters the value 999, 
# which is the stop condition.
# Show how many numbers were entered and the sum between them.

count = sum = 0
while True:
    num = int(input('Write a Number: (999 to stop)'))
    if num == 999:
        break
    count += 1
    sum += num
print(f'You wrote {count} numbers')
print(f' And the sum is: {sum}')