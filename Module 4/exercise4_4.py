from random import randrange

answer = randrange (1, 10)
guess = int(input("Please guess an integer number between 1 and 10:\n"))

while guess != answer:
    if guess > answer:
        print("Too high!\n")
        guess = int(input("Try again:\n"))
    elif guess < answer:
        print("Too low!\n")
        guess = int(input("Try again:\n"))
print("Correct!")