from BinarySearchTree import BinarySearchTree
from nodeTree import NodeTree

def menu():
    option = -1
    
    while option < 0 or option > 4:
        print("\n1 - Insert number in the Tree.\n" +
              "2 - Print the tree.\n" +
              "3 - Show left subtree of a node.\n" +
              "4 - Show right subtree of a node.\n" +
              "0 - Exit.\n")
        option = int(input("Enter your option:"))
        if option < 0 or option > 4:
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
            data = int(input("\nEnter an element: "))
            if bst.isEmpty():
                bst.root = NodeTree(data)
            else:
                bst.insert(bst.root, data)
            print(f"Element {data} inserted.")
        
        elif choice == 2:
            print("\nPrinting the tree...")
            bst.printTree(bst.root, 0)
        
        elif choice == 3:
            data = int(input("\nEnter the node's value to show its left subtree: "))
            node = bst.search(bst.root, data)
            if node:
                bst.printLeftSubtree(node)
            else:
                print(f"\nNode with value {data} not found.")
        
        elif choice == 4:
            data = int(input("\nEnter the node's value to show its right subtree: "))
            node = bst.search(bst.root, data)
            if node:
                bst.printRightSubtree(node)
            else:
                print(f"Node with value {data} not found.")

main()
