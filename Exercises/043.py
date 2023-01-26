# Develop a logic that reads a person's weight and height, 
# calculates their BMI and shows their status, according to the table below:
# - Under 18.5: Underweight                -25 to 30: Overweight
# - Between 18.5 and 25: Ideal weight      -30 to 40: Obesity
# - Over 40: Morbid Obesity

weight = float(input('Whats your weight? (kg)'))
height = float(input('How tall are you? (m)'))
imc = float(weight / (height ** 2 ))

print('The Imc is: {:.1f}'.format(imc))
if imc <= 18.5:
    print('You are underweight ')
elif imc > 18.5 and imc <= 25:
    print('Nice weight ')
elif imc > 25 and imc <= 30:
    print('You are above weight')
elif 30 < imc <= 40:
    print('Obesity')
else:
    print('Stop eating or you will die !')