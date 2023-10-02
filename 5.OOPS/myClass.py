class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def getDetails(self):
        print("model :", self.model)
        print("Make :", self.make)

    def startEngine(self):
        print(f"{self.make} {self.model}'s engine is running.")


veh = Vehicle("Toyota", "Camry")
veh.startEngine()