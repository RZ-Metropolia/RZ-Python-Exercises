prompt = "\nPlease enter a number: "
prompt += "(Press 'enter' button to quit)\n"

numbers = []
number = input(prompt)
while number != '':
    number = float(number)
    numbers.append(number)
    number = input(prompt)

if len(numbers) == 0:
    print("You did not enter any number.")
else:
    numbers_sorted = sorted(numbers, reverse=True)
    print(f"The five greatest numbers in descending order are: {numbers_sorted[:5]}")

