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

    #graph2 = copy.deepcopy(graph1)
    #graph2.add_edge(3,4)

    #graph2.contraction(2,5)
    #graphManager.add_graph_on_figure(graph2,plot_r,plot_c,2)

    #graph2.contraction(1, 3)
    #graphManager.add_graph_on_figure(graph2,plot_r,plot_c,3)


    #graph3 = copy.deepcopy(graph1)
    #graph3.add_edge(2,5)
    #graph3.add_edge(3, 4)

    #graphManager.add_graph_on_figure(graph3,plot_r,plot_c,4)

    cpCalculator = CPCalculator()
    #print(cpCalculator.get_chromatic_polynomial(graph3))

    adj_mat2 = [[0, 1, 1,],
                [1, 0, 1,],
                [1, 1, 0,]]
    graph4 = Graph(3, adj_mat2)

    adj_mat3 = [[0,1,1,0],
                [1,0,0,1],
                [1,0,0,1],
                [0,1,1,0]]
    graph5 = Graph(4, adj_mat3)

    graphManager.add_graph_on_figure(graph4, plot_r, plot_c, 5)
    graphManager.add_graph_on_figure(graph5, plot_r, plot_c, 6)

    print("Chromatic Polynomial of graph1: \n" + str(cpCalculator.get_chromatic_polynomial(graph1)))

    adj_mat4 = [[0,1,0,0,1],
                [1,0,1,0,1],
                [0,1,0,1,0],
                [0,0,1,0,1],
                [1,1,0,1,0]]

    graph6 = Graph(5, adj_mat4)

    graphManager.add_graph_on_figure(graph6, plot_r, plot_c, 7)

    print("Chromatic Polynomial of graph6: \n" + str(cpCalculator.get_chromatic_polynomial(graph6)))

    adj_mat5 = [[0,1,0,0,0],
                [1,0,1,0,0],
                [0,1,0,1,0],
                [0,0,1,0,1],
                [0,0,0,1,0]]

    graph7 = Graph(5, adj_mat5)

    graphManager.add_graph_on_figure(graph7, plot_r, plot_c, 8)
    graphManager.show_figure()

    print("Chromatic Polynomial of graph7: \n" + str(cpCalculator.get_chromatic_polynomial(graph7)))
