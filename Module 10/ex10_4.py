from random import randint

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance 
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)       

    def print_status(self):
        print("-" * 100)
        print("{:<20} {:<15} {:<15} {:<15}".format("Registration Number", "Maximum Speed", "Current Speed", "Travelled Distance"))
        for car in self.cars:
            print("{:<20} {:<15} {:<15} {:<15}".format(car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance))
        print("-" * 100 + "\n")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                print(f"\nWe have a winner: {car.registration_number}!")
                return True
        
        return False

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
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

# main program
cars = []
for i in range(10):
    car = Car(f"ABC-{i + 1}", randint(100, 200))
    
    cars.append(car)

race_0 = Race("Grand Demolition Derby", 8000, cars)

print(f"{race_0.name} is about to begin!")
race_0.print_status()

time_passed = 0 
while not race_0.race_finished():
    race_0.hour_passes()

    time_passed += 1
    if time_passed % 10 == 0:
        print(f"The race has lasted for {time_passed} hours!")
        race_0.print_status()

print("Final Result")
race_0.print_status()