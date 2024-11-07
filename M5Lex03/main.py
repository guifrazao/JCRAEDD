from doublyCircularOrderedLinkedList import DoublyCircularOrderedLinkedList
from doublyCircularUnorderedLinkedList import DoublyCircularUnorderedLinkedList
def criar_lista():
    linkedList = DoublyCircularOrderedLinkedList()
    continuar = "s"
    while continuar == "s":
        try:      
            id = int(input("\nDigite a chave: "))
            nome = input("Digite o nome: ")
            linkedList.insert({"id": id, "name": nome})
            continuar = input("\nDeseja cadastrar mais dados? [s/n]: ").lower()              
        except Exception as e:
            print(f"\nErro: {e}, tente novamente")
            continue
    
    return linkedList

def concatenar(l1, l2): #l1/l2.head.previous = ultimo elemento
    l2.head.previous.next = l1.head
    l1.head.previous.next = l2.head
    l1.head.previous = l2.head.previous
    l2.head.previous = l1.head.previous
    
def intercalar(l1, l2):
    l3 = DoublyCircularUnorderedLinkedList()
    if l1.length() != l2.length():
        print("Listas não são intercaláveis")
        return
    
    currentL1 = l1.head
    currentL2 = l2.head
    current_list = l1

    while currentL1.next != l1.head or currentL2.next != l2.head:             
        if current_list == l1:
            l3.insert_end(currentL1.data)
            currentL1 = currentL1.next
            current_list = l2
        else:
            l3.insert_end(currentL2.data)
            currentL2 = currentL2.next
            current_list = l1
    
    l3.insert_end(currentL1.data)
    l3.insert_end(currentL2.data)

    return l3
    



def main():
    l1 = None
    
    while True:
        print("\nMenu:")
        print("1. Criar lista")
        print("2. Buscar um nome dado a chave")
        print("3. Inserir um novo elemento na lista")
        print("4. Remover elementos da lista")
        print("5. Imprimir lista")
        print("6. Copiar uma lista l1 para uma lista l2")
        print("7. Concatenar uma lista l1 com uma lista l2")
        print("8. Intercalar l1 e l2")
        print("9. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            l1 = criar_lista()

        elif choice == '2':
            key = int(input("\nDigite a chave: "))
            node = l1.searchNode(key)
            if node == None:
                print("Nenhum elemento com o ID especificado foi encontrado")
            else:
                print(node.data['name'])

        elif choice == '3':
            id = int(input("\nDigite a chave: "))
            nome = input("Digite o nome: ")
            l1.insert({"id": id, "name": nome})
            print("Elemento adicionado com sucesso")

        elif choice == '4':
            id = int(input("\nDigite a chave do elemento a ser removido: "))
            l1.deleteNode(id)

        elif choice == '5':
            l1.print()

        elif choice == '6':
            l2 = criar_lista()
            l1 = l2
            print("l2 copiada para l1")

        elif choice == '7':
            l2 = criar_lista()
            l2.print()
            concatenar(l1, l2)
        elif choice == '8':
            l2 = criar_lista()
            l2.print()
            lista_intercalada = intercalar(l1, l2)
            if lista_intercalada is not None:
                lista_intercalada.print()
        elif choice == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()