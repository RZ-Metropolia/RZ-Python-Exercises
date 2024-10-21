cities = []
amount = 5

for i in range(amount):
    city = input(f"Please enter the name of city{i+1}: ")
    cities.append(city)

print("\nThe five cities you have entered are:")
for city in cities:
    print(city.title())


