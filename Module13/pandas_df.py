import pandas as pd

# Defining a dictionary 'data' containing information about individuals
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

# Creating a pandas DataFrame 'df' from the dictionary 'data'
df = pd.DataFrame(data)
print(df)
