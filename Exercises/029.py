# Write a program that reads the speed of a car.
# If it exceeds 80Km/h, display a message saying the car was fined.
# The fine will cost R$7.00 for each Km above the limit.

speed = float(input("Enter the car's speed: "))

if speed <= 80:
    print("You are within the speed limit.")
else:
    fine = (speed - 80) * 7
    print("You are over the speed limit!")
    print(f"You will have to pay a fine of R${fine:.2f}.")
