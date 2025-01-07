# Develop a program that asks for the distance of a trip in Km.
# Calculate the ticket price, charging R$0.50 per Km for trips up to 200Km
# and R$0.45 for longer trips.

distance = float(input("Enter the distance of the trip in Km: "))

if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45

print(f"The ticket will cost R${price:.2f}")
