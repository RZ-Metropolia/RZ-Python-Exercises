cities = []
amount = 5

for i in range(0, amount):
    city = input("Please enter a name of a city: ")
    cities.append(city)

print("\nThe five cities you have entered are:")
for city in cities:
    print(city)


