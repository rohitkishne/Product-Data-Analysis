import matplotlib.pyplot as plt
import matplotlib.axes as Axes
import seaborn as sns
import pandas as pd


# ================== Individual Graph Functions ====================

# Graph of analysing Stock Count  
def plot_stock_status(ax: Axes, df: pd.DataFrame):
  sns.countplot(x="Stock_Status", data=df, ax=ax)
  ax.set_xlabel("Stock Status", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 15, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  ax.set_ylabel("Count", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 20, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))


# Graph of analysing Category with their Average Price
def plot_avg_price_by_category(ax: Axes,df: pd.DataFrame):
  avg_price = df.groupby("Category")["Price"].mean()
  sns.barplot(y=avg_price.index, x=avg_price.values, ax=ax)
  ax.set_xlabel("Price", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 15  , bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  ax.set_ylabel("Category", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 2, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  plt.setp(ax.get_xticklabels(), rotation=90)

# Graph of analysing distribution of Discount
def plot_discount_distribution(ax, df: pd.DataFrame):
  sns.histplot(df["Discount_Rate"], bins=10, ax=ax)
  ax.set_xlabel("Discount", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 15, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  ax.set_ylabel("Count", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 20, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))

# Graph of analysing correlation between Price and Discount
def plot_price_vs_discount(ax, df: pd.DataFrame):
  sns.scatterplot(x="Price", y="Discount_Rate", data=df, ax=ax)
  ax.set_xlabel("Price", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 15, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  ax.set_ylabel("Discount", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 20, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  
# Graph of analysing correlation between Stock and Discount
def plot_stock_vs_discount(ax, df: pd.DataFrame):
  sns.scatterplot(x="Stock", y="Discount_Rate", data=df, ax=ax)
  ax.set_xlabel("Stock", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 15, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  ax.set_ylabel("Discount", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 20, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  
# Graph of analysing top 10 expensive products
def plot_top_expensive_products(ax: Axes, df: pd.DataFrame):
  top_product = df.sort_values(by="Price", ascending=False).head(10)
  sns.barplot(x=top_product["Price"], y=top_product["Name"], ax=ax)
  ax.set_xlabel("Price", fontsize=11, fontweight='bold', fontstyle = "italic", labelpad = 15, bbox=dict(facecolor='lightgray', edgecolor='black', linewidth=1))
  ax.tick_params(axis='y', labelsize=10)


# ===================== Graph Manager Function ======================

def get_graphs(df):

# Graph list contains all the graph which will show into visualization
  graph_list = [
    lambda ax: plot_stock_status(ax, df),
    lambda ax: plot_avg_price_by_category(ax, df),
    lambda ax: plot_discount_distribution(ax, df),
    lambda ax: plot_price_vs_discount(ax, df),
    lambda ax: plot_stock_vs_discount(ax, df),
    lambda ax: plot_top_expensive_products(ax, df)
  ]

# This is the indivual graph titles given to the graphs according to the graph list 
  titles = [
    "Stock Status Distribution",
    "Average Price by Category",
    "Discount Distribution",
    "Price vs Discount",
    "Stock vs Discount",
    "Top 10 Expensive Products"
  ]

  return graph_list, titles