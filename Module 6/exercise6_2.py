import random

def roll_dice(sides_number):
    return random.randrange(1, sides_number + 1)

print("\nLet's roll a dice until you get the largest number!")
sides_number_0 = int(input("How many sides of the dice do you want? "))
while True:
    number = roll_dice(sides_number_0)

    if number == sides_number_0:
        print(number)
        break
    else:
        print(number)
        roll_dice(sides_number_0)