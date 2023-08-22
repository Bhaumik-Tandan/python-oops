"""
Question 3: Polymorphism
Define a class Shape with a method area(). 
Create subclasses Circle, Rectangle, and Triangle, each with its specific implementation of the area() method. 
Demonstrate polymorphism by creating a list of different shapes and calling their area() methods in a loop.
"""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

triangle = Triangle(2, 6)
rectangle = Rectangle(2, 12)
circle = Circle(7)

shapes = [triangle, rectangle, circle]

for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area()}")