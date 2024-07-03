import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read_csv('avgIQpercountry.csv')

# Printing information about the DataFrame
print(df.info())

# Using the head function
print(df.head())  # Displays the first 5 rows
print(df.head(10))  # Displays the first 10 rows

# Using the tail function
print(df.tail())  # Displays the last 5 rows
print(df.tail(10))  # Displays the last 10 rows
