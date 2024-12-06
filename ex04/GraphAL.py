'''
4. Implemente um algoritmo para verificar se um grafo e acíclico utilizando o algoritmo
de busca em profundidade.
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
        
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node
    
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex" + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print("->{}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")

    def dfs(self, vertex, visited, parent): # Depth-First Search (Busca em Profundidade)
        visited[vertex] = True
        temp = self.graph[vertex]
        while temp:
            if not visited[temp.vertex]:
                if self.dfs(temp.vertex, visited, vertex):
                    return True
            elif temp.vertex != parent:
                return True # ciclo
            temp = temp.next
        return False

    def is_acyclic(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.dfs(i, visited, -1):
                    return False  # Graph contains a cycle
        return True  # Graph is acyclic

graph = GraphAL(5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
# graph.add_edge(4, 1)  # adicionar um ciclo
graph.print_agraph()
print("O grafo é acíclico?", graph.is_acyclic())
