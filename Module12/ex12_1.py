import requests

def print_random_joke():
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    joke = response["value"]
    print(joke)

# main program
while True:
    print("This is a Chuck Norris joke:")
    print_random_joke()

    user_input = input("Do you want to hear another one? (y/n): ")
    while user_input.lower() != 'y' and user_input.lower() != 'n':
        user_input = input("Invalid input, please try again: ")
    if user_input.lower() == 'n':
        break
    elif user_input.lower() == 'y':
        continue