"""
Python implementation of adjaceny list graph representation
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.vertices = [None]*self.v
        self.visited = [False]*self.v
        self.recursion_Stack = [False]*self.v

    def add_edge(self, src, dest):

        #Adding destination node at source list
        src_node = Node(dest)
        src_node.next = self.vertices[src]
        self.vertices[src] = src_node

    def cyclic_util(self, node):
        self.visited[node] = True
        self.recursion_Stack[node] = True
        temp = self.vertices[node]
        while temp:
            if not self.visited[temp.data]:
                if self.cyclic_util(temp.data):
                    return True
            elif self.recursion_Stack[temp.data]:
                return True
            temp = temp.next
        self.recursion_Stack[node] = False
        return False


    def is_cyclic(self):
        for i in range(self.v):
            if not self.visited[i]:
                if self.cyclic_util(i):
                    return True

        return False

    def print_graph(self):
        for i in range(self.v):
            print(f'\nadjaceny list for node {i}: head', end='')
            temp = self.vertices[i]
            while temp:
                print(f'-->{temp.data}', end='')
                temp = temp.next


if __name__=='__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.print_graph()
    print()
    if g.is_cyclic():
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")