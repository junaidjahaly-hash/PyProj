class Vehicle():
    # this function runs each time we create/initialise an object
    def __init__(self,name):
        self.name = name
        self.speed = 0
        self.max_speed = 200
        self.fuel_level = 40
        self.number_of_tyres = 4

    def horn(self):
        return "Beep beep"
    
    def start(self):
        if(self.fuel_level <= 0):
            print("Unable to start vehicle")
        else:
            print("starting engine")

    def stop(self):
        print('stopping engine')
        self.speed = 0
        self.max_speed = 200
        self.fuel_level = 40
        self.number_of_tyres = 4

    def horn(self):
        return "Beep beep"
    
    def status(self):
        print(f"I am a vehicle {self.name} with {self.number_of_tyres} tyres going at {self.speed}")
    
    def start(self):
        if(self.fuel_level <= 0):
            print("unable to start engine")
        else:
            print("starting engine")

    def stop(self):
        print('stopping engine')

class FireTruck(Vehicle):
    def __init__(self, name):
        super().__init__(name) # runs the __init__ in Vehicle
        self.number_of_tyres = 6


class Ambulance(Vehicle):
    # siren: siren_status (ON/OFF) ; start_siren() ; stop_siren()
    pass

nayar_car = Vehicle("Nayar Car")
nayar_car.status()
truck_1 = FireTruck("Firetruck 1")
truck_1.status()