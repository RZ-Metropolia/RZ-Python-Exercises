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

new_car = Car("ABC-123", 142, 60, 2000)

new_car.drive(1.5)

print(f"The car has travelled {new_car.travelled_distance} km in total.")