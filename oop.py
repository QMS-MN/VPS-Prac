class Microwave:
    def __init__(self,brand,power_rating):
        self.brand = brand
        self.power_rating  = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> none:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on")

    def turn_off(self) -> none:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off")
        else:
            print(f"Microwave ({self.brand}) is already turned off")               

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Microwave running past ({seconds})")
        else:
            print("Turn on your microwave.....")    
smeg = Microwave('smeg','10')
smeg.turn_on()
smeg.run('10')
smeg.turn_off()