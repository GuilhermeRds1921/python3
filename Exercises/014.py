# Write a program that converts a temperature
# entered in ºC to ºF.

temp = float(input("Enter the temperature in ºC: "))
f = float((temp * 9 / 5) + 32)

print("The temperature {}ºC is equal to {}ºF".format(temp, f))
