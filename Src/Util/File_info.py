import pandas as pd

# ===============================File Information Function========================
# Getting the File Information
def File_Info(df: pd.DataFrame) -> pd.DataFrame:
  print("-----------------Getting File Information--------------------------\n")
  pd.options.display.width = 1000
  pd.options.display.expand_frame_repr = False
  pd.options.display.max_columns = None
  pd.options.display.max_colwidth = None
  # Getting Row and Column info
  print(df.shape)
  print("-----------------------------------------------------------------------------")
  # Getting Column Information
  print(df.columns)
  print("-----------------------------------------------------------------------------")
  # Getting the File whole info
  print(df.info())
  print("-------------------------------------------------------------------------------")
  # Getting the Statistics Summary of Data
  print(df.describe())

  print("---------------------------File Information Ends Here-------------------------\n")