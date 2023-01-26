# Develop a program that calculates the sum between all the odd numbers 
# that are multiples of three and are in the range of 1 to 500.

sum = 0
for i in range(1,501):
    if (i % 2 != 0 ) and (i % 3 == 0):
        sum += i
print(sum)