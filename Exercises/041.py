# The National Swimming Confederation needs a program that 
# reads the year of birth of an athlete and shows his Category, 
# according to age:
# - Up to 9 years old: Mirim
# - Up to 14 years old: Infantil
# - Up to 19 years: Junior
# - Up to 25 years old: Sênior
# - Up: Master


from datetime import date
date = date.today().year

birthday = int(input('When is you birthday? '))
age = date - int(birthday)
if age <= 9:
    print('You are Mirim ')
elif age > 9 and age <= 14:
    print('You are Infantil ')
elif age > 14 and age <= 19:
    print('You are Junior ')
elif age > 19 and age <= 25:
    print('You are Senior ')
else:
    print('You are Master')