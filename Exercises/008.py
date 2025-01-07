# Write a program that reads a value in meters and displays it converted into centimeters
# and millimeters.

num = float(input("Enter the measurement in Meters: "))
cent = float(num * 100)
mili = float(num * 1000)

print("Centimeters: {}\nMillimeters: {}".format(cent, mili))
