import streamlit as st
import pandas as pd

file_path= "covid_dataset.csv"
df = pd.read_csv(file_path)

st.title("COVID-19 Data Visualizations")

st.write(df)

st.subheader("Visu")



