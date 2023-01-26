# Develop a program that reads a person's gender, 
# but only accepts 'Mm' or 'Ff' values. 
# If it is wrong, ask for typing again until you have a correct value

sex = 's'
while sex != 'M' and sex != 'F':
    sex = str(input('Whats your gender? f or m: ')).upper()
    if sex not in 'FM':
        print('This isnt a valid answer. ')

if sex =='M':
    print('Your Gender is Male')
else:
    print('Your Gender is Female')