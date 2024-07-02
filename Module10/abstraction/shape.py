# Import the ABC class and the abstractmethod decorator from the abc module
from abc import ABC, abstractmethod


# Define a new class named 'Shape' that inherits from 'ABC'
class Shape(ABC):
    # Use the @abstractmethod decorator to declare 'area' as an abstract method
    # An abstract method is a method that is declared, but contains no implementation
    @abstractmethod
    def area(self):
        pass


# Define a new class named 'Circle' that inherits from 'Shape'
class Circle(Shape):
    # Constructor method to initialize the 'radius' attribute
    def __init__(self, radius):
        self.radius = radius

    # Implement the abstract 'area' method for the 'Circle' class
    def area(self):
        return 3.14 * self.radius * self.radius  # Calculate and return the area of the circle


# Define a new class named 'Square' that inherits from 'Shape'
class Square(Shape):
    # Constructor method to initialize the 'length' attribute
    def __init__(self, length):
        self.length = length

    # Implement the abstract 'area' method for the 'Square' class
    def area(self):
        return self.length * self.length  # Calculate and return the area of the square


# Create an instance of the 'Circle' class with a radius of 7
circle_1 = Circle(7)
# Create an instance of the 'Square' class with a length of 10
square_1 = Square(10)

print(circle_1.area())
print(square_1.area())
