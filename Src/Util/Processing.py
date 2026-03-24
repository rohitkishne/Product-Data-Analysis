import pandas as pd
import numpy as np
from Src.Util.Discount import getDiscount
from Src.Util.Stock import Stock_Situation

# ===============================Implement Logic Function==============================
# Building Logic and Calculation
def File_Logic(df: pd.DataFrame, map_df: pd.DataFrame) -> pd.DataFrame:
  print("-----------------File Logic Started--------------------------\n")
  
  # Getting Discount over price on the basis of Categories and Stock
  df = getDiscount(df, map_df)

  # Stock Insight - give the info about Stock Requirement
  df = Stock_Situation(df)

  print("------------------File Logic Ended--------------------------\n")

  return df
