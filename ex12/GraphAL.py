'''
12. Considerando o grafo a seguir, crie um programa que execute a busca em
profundidade partindo do vértice a.
'''

class AdjNode:
    def __init__(self, value):
        self.vertex = value  # Valor do nó agora é do tipo string
        self.next = None

class GraphAL:
    def __init__(self, vertices):
        self.vertices = vertices  # Lista de vértices (do tipo string)
        self.V = len(vertices)   # Número de vértices
        self.graph = [None] * self.V
        
    def add_edge(self, s, d):
        s_index = self.vertices.index(s)  
        d_index = self.vertices.index(d)  
        
        node = AdjNode(d)
        node.next = self.graph[s_index]
        self.graph[s_index] = node

    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + self.vertices[i] + ":", end="")
            temp = self.graph[i]
            while temp:
                print("->{}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")
    
    def dfs(self, start):
        visited = [False] * self.V
        stack = [start]  
        dfs_result = []
        
        while stack:
            vertex = stack.pop()  # Remove o topo da pilha
            vertex_index = self.vertices.index(vertex)  # Índice do vértice
            
            if not visited[vertex_index]:
                visited[vertex_index] = True
                dfs_result.append(vertex)  # Adiciona ao resultado
                
                # Adiciona os vizinhos à pilha
                temp = self.graph[vertex_index]
                while temp:
                    if not visited[self.vertices.index(temp.vertex)]:
                        stack.append(temp.vertex)
                    temp = temp.next
        
        return dfs_result




