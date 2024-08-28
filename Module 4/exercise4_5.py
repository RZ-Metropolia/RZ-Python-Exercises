username_correct = "python"
password_correct = "rules"
attempt = 0

username = str(input("Enter your username: \n"))
password = str(input("Enter your password: \n"))

while username != username_correct and password != password_correct:
    attempt = attempt + 1
    if attempt == 5:
        break

    print("Wrong username or password! Please try again.\n")
    username = str(input("Enter your username: \n"))
    password = str(input("Enter your password: \n"))

if attempt == 5:
    print("Access denied!\n")
else:
    print("Welcome!\n")