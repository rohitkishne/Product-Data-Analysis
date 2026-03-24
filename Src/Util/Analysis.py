import pandas as pd

# ==================================Analysis============================================
# Doing Analysis over Data on differenct Scenerio
def analyse_data(df: pd.DataFrame) -> pd.DataFrame:
  print("-----------------------Data Analysis Started------------------------\n")

  # Category Summary Analysis
  category_Summary = df.groupby('Category').agg({
    'Price' : 'mean',
    'Stock' : 'sum',
    'Discount_Rate' : 'mean'
  }).reset_index()

  # Stock Status Count
  Stock_Status_Count = df['Stock_Status'].value_counts()
  
  # High Discount Product
  High_Discount = df[df['Discount_Rate'] > 0.2][['Name', 'Category', 'Discount_Rate']] 

  print("------------------------Data Analysis Ended-------------------------\n")

  return {
    "Category_Summary" : category_Summary,
    "Stock_Status_Count" : Stock_Status_Count,
    "High_Discount_Product" : High_Discount
  }