import networkx as nx

class Graph:

    def __init__(self, order, edge_list):
        self.order = order
        self.edge_list = edge_list
        self.size = len(self.edge_list)

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

    def add_edge(self, v1, v2):
        # add edge e = v1v2 to graph G
        self.G.add_edge(v1,v2)


    def delete_edge(self, v1, v2):
        # delete edge e = v1v2 from graph G
        self.G.remove_edge(v1,v2)

