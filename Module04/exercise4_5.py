username_correct = "python"
password_correct = "rules"
attempt_times = 0

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

while username != username_correct and password != password_correct:
    attempt_times += 1
    if attempt_times == 5:
        break

    print("Wrong username or password! Please try again.")
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))

if attempt_times == 5:
    print("Access denied!\n")
else:
    print("Welcome!\n")