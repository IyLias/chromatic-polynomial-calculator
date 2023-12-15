import networkx as nx
import numpy as np
from Graph import Graph

# This class for calculating chromatic polynomial of graphs
# CP stands for Chromatic Polynomial
class CPCalculator:

    def __init__(self):

        pass

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

        return self.FRT(G, is_dense)


    def FRT(self, G, is_dense):
        # This function produces chromatic polynomial of arbitrary graph G by using FRT
        # P(G, λ) = P(G + xy, λ) + P(G * xy, λ)

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
        if is_dense:
            [x,y] = self.get_pair_of_vertices(G, False)
            g1 = G.add_edge(x+1,y+1)
            g2 = G.contraction(x+1,y+1)
            cp = self.FRT(g1, is_dense) + self.FRT(g2, is_dense)

        else:
            [x, y] = self.get_pair_of_vertices(G, True)
            g1 = G.delete_edge(x + 1, y + 1)
            g2 = G.contraction(x + 1, y + 1)
            cp = self.FRT(g1, is_dense) - self.FRT(g2, is_dense)

        cp = np.poly1d(cp, variable='λ')
        return cp


