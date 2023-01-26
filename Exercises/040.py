# Create a program that reads two notes from a student 
# and calculates their average, showing a message at the end, 
# according to the average achieved: 
# - Average of 5.0: RECOVERED
# - Average between 5.0 and 6.9: RECOVERY 
# - Average 7.0 or higher: APPROVED


num1 = float(input('Write the First Grade: '))
num2 = float(input('Write the Second Grade: '))
average = float(num1 + num2) / 2
if average < 5:
    print('You Fail ')
elif average > 5 and average < 7:
    print('You are in Recovery')
else:
    print('Congratulations! You Passed')