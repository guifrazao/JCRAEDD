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
    while option < 0 or option > 9:
        print("\n1 - Inserir um novo nó no início.\n" +
              "2 - Adicionar um novo nó ao final.\n" +
              "3 - Inserir um novo nó após o nó anterior dado\n" +
              "4 - Imprimir a lista encadeada.\n" +
              "5 - Remover próximo nó após o nó anterior (iterativo)\n" +
              "6 - Inserir um nó após (iterativo)\n" +
              "7 - Remover próximo nó após o nó anterior (recursivo)\n" +
              "8 - Inserir um nó após (recursivo)\n" +
              "0 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 9:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    print("### Lista Duplamente Encadeada Circular ###\n")
    choice = 100
    myList = DoublyCircularLinkedUnorderedList()

    while choice != 0:
        choice = menu()
        if choice == 0:
            print("Encerrando...\n")
            break
        elif choice == 1:
            myList.insert_front(int(input("Digite um número: ")))
        elif choice == 2:
            myList.insert_end(int(input("Digite um número: ")))
        elif choice == 3:
            prev_node_value = int(input("Digite o valor do nó anterior: "))
            prev_node = myList.searchNode(prev_node_value)
            if prev_node:
                myList.insert_after(prev_node, int(input("Digite um número: ")))
            else:
                print("Nó anterior não encontrado.")
        elif choice == 4:
            myList.display()
        elif choice == 5:
            prev_node_value = int(input("Digite o valor do nó anterior: "))
            prev_node = myList.searchNode(prev_node_value)
            if remove_node_iterative(myList, prev_node):
                print("Nó removido (iterativo).")
            else:
                print("Nó não encontrado ou lista vazia.")
        elif choice == 6:
            node_value = int(input("Digite o valor do nó anterior: "))
            node = myList.searchNode(node_value)
            if insert_after_node_iterative(myList, node, int(input("Digite um número: "))):
                print("Nó inserido após (iterativo).")
            else:
                print("Nó não encontrado ou lista vazia.")
        elif choice == 7:
            prev_node_value = int(input("Digite o valor do nó anterior: "))
            prev_node = myList.searchNode(prev_node_value)
            if remove_node_recursive(myList, prev_node):
                print("Nó removido (recursivo).")
            else:
                print("Nó não encontrado ou lista vazia.")
        elif choice == 8:
            node_value = int(input("Digite o valor do nó anterior: "))
            node = myList.searchNode(node_value)
            if insert_after_node_recursive(myList, node, int(input("Digite um número: "))):
                print("Nó inserido após (recursivo).")
            else:
                print("Nó não encontrado ou lista vazia.")
        else:
            print("Opção inválida! Tente novamente.")

main()