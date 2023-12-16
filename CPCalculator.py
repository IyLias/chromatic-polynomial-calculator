import copy

import networkx as nx
import numpy as np
from Graph import Graph

# This class for calculating chromatic polynomial of graphs
# CP stands for Chromatic Polynomial
class CPCalculator:

    def __init__(self):

        self.FRT_results = [(0,0)]
        self.FRT_levels = 0

        pass


    def init_values(self):
        self.FRT_results = [(0,0)]
        self.FRT_levels = 0


    def get_FRT_results(self):
        return self.FRT_results


    def get_FRT_levels(self):
        return self.FRT_levels


    def get_pair_of_vertices(self, G, is_adjacent):
        # return random pair of 2 vertices which are (non-)adjacent
        order = G.get_order()
        adj_mat = G.get_adj_matrix()

        for i in range(0, order):
            for j in range(0, order):
                if i!=j and adj_mat[i][j] == (0 if is_adjacent==False else 1) :
                    return [i,j]


    def cp_of_empty_graph(self, G):
        order = G.get_order()
        p = np.poly1d(np.poly1d([1, 1]) - np.poly1d([1]), variable='λ')
        p = np.poly1d(p ** order, variable='λ')
        return p

    def cp_of_complete_graph(self, G):
        order = G.get_order()
        p = np.poly1d([n for n in range(1,order)], True, variable='λ')
        p = np.poly1d(p * (np.poly1d([1, 1]) - np.poly1d([1])), variable='λ')
        return p


    def cp_of_cycle_graph(self, G):
        order = G.get_order()
        cf = np.poly1d([1], True, variable='λ')
        p = np.poly1d(cf ** order, variable='λ')

        if order % 2 == 1:
            cf = -cf
        p = np.poly1d(p + cf, variable='λ')
        return p


    def cp_of_tree(self, G):
        order = G.get_order()
        p = np.poly1d([1], True, variable='λ')
        p = np.poly1d(p ** (order-1), variable='λ')
        p = np.poly1d(p * (np.poly1d([1, 1]) - np.poly1d([1])), variable='λ')
        return p

    def get_chromatic_polynomial(self,G):

        # show basic info of given graph G
        print("Order of graph G is " + str(G.get_order()) + "  and " + "Size of graph G is " + str(G.get_size()))

        density = G.get_density()
        is_dense = True if density > 0.5 else False

        self.init_values()
        self.FRT_results.append((G,1))
        return self.FRT(G, is_dense,1)


    def FRT(self, G, is_dense, level):
        # This function produces chromatic polynomial of arbitrary graph G by using FRT
        # P(G, λ) = P(G + xy, λ) + P(G * xy, λ)
        print("level of G: ", level)
        print("adj_mat of G: ", G.get_adj_matrix())

        if self.FRT_levels < level:
            self.FRT_levels = level

        # exit conditions.. If G is O_n , K_n, C_n, T_n, then return its chromatic polynomial
        if G.is_empty_graph():
           return self.cp_of_empty_graph(G)

        if G.is_complete_graph():
            return self.cp_of_complete_graph(G)

        if G.is_cycle_graph():
            return self.cp_of_cycle_graph(G)

        if G.is_tree():
            return self.cp_of_tree(G)


        cp = 0
        g1 = copy.deepcopy(G)
        g2 = copy.deepcopy(G)

        if is_dense:
            [x,y] = self.get_pair_of_vertices(G, False)

            g1.add_edge(x+1,y+1)
            self.FRT_results.append((g1, level+1))

            g2.contraction(x+1,y+1)
            self.FRT_results.append((g2,level+1))

            cp = self.FRT(g1, is_dense,level+1) + self.FRT(g2, is_dense,level+1)

        else:
            [x, y] = self.get_pair_of_vertices(G, True)

            g1.delete_edge(x + 1, y + 1)
            self.FRT_results.append((g1, level+1))

            g2.contraction(x + 1, y + 1)
            self.FRT_results.append((g2, level+1))

            cp = self.FRT(g1, is_dense,level+1) - self.FRT(g2, is_dense,level+1)

        cp = np.poly1d(cp, variable='λ')
        return cp


