"""
Python implementation of adjacency matrix representation of graph
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.matrix = []
        for i in range(self.v):
            self.matrix.append([0]*self.v)

    def add_edge(self, src, dest):
        self.matrix[src][dest] = 1
        self.matrix[dest][src] = 1

    def print_graph(self):
        print(self.matrix)


if __name__=='__main__':
    v = 5
    graph = Graph(v)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
