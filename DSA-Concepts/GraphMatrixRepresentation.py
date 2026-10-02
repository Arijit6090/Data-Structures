class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    # Undirected Graph
    def add_edge(self, src, dest):
        if 0<=src<self.size and 0<=dest<self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else: 
            print("Invalid Edge")

    # Directed Graph
    def directed_edge(self, src, dest):
        if 0<=src<self.size and 0<=dest<self.size:
            self.mat[src][dest] = 1
        else: 
            print("Invalid Edge")

    # Weighted Graph (Undirected)
    def weighted_edge(self, src, dest, weight):
        if 0<=src<self.size and 0<=dest<self.size:
            self.mat[src][dest] = weight
            self.mat[dest][src] = weight
        else: 
            print("Invalid Edge")

    # Weighted Graph (Directed)
    # def weighted_edge(self, src, dest, weight):
    #    if 0<=src<self.size and 0<=dest<self.size:
    #        self.mat[src][dest] = weight
    #    else: 
    #        print("Invalid Edge")

    def print_graph(self):
        for row in self.mat:
            print(" ".join(map(str,row)))

G = Graph(5)

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)

G.print_graph()

print("\n")

G_W = Graph(5)

G_W.weighted_edge(0,1,4)
G_W.weighted_edge(0,2,3)
G_W.weighted_edge(1,3,4)
G_W.weighted_edge(2,3,5)
G_W.weighted_edge(2,4,4)
G_W.weighted_edge(3,4,2)

G_W.print_graph()