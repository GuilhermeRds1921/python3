# Create an algorithm that reads the price of a product and shows its
# new price with a 5% discount.

price = float(input("Enter the price of something: "))
discounted_price = float(price - (price * 0.05))

print("The price with a 5% discount is: {:.2f}".format(discounted_price))
