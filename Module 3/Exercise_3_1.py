zander_length = float(input("Enter the length of the zander in centimeters:\n"))

size_limit = 42
if zander_length < size_limit:
    print("Please release the fish back in to the lake.")
    print("Cause the fish is", size_limit - zander_length, "centimeters below the size limit")
else:
    print("Valid fish")

