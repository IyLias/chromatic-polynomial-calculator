import networkx as nx
import matplotlib.pyplot as plt

# This class manages the screen and shows multiple graphs
class GraphManager:

    def __init__(self,size_r, size_c):
        self.fig, self.axes = plt.subplots(size_r, size_c)

        pass


    def add_graph_on_figure(self, G,r,c,i):
        plt.subplot(r, c, i)
        plt.cla()

        graph = G.get_graph()
        nx.draw_circular(graph, with_labels=False)

    def show_figure(self):
        plt.show()