import numpy as np
import pandas as pd

# ===============================Discount Function=================================
# Function to identify discount on the basis of Categories and Stock
def getDiscount(df: pd.DataFrame, map_df: pd.DataFrame) -> pd.DataFrame:
  # Default Discount keeps as 0%
  default_discount = 0.0
  
  # Merge Mapping 
  df = df.merge(map_df, on='Category', how="left")

  # Apply Dynamic Condition - we are doing mapping here with discount Mapping file
  df['Discount_Rate'] = np.where(
    (df['Stock'] > df['Min_Stock']),
    df['Discount_Rate'],
    default_discount
  )

  # Handle NaN Values where there is no condition applied
  df['Discount_Rate'] = df['Discount_Rate'].fillna(default_discount)

  # Final Price Calculation after giving discount
  df['Discounted_Price'] = df['Price'] * (1 - df['Discount_Rate'])

  return df