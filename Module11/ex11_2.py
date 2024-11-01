from random import randint

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, travelled_time):
        self.travelled_distance += travelled_time * self.current_speed

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed, current_speed, travelled_distance)
        self.battery = battery

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed, current_speed, travelled_distance)
        self.tank_volume = tank_volume

# main program
electric_car_0 = ElectricCar("ABC-15", 180, 52.5, 50)
gasoline_car_0 = GasolineCar("ACD-123", 165, 32.3, 80)

for i in range(3):
    electric_car_0.accelerate(randint(-180, 180))
    gasoline_car_0.accelerate(randint(-165, 165))

    electric_car_0.drive(1)
    gasoline_car_0.drive(1)
    print("One hour has passed, the current speed of two cars are: ")
    print(f"{electric_car_0.registration_number}: {electric_car_0.current_speed} km/h")
    print(f"{gasoline_car_0.registration_number}: {gasoline_car_0.current_speed} km/h")
    print("Current kilometer counter of two cars are: ")
    print(f"{electric_car_0.registration_number}: {electric_car_0.travelled_distance} km")
    print(f"{gasoline_car_0.registration_number}: {gasoline_car_0.travelled_distance} km\n")


print("After three hours:")
print(f"The kilometer counter of {electric_car_0.registration_number} is {electric_car_0.travelled_distance}.")
print(f"The kilometer counter of {gasoline_car_0.registration_number} is {gasoline_car_0.travelled_distance}.")
