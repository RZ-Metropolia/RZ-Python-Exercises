talent_input = input("Enter talents:\n")
talent = float(talent_input)
pound_input = input("Enter pounds:\n")
pound = float(pound_input)
lot_input = input("Enter lots:\n")
lot = float(lot_input)

weight = talent * 20 * 32 * 13.3 + pound * 32 * 13.3 + lot * 13.3

print("The weight in modern units: ")
print(str(int(weight/1000)) + " kilograms and " +
      str(weight - int(weight/1000) * 1000) + " grams.")