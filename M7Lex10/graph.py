from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight)) 

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        unvisited = set(self.graph.keys())
        
        for u in self.graph:
            for v, _ in self.graph[u]:
                unvisited.add(v) 

        while unvisited:
            current_vertex = None
            current_distance = float('inf')
            
            for vertex in unvisited:
                if distances.get(vertex, float('inf')) < current_distance:
                    current_vertex = vertex
                    current_distance = distances.get(vertex, float('inf'))
            
            if current_vertex is None:
                break
            
            unvisited.remove(current_vertex)
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
        
        return distances



graph = Graph()


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

start_vertex = 0
distances = graph.dijkstra(start_vertex)

print(f"Distâncias mínimas a partir do vértice {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Vértice {vertex}: {distance}")
