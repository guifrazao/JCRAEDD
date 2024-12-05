from BinarySearchTree import BinarySearchTree

def menu():
    option = -1
    
    while option < 0 or option > 3:
        print("\n1 - Insert number in the Tree.\n" +
              "2 - Print the tree.\n" +
              "3 - Print tree relationships.\n" +
              "0 - Exit.\n")
        option = int(input("Enter your option:"))
        if option < 0 or option > 3:
            print("\tInvalid option! Enter again.")
    
    return option

def main():
    print("### Binary Search Tree ###")
    choice = 100
    
    bst = BinarySearchTree()
    
    while choice != 0:
        choice = menu()
    
        if choice == 0:
            print("\nClosing...\n")
            bst.deleteTree()
            break
        
        elif choice == 1:
            print("\nInserting elements...")
            bst.insert(bst.root, int(input("Enter an element:")))
                
        elif choice == 2:
            print("\nPrinting the tree...")
            bst.printTree(bst.root, 0)

        else:
            if bst.isEmpty():
                print("\nTree empty!")
            else:
                print("\nPrinting tree relationships...")
                bst.imprimeRelacoes(bst.root)

main()
