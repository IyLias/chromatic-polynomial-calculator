import networkx as nx
import matplotlib.pyplot as plt
import math
from Graph import Graph

# This class manages the screen and shows multiple graphs
class GraphManager:

    def __init__(self,r,c):
        self.plot_r = r
        self.plot_c = c

    def add_graph_on_figure(self, G,i):

        plt.subplot(self.plot_r,self.plot_c,i)

        graph = G.get_graph()
        nx.draw_circular(graph, with_labels=False)


    def add_graph_with_tree_structure(self, graphs, level):
        self.plot_r = level
        k = self.plot_c = 2**level-1
        unit = 2 ** math.floor(math.log2(k))

        cur_level = 0
        nth = 1
        for g, level in graphs:
            if level == 0:
                continue

            if cur_level != level:
                cur_level = level
                nth = 1
            else:
                nth += 1

            value = (level-1)*k + int((unit * (2*nth -1)) / 2 ** (level-1))
            plt.subplot(self.plot_r, self.plot_c, value)

            nx.draw_circular(g.get_graph(), with_labels=False)


    def show_figure(self):
        plt.show()