# Develop a program that reads an integer 
# and tells if it is a prime number

num = int(input('Write a number: '))
a = 0
for i in range(2,num):
    if num % i == 0:
        a += 1
if a == 0:
    print('{} is prime. '.format(num))
else:
    print('{} isnt prime. '.format(num))