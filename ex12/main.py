from BinarySearchTree import BinarySearchTree

def menu():
    option = -1

    while option < 0 or option > 12:
        print("\n1 - Insert number in the Tree.\n" +
              "2 - Print the tree.\n" +
              "3 - Find elements in a range.\n" +
              "0 - Exit.\n")
        option = int(input("Enter your option:"))
        if option < 0 or option > 12:
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
            if bst.isEmpty():
                print("\nTree empty!")
            else:
                print("\nPrinting the tree...")
                bst.printTree(bst.root, 0)

        else:
            if bst.isEmpty():
                print("\nTree empty!")
            else:
                print("\nFinding elements in a range...")
                low = int(input("Enter the lower bound:"))
                high = int(input("Enter the upper bound:"))
                print(f"Elements in range [{low}, {high}]: {bst.rangeFind(bst.root, low, high)}")

main()