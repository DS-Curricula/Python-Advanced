# Define a global variable 'greeting'
greeting = "Hello"


# Define a function 'greet' that takes a 'name' parameter
def greet(name):
    # Declare 'message' as a global variable
    global message
    # Create a message using the global variable 'greeting' and the 'name' parameter
    message = f"{greeting},{name}!"
    print(message)


greet("Bob")  # Output: Hello, Bob!
print(message)  # Output: Hello, Bob!

# Accessing and modifying the global variable 'message'
message = f"{greeting}, student!"
print(message)  # Output: Hello, student!
