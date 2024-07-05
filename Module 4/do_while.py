# Do-While Loop

# Infinite loop
while True:
    # Prompt the user to enter a positive number
    user_input = input("Enter a positive number: ")

    # Check if the input is numeric
    if user_input.isnumeric():
        # Convert the input to an integer
        number = int(user_input)
        # Check if the number is positive
        if number > 0:
            # Break out of the loop if input is valid
            break

    # Print error message for invalid input
    print("Invalid input. Please try again.")

# Print the valid positive number entered by the user
print("You entered a valid positive number:", number)
