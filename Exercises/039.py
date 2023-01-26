# Make a program that reads the year of birth of a young person and informs,
# according to their age, if they are still going to join the military, 
# if is time to join or if past the time of enlistment.
# Your program should also show how much time is left or past the deadline.

year = int(input('Whats year were you born? '))
age = 2020 - int(year)
if age > 18:
    print('You already spent {} year of enlistment year '.format(age - 18))
elif age == 18:
    print('This is the enlistment year ')
else:
    print('You still have {} years to the enlistment year '.format(18 - age))