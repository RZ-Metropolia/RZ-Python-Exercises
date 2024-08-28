numbers =[]
number = input("Enter a number or press the Enter button to quit: \n")


while number != "":
    numbers.append(float(number))
    number = input("Enter a number or press the Enter button to quit: \n")

print(f"The largest number you inputted is {max(numbers)}, and the smallest number you inputted is {min(numbers)}.")
