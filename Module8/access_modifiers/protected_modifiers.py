# Define a class named MyClass.
class MyClass:
    # Define a constructor (__init__ method) for the class
    def __init__(self):
        # Initialize a protected instance variable named protected_variable and assign it a value.
        self._protected_variable = "This is a protected variable"

    # Define a private method named protected_method
    def _protected_method(self):
        # Print a message indicating that this is a private method
        print("This is a protected method")


# Create an instance of the MyClass class.
my_class = MyClass()

# Access and print the value of the protected_variable instance variable.
print(my_class._protected_variable)

# Call the protected_method method.
my_class._protected_method()
