import math


class Shape:
    #  Method to calculate the area of the shape.
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    #  Method overriding to calculate the area of a circle.
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method overriding to calculate the area of a rectangle.
    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # Method overriding to calculate the area of a triangle.
    def area(self):
        return 0.5 * self.base * self.height


# Create instances of each subclass
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculate and print the area of each shape
print("Area of the circle:", circle.area())  # Output: 78.53981633974483
print("Area of the rectangle:", rectangle.area())  # Output: 24
print("Area of the triangle:", triangle.area())  # Output: 12.0
