# Define the base class DigitalSchool
class DigitalSchool:
    def __init__(self, name, city, state, courses):
        # Initialize common attributes for all digital schools
        self.__name = name  # Private attribute
        self.__city = city  # Private attribute
        self.__state = state  # Private attribute
        self.__courses = courses  # Private attribute

    @property
    def name(self):
        # Getter for the name attribute
        return self.__name

    @name.setter
    def name(self, value):
        # Setter for the name attribute
        self.__name = value

    @property
    def city(self):
        # Getter for the city attribute
        return self.__city

    @city.setter
    def city(self, value):
        # Setter for the city attribute
        self.__city = value

    @property
    def state(self):
        # Getter for the state attribute
        return self.__state

    @state.setter
    def state(self, value):
        # Setter for the state attribute
        self.__state = value

    @property
    def courses(self):
        # Getter for the courses attribute
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Setter for the courses attribute
        self.__courses = value

    def show_school_info(self):
        # Public method to display school information
        return {
            "name": self.__name,
            "city": self.__city,
            "state": self.__state,
            "courses": self.__courses,
        }

    def organize_hackathon(self):
        # Default implementation of organize_hackathon
        print("Organizing a generic hackathon.")


# Define the subclass DS_Prishtina, inheriting from DigitalSchool
class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        # Call the superclass constructor to initialize common attributes
        super().__init__(name, city, state, courses)
        self.__student_number = student_number  # Private attribute

    @property
    def student_number(self):
        # Getter for the student_number attribute
        return self.__student_number

    @student_number.setter
    def student_number(self, value):
        # Setter for the student_number attribute
        self.__student_number = value

    def SCF(self):
        # Method specific to DS_Prishtina
        print("First edition")

    def organize_hackathon(self):
        # Override the method to organize a specific hackathon for DS_Prishtina
        print("Data Analysis Hackathon")


# Define the subclass DS_Ferizaj, inheriting from DigitalSchool
class DS_Ferizaj(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        # Call the superclass constructor to initialize common attributes
        super().__init__(name, city, state, courses)
        self.__student_number = student_number  # Private attribute

    @property
    def student_number(self):
        # Getter for the student_number attribute
        return self.__student_number

    @student_number.setter
    def student_number(self, value):
        # Setter for the student_number attribute
        self.__student_number = value

    def Internship(self):
        # Method specific to DS_Ferizaj
        print("Internship in Starlabs")

    def organize_hackathon(self):
        # Override the method to organize a specific hackathon for DS_Ferizaj
        print("Scratch Hackathon")


# Example usage:
# Create an instance of DS_Ferizaj
ferizaj_obj = DS_Ferizaj("Digital School Ferizaj", "Ferizaj", "Kosovo",
                         ["Code", "Scratch", "App Inv"], 123)
# Call the Internship method of DS_Ferizaj
ferizaj_obj.Internship()  # Output: Internship in Starlabs
# Call the organize_hackathon method of DS_Ferizaj
ferizaj_obj.organize_hackathon()  # Output: Scratch Hackathon
# Access attributes using property methods
print(ferizaj_obj.name)  # Output: Digital School Ferizaj


# Create an instance of DS_Prishtina
prishtine_obj = DS_Prishtina("Digital School Prishtina", "Prishtina", "Kosovo",
                             ["Python", "PHP", "Javascript"], 200)
# Call the SCF method of DS_Prishtina
prishtine_obj.SCF()  # Output: First Edition
# Call the organize_hackathon method of DS_Prishtina
prishtine_obj.organize_hackathon()  # Output: Data Analysis Hackathon
# Access attributes using property methods
print(prishtine_obj.student_number)  # Output: 200

