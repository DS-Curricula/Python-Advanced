#Example of procedural programming in Python
def calculate_area(length, width):
    return  length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3

area = calculate_area(length, width)
perimeter = calculate_perimeter(length,width)

print(f"Area: {area}") #Output: Area: 15
print(f"Perimeter: {perimeter}")  #Output: Perimeter: 16