import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

if __name__ == "__main__":
    wheeled = Vehicle(Wheels())
    tracked = Vehicle(Tracks())
    
    wheeled.turn(True)
    # wheels:  True True
    # wheels:  True False
    tracked.turn(False)
    # tracks:  False True
    # tracks:  False False