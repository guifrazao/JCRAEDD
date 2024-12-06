from GraphAL import GraphAL

grafo = GraphAL(9)  

arestas = [
    (1, 2),
    (2, 3), (2, 4),  
    (3, 2),  
    (4, 5), (4, 7),  
    (5, 3), (5, 8),  
    (6, 8), 
    (9, 1)   
]

for u, v in arestas:
    grafo.add_edge(u - 1, v - 1)

grafo.print_agraph()

print("BFS:", grafo.bfs(0))
print("DFS:", grafo.dfs(0))
print()


grafo_2 = GraphAL(9)  

arestas_2 = [
    (1, 2), (1, 9),  
    (2, 3),  
    (3, 5), (3, 6),
    (4, 2), (4, 7), 
    (5, 3), (5, 4),  
    (6, 8), 
    (7, 8),
    (8, 5),
    (9, 1)   
]

for x, y in arestas_2:
    grafo_2.add_edge(x - 1, y - 1)

grafo_2.print_agraph()

print("BFS:", grafo_2.bfs(0))
print("DFS:", grafo_2.dfs(0))