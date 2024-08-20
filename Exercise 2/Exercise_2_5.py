talent_input = input("Enter talents:\n")
talent = float(talent_input)
pound_input = input("Enter pounds:\n")
pound = float(pound_input)
lot_input = input("Enter lots:\n")
lot = float(lot_input)

weight = talent * 20 * 32 * 13.3 + pound * 32 * 13.3 + lot * 13.3
weight_kilogram = int(weight / 1000)
weight_gram = weight - weight_kilogram * 1000

print("The weight in modern units: ")
print(f'{weight_kilogram} kilograms and {weight_gram:.2f} grams')