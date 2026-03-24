import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from Src.Util.graph_list import get_graphs

def dashboard_dropdown(df):

    graph_list, titles = get_graphs(df)

    fig, ax = plt.subplots(figsize=(18, 7.5))
    plt.subplots_adjust(left=0.3)

    def draw(index):
        ax.clear()
        graph_list[index](ax)
        ax.set_title(titles[index], fontsize=18, fontweight="bold", color="Red", pad=20,  bbox=dict(facecolor='honeydew', edgecolor='black'))
        plt.draw()

    rax = plt.axes([0.01, 0.4, 0.15, 0.4])
    radio = RadioButtons(rax, titles)

    def on_click(label):
        draw(titles.index(label))

    radio.on_clicked(on_click)

    draw(0)
    plt.show()