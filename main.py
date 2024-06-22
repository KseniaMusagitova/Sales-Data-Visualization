import matplotlib.pyplot as plt
import pandas as pd
# Load data from local file
data = pd.read_csv('sales.csv')

# Line plot - Revenue over years for each product
plt.figure(figsize=(12, 6))
for product in data['Product'].unique():
    product_data = data[data['Product'] == product]
    plt.plot(product_data['Year'], product_data['Revenue'], label=product)
plt.title('Revenue Over Years for Each Product')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart - Total units sold for each product
total_units_sold = data.groupby('Product')['Units Sold'].sum()
plt.figure(figsize=(12, 6))
total_units_sold.plot(kind='bar', color=['blue', 'green', 'red'], alpha=0.7)
plt.title('Total Units Sold for Each Product')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.grid(True)
plt.show()

# Scatter plot - Revenue vs Units Sold
plt.figure(figsize=(12, 6))
plt.scatter(data['Units Sold'], data['Revenue'], c='purple', alpha=0.5)
plt.title('Revenue vs Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# Line plot - Total revenue over years
total_revenue = data.groupby('Year')['Revenue'].sum()
plt.figure(figsize=(12, 6))
total_revenue.plot(kind='line', color='orange')
plt.title('Total Revenue Over Years')
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()
