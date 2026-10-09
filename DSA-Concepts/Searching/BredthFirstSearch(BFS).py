from collections import deque
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

    # BFS
    def bfs(self, src):
        visited = [False]*self.size
        queue = deque([src])
        visited[src] = True
        while(queue):
            # v as vertex
            v = queue.popleft()
            print(v, end=" -> ")
            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)
        print("N")

G = Graph(5)

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(2,3) # this line will also give same answer. I was just testing
G.add_edge(2,4)
G.add_edge(3,4)

G.bfs(0)

