from random import randrange

def roll_dice():
    return randrange(1, 7)

print("\nLet's roll a dice until we get a 6!")
while True:
    number = roll_dice()

    if number == 6:
        print(number)
        break
    else:
        print(number)