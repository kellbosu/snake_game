class Machine:
    def __init__(self):
        self.power = "off"
        self.material = "metal"

    def power_on(self):
        print("Powering up systems...")
        self.power = "on"
        if self.power == "on":
            print("Lights blinking. Engine rumbling.")
    
    def power_off(self):
        print("Shutting down...")
        self.power == "off"
        if self.power == "off":
            print("All dark. All quiet.")

class Plane(Machine):
    def __init__(self):
        super().__init__()

    def power_on(self):
        super().power_on()
        print("Prop spinning. Whoosha whoosha whoosha")

    def take_off(self):
        if self.power == "on":
            print("Wheels up. We have lift")
        else:
            print("Standing still...")
    
star_scream = Plane()

print(star_scream.power)
star_scream.power_on()