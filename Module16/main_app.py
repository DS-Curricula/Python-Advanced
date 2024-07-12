import streamlit as st

# Creating a button with the label "Click Me"
if st.button("Click Me"):
    # If the button is clicked, display the text "Button Clicked!"
    st.write("Button Clicked!")

# Creating a checkbox with the label "Check me to show some text"
if st.checkbox("Check me to show some text"):
    # If the checkbox is checked, display the text "You're seeing this text because you checked the checkbox"
    st.write("You're seeing this text because you checked the checkbox")


# Create a text input widget with a default value of "Sample text"
user_input = st.text_input("Enter text", "Sample text")

# Display the text entered by the user
st.write("You entered:", user_input)

# Creating a number input widget for the user to enter their age.
# 'min_value' sets the minimum allowed value to 0.
# 'max_value' sets the maximum allowed value to 100.
age = st.number_input("Enter your age", min_value=0, max_value=100)

# Display the entered age using the st.write function.
st.write(f"Your age is: {age}")

# Creating a text are widget for the user to enter a message
message = st.text_area("Enter a message")

# Display the entered message to the user using the st.write() function
st.write(f"Your message: {message}")

# Creating a list of radio buttons
choice = st.radio("Pick one", ["Choice 1", "Choice 2", "Choice 3"])

# Displaying the chosen option to the user.
st.write(f"You chose: {choice}")

# Create a button widget labeled "Success"
if st.button("Success"):
    # Display a success message indicating that the operation was successful
    st.success("Operation was successful")


# Simulate an exception and display it
try:
    # Attempt to divide by zero, which will raise an exception
    1 / 0
except Exception as e:
    # Catch the exception and display it using st.exception()
    st.exception(e)
