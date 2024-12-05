from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

    def DFS_nonrecursive(self, v):
        visited = set()
        stack = []
        stack.append(v)

        while stack != []:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current, end=" ")
                
                for neighbour in self.graph[current][::-1]: #precisa ser adicionado inversamente por ser uma pilha (LIFO)
                    if neighbour not in visited:
                        stack.append(neighbour)
                
        

                


