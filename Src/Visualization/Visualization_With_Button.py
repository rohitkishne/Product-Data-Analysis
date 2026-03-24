import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Button
from Src.Util.graph_list import get_graphs

# ============================ Button Dashboard ======================
def button_dashboard(df: pd.DataFrame):

  # Unpacking the get_graphs function return values
  graph_list, titles = get_graphs(df)

  # Dashboard Layout 
  fig, ax = plt.subplots(figsize = (10,8))

  # Create bottom Space for buttons
  plt.subplots_adjust(bottom=0.25, left=0.18)

  # Current State of Graph
  state = {"i" : 0}

  # Start drawing the Graph
  def draw():
    ax.clear()
    graph_list[state["i"]](ax)
    ax.set_title(titles[state["i"]])
    plt.draw()

  # Creating the Next Button Functionality
  def Next_Button(event):
    state["i"] = (state["i"]+1) % len(graph_list)
    draw()
  
  # Creating the Previous Button Functionality
  def Prev_Button(event):
    state["i"] = (state["i"]-1) % len(graph_list)
    draw()


  # Creating the place for Next and Previous Button
  axprev = plt.axes([0.3, 0.05, 0.1, 0.06])
  axnext = plt.axes([0.6, 0.05, 0.1, 0.06])

  # Give the functionality to the Buttons
  # Previous Button
  btn_prev = Button(axprev, "Previous")
  btn_prev.on_clicked(Prev_Button)

  # Next Button
  btn_next = Button(axnext, "Next")
  btn_next.on_clicked(Next_Button)

  # Finally creating the graph starts from here
  draw()

  # Display the Graphs
  plt.show()  
  


