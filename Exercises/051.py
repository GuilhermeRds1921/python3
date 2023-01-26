# Develop a program that reads the first 
# term and the ratio for an arithmetic progression.
# Show the first 10 terms of this progression.


num = int(input('Write the First term: '))
prog = int(input(('Write the ratio: ')))
for i in range(0, 10):
    print('{}'.format(num), end = ' ')
    num += prog
