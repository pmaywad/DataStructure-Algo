"""
Python program for topological sort of DAG
"""

from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.indegree = [0] * v

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.indegree[dest] += 1

    def topological_sort(self):
        print(self.indegree)
        L = []
        S = [i for i in range(self.v) if self.indegree[i] == 0]
        while S:
            start = S.pop()
            L.append(start)
            for m in self.graph[start]:
                self.indegree[m] -= 1

                if self.indegree[m] == 0:
                    S.append(m)

        for i in range(self.v):
            if self.indegree[i]:
                return None

        return L

if __name__=='__main__':

    graph = Graph(8)
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
    for src, dest in edges:
        graph.add_edge(src, dest)

    L = graph.topological_sort()
    if not L:
        print("Graph has atleast one cycle")
    else:
        print("Topological sort of given graph is %s" % L)

