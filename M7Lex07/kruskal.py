class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def addEdge(self, u, v, weight):
        self.edges.append([u, v, weight])

    def searchRoot(self, parent, i):
        if parent[i] == i:
            return i
        else:
            return self.searchRoot(parent, parent[i])

    def join(self, parent, rank, x, y):
        x_root = self.searchRoot(parent, x)
        y_root = self.searchRoot(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, weight = self.edges[i]
            i = i + 1
            x = self.searchRoot(parent, u)
            y = self.searchRoot(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, weight])
                self.join(parent, rank, x, y)

        return result

# a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8:
g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 4)
g.addEdge(2, 3, 7)
g.addEdge(2, 4, 4)
g.addEdge(2, 8, 2)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

mst = g.kruskal()

for u, v, weight in mst:
    print(f"Aresta {u}-{v} com peso {weight}")
