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
    bst = BinarySearchTree()
    
    while True:
        print()
        print("\nMenu:")
        print("1. Inserir número")
        print("2. Mostrar se a árvore é estritamente binária")
        print("3. Mostrar se a árvore é completa")
        print("4. Mostrar se a árvore é cheia")
        print("5. Sair\n")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            try:      
                num = int(input("Digite um número: "))
                bst.insert(bst.root, num) 
            except Exception as e:
                print(f"\nErro: {e}, tente novamente")

        elif choice == '2':
            bst.printTree(bst.root, 0)
            print(bst.isStrictlyBinary(bst.root))

        elif choice == '3':
            print(bst.isComplete())

        elif choice == '4':
            print(bst.isStrictlyBinary(bst.root) and bst.isComplete())

        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()