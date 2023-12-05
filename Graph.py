import networkx as nx

class Graph:

    def __init__(self, order, size, edge_list):
        self.order = order
        self.size = size
        self.edge_list = edge_list

        self.G = nx.Graph()
        self.G.add_nodes_from(range(1,self.order+1))
        for edge in self.edge_list:
            self.G.add_edge(edge[0],edge[1])

        self.chromatic_number = 0
        self.chromatic_polynomial = 0


    def set_adj_matrix(self, adj_matrix):
        self.adj_matrix = adj_matrix



    def get_order(self):
        return self.order

    def get_size(self):
        return self.size

    def get_edge_list(self):
        return self.edge_list


    def get_graph(self):
        return self.G