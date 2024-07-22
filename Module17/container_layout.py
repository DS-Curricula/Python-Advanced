import streamlit as st

# Create a container to group related elements
with st.container():
    # Add a header inside the container
    st.header("This is a container")

    # Add some text content inside the container
    st.write("This is inside the container")

# Add some text content outside the container
st.write("This is outside the container")
