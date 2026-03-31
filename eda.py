import pandas as pd

df = pd.read_csv("train.csv")

print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
import matplotlib.pyplot as plt

# Graph 1: Sales Distribution
plt.figure()
plt.hist(df['Sales'], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Graph 2: Category Distribution
plt.figure()
df['Category'].value_counts().plot(kind='bar')
plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
import sqlite3
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
query = "SELECT * FROM sales LIMIT 5"
result = pd.read_sql(query, conn)
print(result)
query = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category
"""
result = pd.read_sql(query, conn)
print(result)
query = """
SELECT "Product Name", SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 5
"""
result = pd.read_sql(query, conn)
print(result)
query = """
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
"""
result = pd.read_sql(query, conn)
print(result)