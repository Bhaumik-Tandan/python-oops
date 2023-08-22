"""
Question 4: Abstraction
Create an abstract class Animal with an abstract method speak(). 
Implement subclasses Dog, Cat, and Cow, overriding the speak() method to make appropriate sounds. 
Demonstrate abstract classes and methods.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self)->str:
        pass


class Dog(Animal):
    def speak(self):
        return "Bhow"
    
class Cat(Animal):
    def speak(self):
        return "Meaw"

class Cow(Animal):
    def speak(self):
        return "Moo"

animals=[Cow(),Dog(),Cat()]

for animal in animals:
    print(f"{type(animal).__name__} says {animal.speak()}")
