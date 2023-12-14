from GraphManager import *
from Graph import Graph
from CPCalculator import CPCalculator
import numpy as np
import copy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adj_mat1 = [[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 0],
                [1, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [1, 0, 1, 1, 0] ]
    graph1 = Graph(5, adj_mat1)

    plot_r = 3
    plot_c = 3

    graphManager = GraphManager()
    graphManager.add_graph_on_figure(graph1, plot_r,plot_c,1)

    graph2 = copy.deepcopy(graph1)
    graph2.add_edge(3,4)

    graph2.contraction(2,5)
    graphManager.add_graph_on_figure(graph2,plot_r,plot_c,2)

    graph2.contraction(1, 3)
    graphManager.add_graph_on_figure(graph2,plot_r,plot_c,3)


    graph3 = copy.deepcopy(graph1)
    graph3.add_edge(2,5)
    graph3.add_edge(3, 4)

    graphManager.add_graph_on_figure(graph3,plot_r,plot_c,4)
    graphManager.show_figure()

    cpCalculator = CPCalculator()
    print(cpCalculator.get_chromatic_polynomial(graph3))