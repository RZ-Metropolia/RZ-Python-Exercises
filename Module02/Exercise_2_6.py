from random import randrange

code_3_digit = f"{randrange(0,10)}{randrange(0,10)}{randrange(0,10)}"
code_4_digit = (f"{randrange(1, 7)}{randrange(1, 7)}"
                f"{randrange(1, 7)}{randrange(1, 7)}")
code_full = code_3_digit + code_4_digit

print("The 3-digit code is: " + code_3_digit)
print("The 4-digit code is: " + code_4_digit)
print("The full code is: " + code_full)