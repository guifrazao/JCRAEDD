from unorderedLinkedList import UnorderedLinkedList
from unorderedLinkedListRecursive import UnorderedLinkedListRecursive

def criar_lista():
    linkedList = UnorderedLinkedListRecursive() if input("Recursiva ou não? [s/n]: ").lower() == "s" else UnorderedLinkedList()
    continuar = "s"
    while continuar == "s":
        try:      
            numero = int(input("\nDigite o número: "))
            linkedList.append(numero)
            continuar = input("\nDeseja cadastrar mais dados? [s/n]: ").lower()              
        except Exception as e:
            print(f"\nErro: {e}, tente novamente")
            continue
    
    return linkedList

def main():
    l1 = criar_lista()
    
    while True:
        print("\nMenu:")
        print("1. Fazer cópia da lista")
        print("2. Concatenar listas")
        print("3. Imprimir lista")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            l2 = l1.makeCopy() if isinstance(l1, UnorderedLinkedList) else l1.makeCopy(UnorderedLinkedListRecursive(), l1.head)
            print(f"Cópia feita. Endereço da lista antiga: {l1}. Endereço da lista nova: {l2}")
            l1.print()
            l2.print()
        elif choice == '2':
            l2 = criar_lista()
            l1.concat(l2)
            print("Lista concatenada com sucesso")
            l1.print()
        elif choice == '3':
            l1.print()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()