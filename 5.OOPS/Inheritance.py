
from myClass import Vehicle

# Inheritance
class Car(Vehicle):
    def __init__(self, make, model, isElectric):
        super().__init__(make, model)
        self.isElectric = isElectric

    def getDetails(self):
        print(f"{self.make} {self.model} is electric: {self.isElectric}")


car = Car("tata", "Punch", True)
car.getDetails();

