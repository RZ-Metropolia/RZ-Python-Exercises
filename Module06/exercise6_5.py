def remove_odd_number(numbers):
    numbers_return = []

    for number in numbers:
        if number % 2 == 0:
            numbers_return.append(number)

    return numbers_return

numbers_0 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
numbers_odd_removed = remove_odd_number(numbers_0)

print(f"I have a list of numbers: {numbers_0}")
print(f"This is a list with all non-even numbers removed: {numbers_odd_removed}")