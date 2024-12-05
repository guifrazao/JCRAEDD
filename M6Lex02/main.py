from binarySearchTree import BinarySearchTree

def criar_arvore():
    bst = BinarySearchTree()
    continuar = "s"
    while continuar == "s":
        try:      
            num = int(input("Digite um número: "))
            bst.insert(bst.root, num)
            continuar = input("\nDeseja cadastrar mais dados? [s/n]: ").lower()              
        except Exception as e:
            print(f"\nErro: {e}, tente novamente")
            continue
    
    return bst

def main():
    bst = None
    
    while True:
        print()
        print("\nMenu:")
        print("1. Criar árvore")
        print("2. Mostrar nós folha")
        print("3. Mostrar os nós ancestrais de um nó")
        print("4. Mostrar os descendentes de um nó")
        print("5. Mostrar o nó pais e os nós filhos de um nó")
        print("6. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            bst = criar_arvore()
            bst.printTree(bst.root, 0)

        elif choice == '2':
            if bst:
                print()
                bst.searchLeafNodes(bst.root)

        elif choice == '3':
            if bst:
                print()
                num = int(input("Digite um número da árvore: "))
                node = bst.search(bst.root, num)
                bst.searchAncestors(bst.root, node)

        elif choice == '4':
            if bst:
                print()
                num = int(input("Digite um número da árvore: "))
                node = bst.search(bst.root, num)
                bst.searchDescendants(node)
        elif choice == '5':
            if bst:
                print()
                num = int(input("Digite um número da árvore: "))
                node = bst.search(bst.root, num)
                bst.searchAncestorAndDescendants(bst.root, node)

        elif choice == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()