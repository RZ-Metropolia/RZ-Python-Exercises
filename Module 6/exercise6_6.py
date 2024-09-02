from math import pi

def pizza_unit_price(diameter, price):
    area = (diameter/2)**2 * pi
    return price / area

diameter_1 = float(input("Please enter the diameter of the first pizza: "))
price_1 = float(input("Please enter the price of the first pizza: "))
diameter_2 = float(input("Please enter the diameter of the second pizza: "))
price_2 = float(input("Please enter the price of the second pizza: "))

price_unit_1 = pizza_unit_price(diameter_1, price_1)
price_unit_2 = pizza_unit_price(diameter_2, price_2)

print(f"\nThe unit price of the first pizza per square meter is {price_unit_1}")
print(f"The unit price of the second pizza per square meter is {price_unit_2}")
if price_unit_1 < price_unit_2:
    print("The first pizza provides better value for money.")
elif price_unit_2 < price_unit_1:
    print("The second pizza provides better value for money.")
elif price_unit_1 == price_unit_2:
    print("The two pizzas provide same value for money.")