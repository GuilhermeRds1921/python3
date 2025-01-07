# Create a program that reads a number from 0 to 9999
# and displays each of its digits separately.

num = int(input("Enter a number from 0 to 9999: "))

unit = int((num / 1) % 10)
ten = int((num / 10) % 10)
hundred = int((num / 100) % 10)
thousand = int((num / 1000) % 10)

print('Unit: {}'.format(unit))
print('Ten: {}'.format(ten))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))
