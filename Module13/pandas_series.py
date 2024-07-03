import pandas as pd

# List of products
products = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pineapples']

# Corresponding sales numbers
sales = [150, 200, 180, 90, 60]

# Creating a pandas Series from the sales data
sales_series = pd.Series(sales, index=products)

print(sales_series)

# Accessing sales for Grapes
print(sales_series['Grapes'])  # Output: 90

# Finding the total number of sales
total_sales = sales_series.sum()
print(total_sales)  # Output: 680

# Finding the product with the highest sales
best_selling_product = sales_series.idxmax()
print(f"Best selling product: {best_selling_product}")  # Output: Best selling product: Bananas
