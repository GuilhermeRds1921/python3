# Develop a program that reads the name, age and sex of 4 people. Show:
# The average age of the group
# how many women are under 20
# what's the name of the older man


count = 0
older = 0
new = 0
for i in range(0, 4):
    print('====== {} Candidate ======'.format(i + 1))
    name = str(input('Whats Your Name? '))
    age = int(input('How old are you? '))
    sex = str(input('Whats your sex type(men or womam)? '))
    count += age
    if sex == 'men':
        if age > older:
            older = age
            olmen = name
    elif sex == 'womam':
        if age < 20:
            new += 1
print('the average age of the group is {} '.format(count / 4))
print('The older mens age is {} and his name is {}'.format(older, olmen))
print('There are {} women younger than 20 '.format(new))


