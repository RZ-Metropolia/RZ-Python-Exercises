def gallon_to_liter(gallon):
    return gallon * 3.785

prompt = "Please enter the quantity of gasoline in gallons: "
while True:
    gallon_0 = float(input(prompt))

    if gallon_0 < 0:
        break
    else:
        liter = gallon_to_liter(gallon_0)
        print(f"{gallon_0} gallon(s) is {liter:.2f} liter(s).")


