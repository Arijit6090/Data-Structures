# Aita amar pakamo chilo, Emni kono dorkar nei
from collections import deque

class Graph:
    def __init__(self, vertex):
        self.mat = [[0] * vertex for x in range(vertex)]
        self.size = vertex

    # Undirected Graph
    def add_edge(self, src, dest):
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")

    # Recursive BFS
    def bfs(self, src):
        visited = [False] * self.size
        queue = deque([src])

        visited[src] = True

        def bfs_recursive():
            # Base case
            if not queue:
                return

            # Remove vertex from front
            v = queue.popleft()
            print(v, end=" -> ")

            # Find neighbours
            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)

            # Recursive call
            bfs_recursive()

        bfs_recursive()

        print("N")


G = Graph(5)

G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

G.bfs(0)