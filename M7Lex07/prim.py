from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def printMST(self, parent, key):
        print("Aresta \tPeso")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{key[i]}")

    def minKey(self, key, mstSet):
        min_value = float('inf')
        min_index = -1 
        for v in range(self.V):
            if key[v] < min_value and v not in mstSet:
                min_value = key[v]
                min_index = v
        return min_index

    def prim(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mstSet = set()

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet.add(u)

            for neighbor, weight in self.graph[u]:
                if neighbor not in mstSet and weight < key[neighbor]:
                    key[neighbor] = weight
                    parent[neighbor] = u
        
        return self.printMST(parent, key)


# a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8:
g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(2, 8, 2)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

mst = g.prim()
