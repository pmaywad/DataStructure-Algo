"""
Python program to get strongly connected components in a graph
"""

from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def DFSUtils(self, visited, node):
        visited[node] = True
        print(node, end='')
        for i in self.graph[node]:
            if not visited[i]:
                self.DFSUtils(visited, i)

    def fill_order(self, visited, stack, node):
        visited[node] = True
        for i in self.graph[node]:
            if not visited[i]:
                self.fill_order(visited, stack, i)

        stack.append(node)

    def get_transpose(self):
        graph = Graph(self.v)
        for i in self.graph:
            for j in self.graph[i]:
                graph.add_edge(j, i)

        return graph

    def find_scc(self):
        stack = []
        visited = [False]*self.v
        for i in range(self.v):
            if not visited[i]:
                self.fill_order(visited, stack, i)

        transpose = self.get_transpose()
        print(transpose.graph)

        visited = [False]*self.v
        print(stack)
        while stack:
            node = stack.pop()
            if not visited[node]:
                transpose.DFSUtils(visited, i)
                print("")




if __name__=='__main__':
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)
    g.find_scc()