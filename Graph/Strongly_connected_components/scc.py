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

        visited = [False]*self.v

        while stack:
            node = stack.pop()
            if not visited[node]:
                transpose.DFSUtils(visited, node)
                print("")




if __name__=='__main__':
    g = Graph(8)
    edges = [(0, 1),(1, 2),(2, 3),(2, 4),(3, 0),(4, 5),(5, 6),(6, 4),(6, 7)]
    for src, dest in edges:
        g.add_edge(src, dest)

    print("Strongly connected components of graph are:")
    g.find_scc()