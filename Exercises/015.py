# Write a program that asks for the number of km
# driven by a rented car and the number of days it was rented.
# Calculate the price to pay, knowing that the car costs R$60 per day
# and R$0.15 per km driven.

km = float(input("How many km did you drive?: "))
days = int(input("How many days was it rented?: "))

print("The amount to be paid is: R${:.2f}".format(km * 0.15 + days * 60))
