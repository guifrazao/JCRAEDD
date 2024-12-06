'''
9. Dado os grafos abaixo, crie um programa que mostre o resultado da busca em
largura e em profundidade começando do vértice 1
'''

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class GraphAL:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
        
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node
    
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex" + str(i + 1) + ":", end="")
            temp = self.graph[i]
            while temp:
                print("->{}".format(temp.vertex + 1), end="")
                temp = temp.next
            print("\n")
    
    def bfs(self, start):
        visited = [False] * self.V
        queue = []
        bfs_result = []
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            vertex = queue.pop(0)
            bfs_result.append(vertex + 1)
            
            temp = self.graph[vertex]
            while temp:
                if not visited[temp.vertex]:
                    queue.append(temp.vertex)
                    visited[temp.vertex] = True
                temp = temp.next
        
        return bfs_result

    def dfs(self, start):
        visited = [False] * self.V
        stack = [start]  
        dfs_result = []
        
        while stack:
            vertex = stack.pop()  
            if not visited[vertex]:
                visited[vertex] = True
                dfs_result.append(vertex + 1)  
                
                temp = self.graph[vertex]
                while temp:
                    if not visited[temp.vertex]:
                        stack.append(temp.vertex)
                    temp = temp.next
        
        return dfs_result

