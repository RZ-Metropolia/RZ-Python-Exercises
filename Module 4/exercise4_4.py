from random import randrange

answer = randrange(1, 11)
guess = int(input("Please guess an integer number between 1 and 10: "))

while guess != answer:
    if guess > answer:
        print("Too high!")
        guess = int(input("Try again: "))
    elif guess < answer:
        print("Too low!")
        guess = int(input("Try again: "))
print("Correct!")