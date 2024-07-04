#Example of Object_Oriented Programmming (OOP) in Python

class Rectangle:
    def __init__(self, length, width):
        #Initialialize the Rectangle object with given length and width
        self.length = length
        self.width = width


    def calculate_area(self):
        return self.length * self.width


    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


#Create an instance of Rectangle with length 2 and width 5
my_rectangle = Rectangle(2,5)

#Calculate the area and perimeter of the rectangle
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}") #Output: Area: 10
print(f"Perimeter: {perimeter}") #Output: Perimeter: 14