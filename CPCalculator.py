import numpy as np
from Graph import Graph

# This class for calculating chromatic polynomial of graphs
# CP stands for Chromatic Polynomial
class CPCalculator:

    def __init__(self):

        #print(np.poly1d([1, 2, 3], True, variable='λ'))
        #p = np.poly1d(np.poly1d([1, 1]) - np.poly1d([1]), variable='λ')
        #p = np.poly1d(p ** 4, variable='λ')
        pass

    def cp_of_empty_graph(self, G):
        order = G.get_order()
        p = np.poly1d(np.poly1d([1, 1]) - np.poly1d([1]), variable='λ')
        p = np.poly1d(p ** order, variable='λ')
        return p

    def cp_of_complete_graph(self, G):
        order = G.get_order()
        p = np.poly1d([n for n in range(1,order)], True, variable='λ')
        return p

    def get_chromatic_polynomial(self,G):

        if G.is_empty_graph():
           return self.cp_of_empty_graph(G)

        if G.is_complete_graph():
            return self.cp_of_complete_graph(G)




    def FRT(self, G):
        pass


