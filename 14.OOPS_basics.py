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


# Inheritance
class Car(Vehicle):
    def __init__(self, make, model, isElectric):
        super().__init__(make, model)
        self.isElectric = isElectric

    def getDetails(self):
        print(f"{self.make} {self.model} is electric: {self.isElectric}")


car = Car("tata", "Punch", True)
car.getDetails();

