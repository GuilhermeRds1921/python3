# Develop a program that reads the length of three sides
# and tells the user if they can form a triangle.

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Sort the sides to simplify the logic
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

# Check if the sides can form a triangle
if a < b + c:
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")
