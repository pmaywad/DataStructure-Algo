"""
Python implementation for cycle detection in undirected graph
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.vertices = [None]*self.v

    def add_edge(self, src, dest):

        #Adding destination node at source list
        src_node = Node(dest)
        src_node.next = self.vertices[src]
        self.vertices[src] = src_node

        #Undirected graph, adding src node to destination list
        dest_node = Node(src)
        dest_node.next = self.vertices[dest]
        self.vertices[dest] = dest_node

    def print_graph(self):
        for i in range(self.v):
            print(f'\nadjaceny list for node {i}: head', end='')
            temp = self.vertices[i]
            while temp:
                print(f'-->{temp.data}', end='')
                temp = temp.next

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