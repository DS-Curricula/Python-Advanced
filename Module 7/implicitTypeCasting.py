#Example 1

x = 32
y = 5.3

result = x + y
print(result, "of type", type(result)) #Output: 37.3 of type <class 'float'>


age = 25
message = "I am " + str(age) + " years old"
print(message) #Output: I am 25 years old.


a = 5
b = "3"
result1 = a * int(b)
print(result1, "of type", type(result1)) #Output: 15 of type <class 'int'>

#Raises a ValueError: Invalid literal for int() with base 10: 'abc'
# z = int("abc")

#ERROR HANDLING
#TRY AND EXCEPT BLOCK

try:
    #code that might raise an exception
    result = 10/0
except ZeroDivisionError:
    #Handle the specific exception
    print("Oops! Tried to devide by zero.")


#2
fruits = {
    "apple": 5,
    "banana": 7,
    "orange": 3
}

#Try to access a key ("cherry") that doesn't exist in the directory
try:
    print(fruits["cherry"])
#Handle the KEyError if it occurs
except KeyError:
    print("The key does not exist in the directory")


#3
text = "This is not a number"

#Try to convert the text to an integer
try:
    text_to_int = int(text)
#Catch any exception that occurs during the conversation
except Exception as e:
    #Print an error message along with the exception details
    print("An error occurred while parsing data: ", e) #Output: An error occurred while parsing data:
    #invalid literal for int() with base 10: 'This is not a number'



#4

try:
    result = 10/2
except ZeroDivisionError:
    #Except block catches a ZeroDivisionError if it occurs during division
    print("Division by zero error occurred")
else:
    #Else block catches if no exception occurred in the try block
    print("Division successful. Result:", result)


#5

try:
    #Code that  may raise an exception
    result = 10/0
except ZeroDivisionError:
    #Code to handle the exception
    print("Cannot divide by zero.")
finally:
    #Code that will always execute regardless of whether an exception occurred or not
    print("Finally block executed")
#Output:Cannot divide by zero. Finally block executed



#Exercise

def divide_numbers(a,b):
    try:
        result = a/b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Invalid division by zero.")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print(f"Unexpected error: {e}")

#Test cases
divide_numbers(10,2) #Output: Result of division: 5.0
divide_numbers(10,0) #Output: Invalid division by zero.
divide_numbers(10,'2') #Output: nvalid type for division