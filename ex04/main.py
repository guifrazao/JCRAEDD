from GraphAL import *

def main():
    num_vertices = int(input("Digite o número de vértices no grafo: "))
    graph = GraphAL(num_vertices)

    while True:
        print("\nMenu:")
        print("1. Adicionar aresta")
        print("2. Imprimir grafo")
        print("3. Verificar se o grafo é acíclico")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            s = int(input("Digite o vértice de origem: "))
            d = int(input("Digite o vértice de destino: "))
            if s < num_vertices and d < num_vertices:
                graph.add_edge(s, d)
                print(f"Aresta adicionada entre {s} e {d}.")
            else:
                print("Erro: Vértices inválidos.")

        elif opcao == 2:
            print("Representação do grafo:")
            graph.print_agraph()

        elif opcao == 3:
            if graph.is_acyclic():
                print("O grafo é acíclico.")
            else:
                print("O grafo contém ciclos.")

        elif opcao == 4:
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
