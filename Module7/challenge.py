def calculate(number1, number2, operator):
    """Performs the given arithmetic operation on two numbers."""
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        raise ValueError("Invalid operation")


try:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} is: {result}")

except ValueError as e:
    print(f"Invalid input: {e}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("End of the program.")
