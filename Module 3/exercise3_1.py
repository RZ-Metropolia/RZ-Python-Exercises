zander_length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42

if zander_length < size_limit:
    print("\nPlease release the fish back in to the lake.")
    print(f"Cause the fish is {size_limit - zander_length} centimeters below the size limit(45cm).")
else:
    print("Valid fish")