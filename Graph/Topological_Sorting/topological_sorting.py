from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def topological_sortingUtils(self, node, stack, visited):
        visited[node] = True
        for i in self.graph[node]:
            if not visited[i]:
                self.topological_sortingUtils(i, stack, visited)
        stack.append(node)

    def topological_sorting(self):
        visited = [False]*self.v
        stack = []

        for i in range(self.v):
            if not visited[i]:
                self.topological_sortingUtils(i, stack, visited)

        print(stack[::-1])


if __name__=='__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Following is a Topological Sort of the given graph")

    # Function Call
    g.topological_sorting()