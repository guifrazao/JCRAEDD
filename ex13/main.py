'''
13. Faça um programa que implemente uma lista encadeada de números inteiros com 
inserção de dados pelo usuário através de um menu. Escreva uma função que insira 
uma nova célula com conteúdo x imediatamente depois da k-ésima célula da lista 
encadeada e outra função que troque de posição duas células de uma mesma lista. 
Faça duas versões: uma iterativa e uma recursiva. 
'''

from linkedUnorderedList import UnorderedLinkedList
from swapFunctions import swapNodesIterative, swapNodesRecursive

def menu():
    option = -1
    while option < 0 or option > 9:
        print("\n1 - Inserir um novo nó no início.\n" +
              "2 - Adicionar um novo nó ao final.\n" +
              "3 - Inserir um novo nó após o nó anterior dado\n" +
              "4 - Imprimir a lista encadeada.\n" +
              "5 - Trocar dois nós (iterativo)\n" +
              "6 - Trocar dois nós (recursivo)\n" +
              "0 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 9:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    print("### Trocar Ordem de Duas Células da Lista Encadeada ###\n")
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
            key1 = input("Digite o valor do primeiro nó para trocar: ")
            key2 = input("Digite o valor do segundo nó para trocar: ")
            if swapNodesIterative(myList, key1, key2):
                print("Nós trocados com sucesso (iterativo).")
            else:
                print("Não foi possível trocar os nós (iterativo).")
        elif choice == 6:
            key1 = input("Digite o valor do primeiro nó para trocar: ")
            key2 = input("Digite o valor do segundo nó para trocar: ")
            if swapNodesRecursive(myList, key1, key2):
                print("Nós trocados com sucesso (recursivo).")
            else:
                print("Não foi possível trocar os nós (iterativo).")
        
        else:
            print("Opção inválida! Tente novamente.")

main()