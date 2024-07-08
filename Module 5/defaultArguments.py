# Define a function 'greet_person' with two parameters: 'name' and 'greeting'
# Where 'greeting' has a default value of "Hello"

def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message


# Call the "greet_person" function with the only the 'name' parameter provided using the default greeting
default_greeting = greet_person("Alice")

# Call the "greet_person" function with both 'name' and 'greeting' parameters provided
custom_greeting = greet_person("Bob", "Hi")

print(default_greeting)
print(custom_greeting)
