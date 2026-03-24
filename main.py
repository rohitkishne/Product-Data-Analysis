import pandas as pd
from Src.Pipeline import run_pipeline

def main():
  # Loading the file
  print("------------------------Loading Started--------------------------------\n")
  # Product file
  df = pd.read_csv(r"Product_Data_Analysis\Data\products-100.csv")
  # Discount Mapping File
  map_df = pd.read_csv(r"Product_Data_Analysis\Data\Discount.csv")

  print("Data has been Fetched Properly!\n")

  print("--------------------------Data Loaded--------------------------------\n")

  # Run Pipeline
  final_df = run_pipeline(df, map_df)

  # print(final_df.head())

if __name__ == "__main__":
  main()