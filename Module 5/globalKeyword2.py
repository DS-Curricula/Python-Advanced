#Define a global variable "greeting"
greeting = "Hello"
name= "Bob"

#Define a function 'greet' that takes a 'name' parameter
def greet():
    #Accessing and modifying the global variable greeting
    global greeting
    greeting = "Goodbye"
    #Creating a local variable 'name'
    name = "Alice"
    #Creating a message using the global variable "greeting" and the 'name' parameter
    message = f"{greeting},{name}!"
    print(message)

greet()

#The value of the global variable greeting will now be "Goodbye"
print(greeting) #Output: Goodbye

#The value of the global variable will remain the same: "Bob"
print(name) #Output: Bob