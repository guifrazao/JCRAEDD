from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        visited = [False]*(max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8, j = 9, k = 10, l = 11:
g = Graph() 
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 5)
g.addEdge(4, 5)
g.addEdge(4, 8)
g.addEdge(5, 2)
g.addEdge(5, 6)
g.addEdge(5, 8)
g.addEdge(5, 9)
g.addEdge(2, 6)
g.addEdge(2, 3)
g.addEdge(2, 7)
g.addEdge(6, 3) 
g.addEdge(6, 10)
g.addEdge(6, 7)
g.addEdge(6, 11)
g.addEdge(3, 7)
g.addEdge(7, 11)
g.addEdge(11, 10)
g.addEdge(10, 9)

print(g.BFS(1))