print("Please enter three integers: ")
num1_input = input()
num2_input = input()
num3_input = input()

num1 = int(num1_input)
num2 = int(num2_input)
num3 = int(num3_input)

numbers_sum = num1 + num2 + num3
numbers_average = numbers_sum / 3

print("The sum of the three integers is: " + str(numbers_sum))
print("The average of the three integers is: " + str(numbers_average))