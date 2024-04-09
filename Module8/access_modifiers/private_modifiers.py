# Define a class named MyClass.
class MyClass:
    # Define a constructor (__init__ method) for the class
    def __init__(self):
        # Initialize a private instance variable named private_variable and assign it a value.
        self.__private_variable = "This is a private variable"

    # Define a private method named private_method
    def __private_method(self):
        # Print a message indicating that this is a private method
        print("This is a private method")


# Create an instance of the MyClass class.
my_class = MyClass()

# Attempt to access the private_variable instance variable directly.
# This will raise an AttributeError because private variables are not directly accessible from outside the class.
print(my_class.__private_variable)

# Attempt to access the private_variable method directly.
# This will raise an AttributeError because private methods are not directly accessible from outside the class.
print(my_class.__private_method())
