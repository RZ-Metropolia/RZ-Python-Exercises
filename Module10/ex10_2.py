class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    
    def go_to_floor(self, target_floor):
        if self.current_floor < target_floor:
            while self.current_floor != target_floor:
                self.floor_up()
                print(f"Going up")
                print(self.current_floor)
        elif self.current_floor > target_floor:
            while self.current_floor != target_floor:
                self.floor_down()
                print(f"Going down")
                print(self.current_floor)
        
        print(f"We have arrived at floor {target_floor}!\n")

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_amounts):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(elevator_amounts):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
    
    def run_elevator(self, elevator_number, target_floor):
        print(f"-Elevator {elevator_number}-")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target_floor)

# main program
building_0 = Building(1, 15, 2)
building_0.run_elevator(1, 10)
building_0.run_elevator(2, 8)
