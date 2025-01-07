# Write a program that reads three numbers and shows which is the largest and which is the smallest.

num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))
num3 = float(input("Enter the Third Number: "))

# Sorting the numbers in ascending order
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2, num3 = num3, num2
if num1 < num2:
    num1, num2 = num2, num1

print(f"{num1} is the Largest")
print(f"{num2} is the Middle")
print(f"{num3} is the Smallest")
