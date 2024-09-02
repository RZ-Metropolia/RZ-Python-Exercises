import random

amount_dices = int(input("Please enter the number of dices: "))
numbers = []

for i in range(amount_dices):
    numbers.append(random.randrange(1, 7))

print(f"The sum of the numbers is {sum(numbers)}.")