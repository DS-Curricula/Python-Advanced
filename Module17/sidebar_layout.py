import streamlit as st

# Add a header to the sidebar
st.sidebar.header("Sidebar")

# Add some text content to the sidebar
st.sidebar.write("This is the sidebar.")

# Add a selectbox widget to the sidebar for choosing an option from a dropdown
st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])

# Add a radio button widget to the sidebar for navigating between different sections
st.sidebar.radio("Go to", ["Home", "Data", "Settings"])
