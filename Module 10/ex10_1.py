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

# main program
elevator_h = Elevator(1, 35)
elevator_h.go_to_floor(15)
elevator_h.go_to_floor(elevator_h.bottom_floor)

