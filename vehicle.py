"""
Question 2: Inheritance
Design a class Vehicle with attributes make, model, and methods start_engine() and stop_engine(). 
Create two subclasses Car and Motorcycle inheriting from Vehicle. 
Each subclass should have a unique method, such as drift() for Car and wheelie() for Motorcycle.
"""

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__engine_running = False

    def start_engine(self):
        if not self.__engine_running:
            self.__engine_running = True
            print(f"The {self.make} {self.model}'s engine is now running.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.__engine_running:
            self.__engine_running = False
            print(f"The {self.make} {self.model}'s engine has been stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already stopped.")

class Car(Vehicle):
    def drift(self):
        if self._Vehicle__engine_running:
            print(f"The {self.make} {self.model} is drifting!")
        else:
            print("Start the engine first to drift.")

class Motorcycle(Vehicle):
    def wheelie(self):
        if self._Vehicle__engine_running:
            print(f"The {self.make} {self.model} is doing a wheelie!")
        else:
            print("Start the engine first to do a wheelie.")

car = Car("Toyota", "Supra")
motorcycle = Motorcycle("Harley-Davidson", "Sportster")

car.start_engine()
motorcycle.start_engine()

car.drift()
motorcycle.wheelie()

car.stop_engine()
motorcycle.stop_engine()
