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

    adj_mat2 = [
        [0,1,0,1],
        [1,0,1,1],
        [0,1,0,1],
        [1,1,1,0]
    ]
    adj_mat3 = [[0, 1, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1],
                [1, 1, 0, 1, 0]]

    
    adj_mat4 = [
        [0,1,1,0,0,0,0,0,0],
        [1,0,1,1,1,0,0,0,0],
        [1,1,0,1,1,0,0,0,0],
        [0,1,1,0,1,0,1,0,0],
        [0,1,1,1,0,0,0,1,0],
        [0,0,0,0,0,0,1,1,0],
        [0,0,0,1,0,1,0,1,1],
        [0,0,0,0,1,1,1,0,1],
        [0,0,0,0,0,1,1,1,0],
    ]

    graph1 = Graph(9, adj_mat4)

    cpCalculator = CPCalculator()
    print("Chromatic Polynomial of graph1: \n" + str(cpCalculator.get_chromatic_polynomial(graph1)))

    graphs = cpCalculator.get_FRT_results()
    level = cpCalculator.get_FRT_levels()
    #print(graphs)
    print(level)

    graphManager = GraphManager(0,0)
    #graphManager.add_graph_with_tree_structure(graphs, level)
    #graphManager.show_figure()


