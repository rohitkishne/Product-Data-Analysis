import matplotlib.pyplot as plt
import pandas as pd
# =====================================Visualization=========================================
# Create Charts and Graphs
def Visualize_Data(df: pd.DataFrame) -> pd.DataFrame:
  print("------------------------Visualization Started-------------------------\n")

  # 1. Stock Status Distribution
  df['Stock_Status'].value_counts().plot(kind="bar")
  plt.title("Stock Status Distribution")
  plt.xlabel("Stock Status")
  plt.ylabel("Count")
  plt.show()

  # 2. Average Price by Category
  category_summary = df.groupby('Category')['Price'].mean()
  category_summary.plot(kind="bar")
  plt.title("Average Price by Category")
  plt.show()

  # 3. Discount Distribution
  plt.hist(df['Discount_Rate'], bins=10)
  plt.title("Discount Distribution")
  plt.xlabel('Discount Rate')
  plt.ylabel('Frequency')
  plt.show()

  # 4. Price vs Discount
  plt.scatter(df['Price'], df['Discount_Rate'])
  plt.title("Price vs Discount")
  plt.xlabel("Price")
  plt.ylabel("Discount Rate")
  plt.show()

  # 5. Stock vs Discount
  plt.scatter(df['Stock'], df['Discount_Rate'])
  plt.title("Stock vs Discount")
  plt.xlabel("Stock")
  plt.ylabel("Discount Rate")
  plt.show()

  # 6. Top 10 Expensive Products
  top10 = df.sort_values(by='Price', ascending=False).head(10)
  plt.barh(top10['Name'], top10['Price'])
  plt.title("Top 10 Expensive Products")
  plt.xlabel("Price")
  plt.gca().invert_yaxis()
  plt.show() 

  print("-----------------------Visualization Completed--------------------------\n")
