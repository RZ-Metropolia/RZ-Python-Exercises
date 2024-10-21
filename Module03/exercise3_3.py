biological_gender = str(input("Please enter your biological gender: "))

if biological_gender.lower() == "female":
    hemoglobin_value = float(input("Please enter your hemoglobin value(g/l): "))
    if hemoglobin_value < 117:
        print("Your hemoglobin value is low.")
    elif hemoglobin_value > 155:
        print("Your hemoglobin value is high.")
    elif 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Invalid hemoglobin value")
elif biological_gender.lower() == "male":
    hemoglobin_value = float(input("Please enter your hemoglobin value(g/l): "))
    if hemoglobin_value < 134:
        print("Your hemoglobin value is low.")
    elif hemoglobin_value > 167:
        print("Your hemoglobin value is high.")
    elif 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Invalid hemoglobin value")