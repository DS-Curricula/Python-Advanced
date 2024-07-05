class Student:
    school_name = "Digital School" # This is a class variable

    def __init__(self, name, age, course):
        # Initialize instance variables (attributes) for name, age and course
        self.name = name
        self.age = age
0        self.course = course


#Create two instances of the Student class, providing values for the constructor parameteres
student_1 = Student("Alice", 15, "Python")
student_2 = Student("Bob", 16, "Javascript")

#Access and print the value of the course attribute for each student
print(student_1.course) #Output: Python
print(student_2.course) #Output:  Javascript
