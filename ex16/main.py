'''
16. Faça um programa que implemente uma lista duplamente encadeada de números 
inteiros com inserção de dados pelo usuário através de um menu. Escreva uma 
função que remova da lista a célula apontada por p e outra função que insira uma 
nova célula com conteúdo x nesta lista duplamente encadeada logo após a célula 
apontada por p. Dê duas soluções: uma iterativa e uma recursiva.
'''

from doublyCircularLinkedUnorderedList import DoublyCircularLinkedUnorderedList
from listFunctions import *

def menu():
    option = -1
    while option < 0 or option > 7:
        print("\n1 - Inserir um novo nó no início.\n" +
              "2 - Adicionar um novo nó ao final.\n" +
              "3 - Imprimir a lista encadeada.\n" +
              "4 - Remover próximo nó após o nó anterior (iterativo)\n" +
              "5 - Inserir um nó após (iterativo)\n" +
              "6 - Remover próximo nó após o nó anterior (recursivo)\n" +
              "7 - Inserir um nó após (recursivo)\n" +
              "0 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 7:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    print("### Lista Duplamente Encadeada ###\n")
    choice = 100

    linked_list = DoublyCircularLinkedUnorderedList()

    while choice != 0:
        choice = menu()

        if choice == 0:
            print("Encerrando...\n")
            break

        elif choice == 1:
            linked_list.insert_front(int(input("Digite um número: ")))

        elif choice == 2:
            linked_list.insert_end(int(input("Digite um número: ")))

        elif choice == 3:
            linked_list.display()

        elif choice == 4:
            prev_node_value = int(input("Digite o valor do nó anterior: "))
            prev_node = linked_list.searchNode(prev_node_value)
            if prev_node:
                if remove_node_iterative(linked_list, prev_node):
                    print("Nó removido (iterativo).")
                else:
                    print("Nó não encontrado ou lista vazia.")
            else:
                print("Nó anterior não encontrado.")

        elif choice == 5:
            node_value = int(input("Digite o valor do nó anterior: "))
            node = linked_list.searchNode(node_value)
            if node:
                if insert_after_node_iterative(linked_list, node, int(input("Digite um número: "))):
                    print("Nó inserido após (iterativo).")
                else:
                    print("Nó não encontrado ou lista vazia.")
            else:
                print("Nó anterior não encontrado.")

        elif choice == 6:
            prev_node_value = int(input("Digite o valor do nó anterior: "))
            prev_node = linked_list.searchNode(prev_node_value)
            if prev_node:
                if remove_node_recursive(linked_list, prev_node_value):
                    print("Nó removido (recursivo).")
                else:
                    print("Nó não encontrado ou lista vazia.")
            else:
                print("Nó anterior não encontrado.")

        elif choice == 7:
            node_value = int(input("Digite o valor do nó anterior: "))
            node = linked_list.searchNode(node_value)
            if node:
                if insert_after_node_recursive(linked_list, node_value, int(input("Digite um número: "))):
                    print("Nó inserido após (recursivo).")
                else:
                    print("Nó não encontrado ou lista vazia.")
            else:
                print("Nó anterior não encontrado.")

main()

