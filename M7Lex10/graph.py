from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Adiciona uma aresta ponderada no grafo (u -> v com peso)
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))  # Adiciona um vizinho com o peso

    def dijkstra(self, start):
        # Inicializa o dicionário de distâncias, incluindo todos os vértices
        # Incluindo os vértices que são destinos, mesmo que não tenham arestas de partida
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        # Conjunto de vértices não processados
        unvisited = set(self.graph.keys())
        
        # Adicionar vértices de destino que podem não estar no grafo como chaves
        for u in self.graph:
            for v, _ in self.graph[u]:
                unvisited.add(v)  # Inclui também os destinos das arestas

        while unvisited:
            # Encontra o vértice não visitado com a menor distância
            current_vertex = None
            current_distance = float('inf')
            
            for vertex in unvisited:
                if distances.get(vertex, float('inf')) < current_distance:
                    current_vertex = vertex
                    current_distance = distances.get(vertex, float('inf'))
            
            # Se não houver mais vértices a processar, o algoritmo terminou
            if current_vertex is None:
                break
            
            # Remove o vértice atual do conjunto de não visitados
            unvisited.remove(current_vertex)
            
            # Explora os vizinhos do vértice atual
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # Se a distância calculada para o vizinho for menor, atualize
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
        
        return distances


# Exemplo de uso do grafo
graph = Graph()

# Adicionando arestas ponderadas
graph.addEdge(0, 1, 5)
graph.addEdge(0, 2, 3)
graph.addEdge(1, 2, 2)
graph.addEdge(1, 4, 3)
graph.addEdge(1, 6, 1)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 4, 7)
graph.addEdge(3, 5, 6)
graph.addEdge(4, 3, 2)
graph.addEdge(4, 5, 1)
graph.addEdge(6, 4, 1)

# Teste o algoritmo de Dijkstra
start_vertex = 0
distances = graph.dijkstra(start_vertex)

# Imprimir as distâncias mínimas do vértice de origem para todos os outros
print(f"Distâncias mínimas a partir do vértice {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Vértice {vertex}: {distance}")
