# ERROR HANDLING

# TRY AND EXCEPT BLOCK
try:
    # code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Oops! Tried to divide by zero.")

# Handling KeyError
fruits = {
    "apple": 5,
    "banana": 7,
    "orange": 3
}

# Try to access a key ("cherry") that doesn't exist in the directory
try:
    print(fruits["cherry"])
# Handle the KeyError if it occurs
except KeyError:
    print("The key does not exist in the directory")

# BaseException
text = "This is not a number"

# Try to convert the text to an integer
try:
    text_to_int = int(text)
# Catch any exception that occurs during the conversation
except Exception as e:
    # Print an error message along with the exception details
    print("An error occurred while parsing data: ", e)  # Output: An error occurred while parsing data:
    # invalid literal for int() with base 10: 'This is not a number'

# Else Block
try:
    result = 10 / 2
except ZeroDivisionError:
    # Except block catches a ZeroDivisionError if it occurs during division
    print("Division by zero error occurred")
else:
    # Else block catches if no exception occurred in the try block
    print("Division successful. Result:", result)

# Finally Block
try:
    # Code that  may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero.")
finally:
    # Code that will always execute regardless of whether an exception occurred or not
    print("Finally block executed")


# Output:Cannot divide by zero. Finally block executed


# Exercise
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Invalid division by zero.")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Test cases
divide_numbers(10, 2)  # Output: Result of division: 5.0
divide_numbers(10, 0)  # Output: Invalid division by zero.
divide_numbers(10, '2')  # Output: Invalid type for division
