from random import randint

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

racing_cars = []

# main program 
def isRaceFinished(racing_cars):
    for car in racing_cars:
        if car.travelled_distance >= 10_000:
            print(f"We have a winner: {car.registration_number}\n")
            return True
    
    return False

for i in range(10):
    car = Car(f"ABC-{i + 1}", randint(100, 200))

    racing_cars.append(car)

print("The race is about to start:")
for car in racing_cars:
    print(vars(car))
print("\n")

race_time = 0

while not isRaceFinished(racing_cars):
    for car in racing_cars:
        speed_change = randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)
    
    race_time += 1
    print(f"The race has lasted for {race_time} hours.")

print("After the race:")
for car in racing_cars:
    print(vars(car))