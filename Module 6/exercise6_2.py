from random import randrange

def roll_dice(sides):
    return randrange(1, sides + 1)

print("\nLet's roll a dice until we get the largest number!")
sides_number_0 = int(input("Enter the sides for the dice: "))
while True:
    number = roll_dice(sides_number_0)

    if number == sides_number_0:
        print(number)
        break
    else:
        print(number)