# Define the Student class
class Student:
    def __init__(self, name, age):
        # Initialize private attributes
        self.__name = name
        self.__age = age

    #Getter method for name property
    @property
    def name(self):
        #Return the value of the private attribute __name
        return self.__name

    #Setter method for name property
    @name.setter
    def name(self, name):
        # Set the value of the private attribute __name
        self.__name = name



    #Getter method for age property
    @property
    def age(self):
        # Return the value of the private attribute __age
        return self.__age


    #Setter method for age property
    @age.setter
    def age(self, age):
        self.__age = age

#Creating am Instance of Student
student1 = Student("Alice", 17)

#Accessing attributes using properties
print("Name:",student1.name) #Output: Name: Alice
print("Age:", student1.age) #Output: Age: 17

#Modifying attributes using properties
student1.name = "Bob"
student1.age = 18

#Accessing modified attributes
print("Updated Name:", student1.name) #Output: Updated Name: Bob
print("Updated Age:", student1.age) #Output: Updated Age: 18
