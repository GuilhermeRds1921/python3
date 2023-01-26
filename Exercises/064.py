# Develop a program that reads multiple integers from the keyboard. 
# The program will only stop when the user enters the value 999, 
# which is the stop condition. Show how many numbers were entered 
# and what was the sum between them (disregard the Flag).


num = 0
count = 0
sum = 0
while num != 999:
    num = int(input('Write a Number: [999 to stop]: '))
    sum += num
    count += 1
print('{} Numbers were shown'.format(count - 1))
print('Their sum is {}'.format(sum - 999))