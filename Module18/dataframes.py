import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

# Create a sample DataFrame using a dictionary
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

# Display the DataFrame in the Streamlit app as an interactive table
st.dataframe(data)
