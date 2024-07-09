import streamlit as st


# Define a function named 'calculate' that takes three parameters: num1, num2, and operation
def calculate(num1, num2, operation):
    # Check if the operation is "Addition"
    if operation == "Addition":
        # Perform addition and store the result
        result = num1 + num2
    # Check if the operation is "Subtraction"
    elif operation == "Subtraction":
        # Perform subtraction and store the result
        result = num1 - num2
    # Check if the operation is "Multiplication"
    elif operation == "Multiplication":
        # Perform multiplication and store the result
        result = num1 * num2
    # Check if the operation is "Division"
    elif operation == "Division":
        try:
            # Perform division and store the result
            result = num1 / num2
        except ZeroDivisionError:
            # Handle division by zero error
            result = "Cannot divide by zero"
    # Return the result of the operation
    return result


def main():
    # Set the title of the Streamlit app
    st.title("Simple Calculator")

    # Get user input for the first whole number using a number input widget with step of 1
    num1 = st.number_input("Enter the first number", step=1)

    # Get user input for the second whole number using a number input widget with step of 1
    num2 = st.number_input("Enter the second number", step=1)

    # Provide radio buttons for the user to select the operation (Addition, Subtraction, Multiplication, Division)
    operation = st.radio("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Calculate the result based on the selected operation and input numbers
    result = calculate(num1, num2, operation)

    # Display the result of the calculation
    st.write(f"Result of the {operation} of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
