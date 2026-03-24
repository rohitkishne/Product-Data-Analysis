import matplotlib.pyplot as plt
import pandas as pd
from Src.Util.graph_list import get_graphs

# =============== Dashboard Creation Started =================

def grid_dashboard(df: pd.DataFrame):

  # Get the graph list and title from the get_graph function
  graph_list, titles = get_graphs(df) 

  # Layout preparation
  fig, axes = plt.subplots(2,3, figsize = (18,10))

  # convert 2D array to 1D list so that looping will be easy and perfect
  axes = axes.flatten() 

  # Iterate over individual graph into the graph list, Note: enumerate give both index along with values
  for i, graph in enumerate(graph_list):
    graph(axes[i])
    axes[i].set_title(titles[i])
  
  # It create the gap in the screen, between the graphs, reduces the overflowing issue
  plt.tight_layout()

  # Display the graphs
  plt.show()