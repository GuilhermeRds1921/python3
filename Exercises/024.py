# Create a program that reads the name of a city
# and checks if it starts with the name "Santo".

city_name = input("Enter the name of your city: ")
city_name = city_name.split()

print('Santo' in city_name[0])
