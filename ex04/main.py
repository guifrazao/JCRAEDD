'''
4. Defina uma função makeTwoWay que espera uma estrutura unicamente ligada como 
o argumento. A função cria e retorna uma estrutura duplamente ligada que contém os 
itens na estrutura unicamente ligada. (Nota: A função não deve alterar a estrutura do 
argumento.) 
'''

from unordered_linked_list import UnorderedLinkedList
from doubly_circular_linked_list import DoublyCircularLinkedUnorderedList
from conversion_functions import makeTwoWay

def menu():
    option = -1
    while option < 0 or option > 6:
        print("\n1 - Inserir um novo nó no início (lista ligada simples).\n" +
              "2 - Imprimir a lista ligada simples.\n" +
              "3 - Converter para lista duplamente ligada e imprimir.\n" +
              "4 - Limpar a lista ligada simples.\n" +
              "5 - Imprimir a lista duplamente ligada.\n" +
              "6 - Limpar a lista duplamente ligada.\n" +
              "0 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 6:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    print("### Converter Lista Ligada para Lista Duplamente Ligada ###\n")
    choice = 100

    myList = None
    doublyLinkedList = None

    while choice != 0:
        choice = menu()

        if choice == 0:
            print("Encerrando...\n")
            break

        elif choice == 1:
            if myList is None:
                myList = UnorderedLinkedList()
            myList.push(input("Digite um item: "))
        
        elif choice == 2:
            if myList is not None:
                myList.printList()
            else:
                print("A lista ligada simples não foi criada ainda.")
        
        elif choice == 3:
            if myList is not None:
                doublyLinkedList = makeTwoWay(myList)
                print("Lista duplamente ligada:", end=" ")
                doublyLinkedList.display()
                print()
            else:
                print("A lista ligada simples não foi criada ainda.")
        
        elif choice == 4:
            if myList is not None:
                myList.clear()
                print("Lista ligada simples limpa.")
            else:
                print("A lista ligada simples não foi criada ainda.")
        
        elif choice == 5:
            if doublyLinkedList is not None:
                print("Lista duplamente ligada:", end=" ")
                doublyLinkedList.display()
                print()
            else:
                print("A lista duplamente ligada não foi criada ainda.")
        
        elif choice == 6:
            if doublyLinkedList is not None:
                doublyLinkedList = DoublyCircularLinkedUnorderedList()
                print("Lista duplamente ligada limpa.")
            else:
                print("A lista duplamente ligada não foi criada ainda.")

main()

