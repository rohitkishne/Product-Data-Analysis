import pandas as pd
import numpy as np


# ===============================Cleaning Function===============================
# Cleaning the File
def File_Cleaning(df: pd.DataFrame) -> pd.DataFrame:
  print("-----------------File Cleaning Started--------------------------\n")
  # Handle Missing Values - Price and Stock
  df["Price"] = df["Price"].fillna(df["Price"].median())

  # Change Data type - EAN, Price and Stocks
  df["EAN"] = df["EAN"].astype('str')
  df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
  df["Stock"] = pd.to_numeric(df["Stock"], errors="coerce")

  # Remove Spaces - Name, Description, Brand, Category, Currency, EAN, Color, Size, Availability
  cols = ["Name", "Description", "Brand", "Category", "Currency", "EAN", "Color", "Size", "Availability"]
  for col in cols:
    df[col] = df[col].str.strip()

  # Outliers Detection
  price_mean = df["Price"].mean()
  price_std = df["Price"].std()
  # Using Z Score method to find Outliers
  Z_Score = np.abs(df["Price"] - price_mean) / price_std
  # check whether it is outliers or not
  df["Is_Outlier"] = Z_Score > 3

  # Remove Duplicates
  df = df.drop_duplicates()

  print("------------------File Cleaning Ended--------------------------\n")

  return df