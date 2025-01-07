# Create a program that reads how much money a person has in their wallet
# and displays how many dollars they can buy.

num = float(input("Enter how much money you have in Reais: "))

print("You could buy ${:.2f} dollars".format(num / 5))
