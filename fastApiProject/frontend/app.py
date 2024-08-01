import streamlit as st
import requests
from pydantic import BaseModel
import pandas as pd

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

st.title("FastAPI and Streamlit Integration")

# Input section
st.header("Add New Item")

name = st.text_input("Name")
description = st.text_area("Description")
price = st.number_input("Price", min_value=0.0, step=0.01)
tax = st.number_input("Tax", min_value=0.0, step=0.01)

if st.button("Create Item"):
    item = Item(name=name, description=description, price=price, tax=tax)
    response = requests.post("http://127.0.0.1:8000/items/", json=item.dict())
    if response.status_code == 200:
        st.success("Item created successfully!")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")

# Display section
st.header("Items List")

response = requests.get("http://127.0.0.1:8000/items/")
if response.status_code == 200:
    items = response.json()
    if items:
        # Convert the list of items to a DataFrame for better display
        df = pd.DataFrame(items)
        st.dataframe(df)
    else:
        st.write("No items available.")
else:
    st.error(f"Error: {response.status_code}")
