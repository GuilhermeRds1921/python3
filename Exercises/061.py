# Remake the exercise 051, reading the first term and 
# the ratio of a PA, showing the first 10 terms 
# of the progression using the while structure.

num = int(input('Write the First Number: '))
ratio = int(input('Write the Ratio: '))
i = 0
while i < 10:
    print('{}  '.format(num), end = '')
    num += ratio
    i += 1
