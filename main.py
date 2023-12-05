import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph


def print_graph(G):
    #subax1 = plt.subplot(121)
    #nx.draw(G, with_labels=True, font_weight='bold')
    nx.draw_circular(G, with_labels=True)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    edge_list1 = [[1,2],[1,3],[1,4],[1,5],
            [2,3],[2,4],[1,2],[3,5],
            [4,5]]
    graph1 = Graph(5, 8, edge_list1)

    print_graph(graph1.get_graph())


