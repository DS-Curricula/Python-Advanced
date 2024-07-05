# Define the Student class
class Student:
    def __init__(self, name, age):
        # Initialize private attributes
        self.__name = name
        self.__age = age

    #Getter method for name
    def get_name(self):
        return self.__name

    #Setter method for name
    def set_name(self, name):
        self.__name = name


    #Getter method for age
    def get_age(self):
        return self.__age

    #Setter method for age
    def set_age(self, age):
        self.__age = age

#Creating am Instance of Student
student1 = Student("Alice", 17)

#Using getter and setter methods
print("Name:", student1.get_name()) #Output: Name: Alice
student1.set_name("Bob")
print("Updated Name", student1.get_name()) #Output: Updated Name: Bob

print("Age:", student1.get_age()) #Output: Age: 17
student1.set_age(18)
print("Updates Age:", student1.get_age()) #Output: Updated Age: 18
