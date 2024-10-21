from random import randrange

amount_dice = int(input("Please enter the amount of dice to roll: "))
numbers = []

for i in range(amount_dice):
    number = randrange(1, 7)
    numbers.append(number)

print(f"The sum of the numbers is {sum(numbers)}.")