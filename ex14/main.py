'''
14. Faça um programa que implemente uma lista encadeada de números inteiros com 
inserção de dados pelo usuário através de um menu. Escreva uma função que inverta 
a ordem das células de uma lista encadeada (a primeira passa a ser a última, a 
segunda passa a ser a penúltima etc.). Faça isso sem usar espaço auxiliar, apenas 
alterando ponteiros. Dê duas soluções: uma iterativa e uma recursiva.
'''

from node import Node
from linkedUnorderedList import UnorderedLinkedList
from reverseFunctions import reverseIterative, reverseRecursive

def menu():
    option = -1
    while option < 0 or option > 7:
        print("\n1 - Inserir um novo nó no início.\n" +
              "2 - Adicionar um novo nó ao final.\n" +
              "3 - Inserir um novo nó após o nó anterior dado\n" +
              "4 - Imprimir a lista encadeada.\n" +
              "5 - Inverter a lista (iterativo)\n" +
              "6 - Inverter a lista (recursivo)\n" +
              "0 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 7:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    print("### Inverter Ordem da Lista Encadeada ###\n")
    choice = 100
    myList = UnorderedLinkedList()

    while choice != 0:
        choice = menu()
        if choice == 0:
            print("Encerrando...\n")
            break
        elif choice == 1:
            myList.push(input("Digite um item: "))
        elif choice == 2:
            myList.append(input("Digite um item: "))
        elif choice == 3:
            myList.insertAfter(myList.searchNode(input("Digite o item anterior: ")), input("Digite um item: "))
        elif choice == 4:
            myList.printList()
        elif choice == 5:
            reverseIterative(myList)
            print("Lista invertida (iterativo).")
        elif choice == 6:
            reverseRecursive(myList)
            print("Lista invertida (recursivo).")
        else:
            print("Opção inválida! Tente novamente.")

main()
