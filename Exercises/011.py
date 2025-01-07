# Create a program that reads the width and height of a wall in
# meters, calculates its area, and the amount of paint needed to
# cover it, knowing that each liter of paint covers an area of 2m².

height = float(input("Enter the height of the wall in meters: "))
width = float(input("Enter the width of the wall in meters: "))
area = float(height * width)

print("You will need {} liters of paint".format(area / 2))
