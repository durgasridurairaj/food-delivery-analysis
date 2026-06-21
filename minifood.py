import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("fooditem.xlsx")

print("\n ==== DATA PREVIEW ====")
print(df.head())

print("\n ==== TOTAL FOOD ITEM ====")
print(len(df))

print("\n ==== HIGHEST FOOD PRICE ====")
print(df["Orders"].max())

print("\n ==== HIGHEST ORDER ITEM ====")
print(df.loc[df["Orders"].idxmax()])

# print(df.dtypes)
# print(df.columns)

print("\n ==== AVERAGE FOOD PRICE ====")
print(df["Price (₹)"].mean())

print("\n ==== HIGHEST PRICE FOODS ====")
print(df[df["Price (₹)"] > 150])

print("\ ==== CATEGORY-WISE ORDER ==== ")
print(df.groupby("Category")["Orders"].sum())

dept_count=df["Category"].value_counts()
dept_count.plot(kind="pie",autopct="%1.1f%%")
plt.title("Food item by Category")
plt.xlabel("Category")
plt.ylabel("")
plt.show()