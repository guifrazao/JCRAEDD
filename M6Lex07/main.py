import random
from binarySearchTree import BinarySearchTree
def menu():
    bst = BinarySearchTree()

    while True:     
        print("\nMenu:")
        print("1 - Inserir número aleatório com geração e inserção aleatórias")
        print("2 - Mostrar os números da árvore usando o imprimeRelacoes")
        print("3 - Imprimir emOrdem, preOrdem e posOrdem")
        print("4 - Mostrar o maior número na árvore")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Gera um número aleatório entre 1 e 100
            numero = random.randint(1, 100)
            print(f"Inserindo o número aleatório: {numero}")
            bst.insert(numero)

        elif opcao == "2":
            print("\nMostrando relações dos nós na árvore:")
            bst.imprimeRelacoes(bst.root)

        elif opcao == "3":
            print("\nImpressões dos percursos:")
            print("Em Ordem: ", end="")
            bst.printInOrder(bst.root)
            print("\nPré-Ordem: ", end="")
            bst.printPreOrder(bst.root)
            print("\nPós-Ordem: ", end="")
            bst.printPostOrder(bst.root)

        elif opcao == "4":
            maior = bst.biggestNumber(bst.root)
            print(f"\nO maior número na árvore é: {maior}")

        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o programa
menu()
