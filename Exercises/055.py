# Develop a program that reads the weight of five people. 
# Show which was the highest and lowest weight.

bigger = 0
smaller = 0
for i in range(0,5):
    num = float(input('Whats your weight? '))
    if num > bigger or i == 0:
        bigger = num
    if num < smaller or i == 0:
        smaller = num
print('{} is the heaviest. '.format(bigger))
print('{} is the lightest. '.format(smaller))