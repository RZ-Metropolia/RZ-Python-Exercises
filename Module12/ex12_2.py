import requests

def print_weather_report(city_name):
    coordinates = return_city_coordinates(city_name)[:]

    lat = coordinates[0]
    lon = coordinates[1]
    request = (
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}"
        f"&appid=144b0766a19930e89c0d2d5977744a88&units=metric"
    )
    response = requests.get(request).json()

    weather = response["weather"][0]["main"]
    temperature = response["main"]["temp"]
    print(f"The weather of {city_name.title()} now is {weather}, and the temperature is {temperature}°C.")

def return_city_coordinates(city_name):
    coordinates = []

    request = (f"http://api.openweathermap.org/geo/1.0/direct?q={city_name.title()}"
               f"&appid=144b0766a19930e89c0d2d5977744a88"
    )
    response = requests.get(request).json()

    coordinates.append(response[0]["lat"])
    coordinates.append(response[0]["lon"])

    return coordinates

# main program
def main():
    try:
        city_name = input("Please enter the city name: ")
        print_weather_report(city_name)
    except IndexError:
        print("Invalid city name, please try again.")
        main()

if __name__ == "__main__":
    main()



