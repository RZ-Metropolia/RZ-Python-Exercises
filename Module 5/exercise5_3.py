number = int(input("Please enter an integer:\n"))
isPrime = None

if number < 2:
    isPrime = False
elif number == 2:
    isPrime = True
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break
        else:
            isPrime = True

if isPrime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")