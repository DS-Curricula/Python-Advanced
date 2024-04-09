# Function to add two numbers
def add(x, y):
    return x + y


# Function to concatenate two strings
def concatenate(x, y):
    return str(x) + str(y)


# Function to demonstrate polymorphism
def operate(operation, x, y):
    """
        Performs a specified operation on two operands.

        :param operation: The operation function to be performed (param1).
        :param x: The first operand (param2).
        :param y: The second operand (param3).
        :return: The result of the operation (returns).
        """
    return operation(x, y)


# Using the operate function with different operations
result_sum = operate(add, 3, 5)
result_concatenate = operate(concatenate, "Hello", "World")

print("Result of sum:", result_sum)  # Output: Result of sum: 8
print("Result of concatenation:", result_concatenate)  # Output: Result of concatenation: HelloWorld
