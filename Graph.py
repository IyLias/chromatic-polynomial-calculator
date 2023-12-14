import networkx as nx
import numpy as np

class Graph:

    def __init__(self, order, adj_mat):
        self.order = order
        self.adj_matrix = adj_mat

        size = 0
        for i in range(0,self.order):
            for j in range(0, self.order):
                if self.adj_matrix[i][j]:
                    size += self.adj_matrix[i][j]
        size /= 2
        self.size = int(size)

        self.G = nx.Graph()
        self.G.add_nodes_from(range(1,self.order+1))

        for i in range(0, self.order):
            for j in range(0, self.order):
                if i<=j and self.adj_matrix[i][j]:
                    self.G.add_edge(i+1,j+1)

        self.chromatic_number = 0
        self.chromatic_polynomial = 0

    def set_adj_matrix(self, adj_matrix):
        self.adj_matrix = adj_matrix



    def get_order(self):
        return self.order

    def get_size(self):
        return self.size

    def get_adj_matrix(self):
        return self.adj_matrix


    def is_empty_graph(self):
        if self.size == 0:
            return True
        else:
            return False


    def is_complete_graph(self):
        complete_size = int((self.order * (self.order-1))/2)
        if self.size == complete_size:
            return True
        else:
            return False



    def get_chromatic_polynomial(self):
        pass

    def get_graph(self):
        return self.G

    def add_edge(self, v1, v2):
        # add edge e = v1v2 to graph G
        if self.adj_matrix[v1-1][v2-1]==0:
            self.adj_matrix[v1-1][v2-1] = 1
            self.adj_matrix[v2- 1][v1- 1] = 1
            self.G.add_edge(v1,v2)
            self.size += 1


    def delete_edge(self, v1, v2):
        # delete edge e = v1v2 from graph G
        if self.adj_matrix[v1-1][v2-1] == 1:
            self.adj_matrix[v1-1][v2-1] = 0
            self.adj_matrix[v2-1][v1-1] = 0
            self.G.remove_edge(v1,v2)
            self.size -= 1

    def contraction(self, v1, v2):
        # graph contraction: vertex identification of v1 and v2
        # suppose v1 is attached to v2
        self.adj_matrix[v1-1][v2-1] = 0
        self.adj_matrix[v2-1][v1-1] = 0

        for i in range(0,self.order):
            if i != v1-1 and i != v2-1:
                if self.adj_matrix[i][v1-1]:
                    self.adj_matrix[i][v2-1] = 1
                    self.adj_matrix[v2-1][i] = 1

        new_mat = np.delete(self.adj_matrix, v1-1,0)
        new_mat = np.delete(new_mat, v1-1, 1)
        print(new_mat)
        self.adj_matrix = new_mat
        self.order -= 1

        self.G = nx.Graph()
        self.G.add_nodes_from(range(1,self.order+1))

        for i in range(0, self.order):
            for j in range(0, self.order):
                if i<=j and self.adj_matrix[i][j]:
                    self.G.add_edge(i+1,j+1)

        size = 0
        for i in range(0, self.order):
            for j in range(0, self.order):
                if self.adj_matrix[i][j]:
                    size += self.adj_matrix[i][j]
        size /= 2
        self.size = int(size)