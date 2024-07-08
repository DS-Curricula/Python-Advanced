# Local Variables
def greet(name):
    message = f"Hello, {name}"  # Creating a variable inside the function
    print(message)


greet("Alice")

# Trying to access the variable outside the function's scope
print(message)  # NameError: name 'message' is not defined
