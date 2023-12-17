from GraphManager import *
from Graph import Graph
from CPCalculator import CPCalculator
import numpy as np
import copy


class TestCase:

    def __init__(self, graphManager, cpCalculator):

        self.graphManager = graphManager
        self.cpCalculator = cpCalculator

    def test(self):
        adj_mat1 = [[0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 0, 1],
                    [1, 1, 0, 0, 1],
                    [1, 0, 1, 1, 0]]

        adj_mat2 = [
            [0, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 1, 1, 0]
        ]
        adj_mat3 = [[0, 1, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1],
                    [1, 1, 0, 1, 0]]

        # adj_mat of chromatic equivalence type1 in chromatic polynomials book
        adj_mat4 = [
            [0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 0],
        ]

        # adj_mat of chromatic equivalence type2 in chromatic polynomials book
        adj_mat5 = [
            [0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 0],
        ]

        graph1 = Graph(5, adj_mat3)
        # graph2 = Graph(9, adj_mat5)

        print("Chromatic Polynomial of H1: \n" + str(cpCalculator.get_chromatic_polynomial("H1", graph1)))

        graphs = self.cpCalculator.get_FRT_results()
        level = self.cpCalculator.get_FRT_levels()
        # print(graphs)
        # print(level)

        # print("Chromatic Polynomial of H2: \n" + str(cpCalculator.get_chromatic_polynomial("H2", graph2)))

        # graphs = cpCalculator.get_FRT_results()
        level = cpCalculator.get_FRT_levels()
        # print(graphs)
        # print(level)

        self.graphManager.add_graph_with_tree_structure(graphs, level)
        self.graphManager.show_figure()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cpCalculator = CPCalculator()
    graphManager = GraphManager(0, 0)
    testcase1 = TestCase(graphManager, cpCalculator)

    testcase1.test()


