import pandas as pd
import numpy as np

# ===============================Stock Function======================================
# Determining the status of stock
def Stock_Situation(df: pd.DataFrame) -> pd.DataFrame:
  # Create condition over Stock
  stock_Condition = [
    (df['Stock'] < 50),
    (df['Stock'] >= 50) & (df["Stock"] <= 500),
    (df['Stock'] > 500)
  ] 
  # Create choice over Stock which tells about the status on the basis of Stock Condition
  stock_tags = ['Critical (Reorder)', 'Healthy', 'Overstocked']

  # Finalise the Status
  df['Stock_Status'] = np.select(stock_Condition, stock_tags, default='Check')

  return df
