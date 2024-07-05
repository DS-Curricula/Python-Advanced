class MyClass:
    def __init__(self):
        #Initialize a private instance variable names __private_variable and assign it a value
        self.__private_variable = "This is a private variable"

    def __private_method(self):
        #Print a message indicating that this is a private method.
        print("This is a private method")

my_class = MyClass()

#Attempt to access the private_variables instance variable directly
#This will raise an AttributeError because private variables are not directly accessible from outside
#the class.
print(my_class.__private_variable)

#Attempt to call the private_method method directly.
#This will raise an AttributeError because private methods are not directly accessible from outside
#the class.
my_class.__private_method()

