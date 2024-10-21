length_input = input("Enter the length of the rectangle:\n")
length = float(length_input)
width_input = input("Enter the width of the rectangle:\n")
width = float(width_input)

perimeter = 2 * (length + width)
area = length * width

print("The perimeter of the rectangle is " + str(perimeter))
print("The area of the rectangle is " + str(area))