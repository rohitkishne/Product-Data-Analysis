from Src.Util.File_info import File_Info
from Src.Util.Data_Cleaning import File_Cleaning
from Src.Util.Processing import File_Logic
from Src.Util.Analysis import analyse_data
from Src.Visualization.Normal_Visualization import Visualize_Data
from Src.Visualization.One_Screen_Multiple_Graph_Visualization import grid_dashboard
from Src.Visualization.Visualization_With_Button import button_dashboard
from Src.Visualization.Dropdown_Visualization import dashboard_dropdown

# ==============================Data Flow Pipeline================================
# Execution Flow
def run_pipeline(df, map_df):
  print("-------------Execution Started----------------\n")
  
  # File Information Fetching
  File_Info(df)

  # Data Cleaning and Processing
  df_clean = File_Cleaning(df)
  df_final = File_Logic(df_clean, map_df)

  # Analysis and Visualization
  analyse_data(df_final)
  # Visualize_Data(df_final)
  # grid_dashboard(df_final)
  # button_dashboard(df_final)
  dashboard_dropdown(df_final)

  print("-------------Execution Ended----------------\n")

  return df_final

