import pandas as pd
import streamlit as st

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
})

# Use st.write to display the DataFrame
st.write(df)
