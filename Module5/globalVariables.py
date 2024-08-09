# Define a global variable "greeting"
greeting = "Hello"


# Define a function "greet" that takes a 'name' parameter
def greet(name):
    # Create a message using the global variable 'greeting' and the 'name' parameter
    message = f"{greeting}, {name}"
    print(message)


# Call the 'greet' function with the argument "Bob"
greet("Bob")

# Print the value of the global variable "greeting"
print(greeting)
