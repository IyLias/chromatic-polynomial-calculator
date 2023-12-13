from GraphManager import *
from Graph import Graph



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    edge_list1 = [[1,2],[1,3],[1,4],[1,5],
            [2,3],[2,4],[2,5],[3,5],
            [4,5]]
    graph1 = Graph(5,edge_list1)

    graphManager = GraphManager(10,10)
    graphManager.add_graph_on_figure(graph1, 1,2,1)

    graph2 = graph1
    graph2.add_edge(3,4)

    graphManager.add_graph_on_figure(graph2,2,2,2)

    graphManager.show_figure()