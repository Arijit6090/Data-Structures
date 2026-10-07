class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        # In case of directed graph there should be one way connection from source to destination
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def print_graph(self):
        for vertex in self.adjList:
            print(vertex," -> ",self.adjList[vertex])

# Test Case
g = Graph()

g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)

g.print_graph()