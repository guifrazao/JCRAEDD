from GraphAL import GraphAL

grafo = GraphAL(["A", "B", "C", "D", "E", "F", "G", "H"])

grafo.add_edge("A", "B")
grafo.add_edge("A", "E")
grafo.add_edge("A", "F")
grafo.add_edge("B", "C")
grafo.add_edge("B", "E")
grafo.add_edge("C", "D")
grafo.add_edge("E", "D")
grafo.add_edge("E", "G")
grafo.add_edge("F", "E")
grafo.add_edge("F", "H")
grafo.add_edge("G", "C")
grafo.add_edge("G", "H")
grafo.add_edge("H", "D")

grafo.print_agraph()
print("DFS:", grafo.dfs("A"))