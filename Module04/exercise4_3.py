numbers = []

while True:
    number = input("Please enter a number or press 'Enter' button to quit: ")

    if number == '':
        break

    numbers.append(float(number))

if len(numbers) == 0:
    print("You did not enter any number.")
else:
    print(f"The largest number you inputted is {max(numbers)}, and the smallest number you inputted is {min(numbers)}.")
