from nodeTree import NodeTree

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root is None
    
    def insert(self, node, data):
        if self.isEmpty():
            self.root = NodeTree(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)
            if data > node.data:
                if node.right is None:
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)

    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)
        
    def printInOrder(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if node.left:
                self.printInOrder(node.left)
            print(f"{node.data} ", end="")
            if node.right:
                self.printInOrder(node.right)

    def printPreOrder(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            print(f"{node.data} ", end="")
            if node.left:
                self.printInOrder(node.left)
            if node.right:
                self.printInOrder(node.right)

    def printPostOrder(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if node.left:
                self.printInOrder(node.left)
            if node.right:
                self.printInOrder(node.right)
            print(f"{node.data} ", end="")

    def minNode(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            while node.left:
                node = node.left
            return node.data
        
    def maxNode(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            while node.right:
                node = node.right
            return node.data
    
    def heightTree(self, node):
        if node:
            return 1 + max(self.heightTree(node.left), self.heightTree(node.right))
        else:
            return 0
    
    def countNodes(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)

    def delete(self, node, data):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            #leaf node
            if node.left is None and node.right is None:
                return None
            #one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            #two children
            else:
                successor = self._minValueRight(node.right)
                node.data = successor.data
                node.right = self.delete(node.right, successor.data)

        return node

    def _minValueRight(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def printTree(self, node, level):
        if node:
            self.printTree(node.right, level+1)
            print("     " * level + f"-> {node.data}")
            self.printTree(node.left, level+1)

    def deleteTree(self):
        self.root = None

    def searchLeafNodes(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if not node.left and not node.right:
                print(f"{node.data} ", end="")
            if node.left:
                self.searchLeafNodes(node.left)
            if node.right:
                self.searchLeafNodes(node.right)

    def countLeafNodes(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            
            return self.countLeafNodes(node.left) + self.countLeafNodes(node.right)

    def isStrictlyBinary(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if node.left:
                if not node.right:
                    return False
                return self.isStrictlyBinary(node.left)
            
            if node.right:
                if not node.left:
                    return False
                return self.isStrictlyBinary(node.right)
            
            if self.countNodes(self.root) != 2 * self.countLeafNodes(self.root) - 1:
                return False
            
            return True

    def isComplete(self):
        if self.isEmpty():
            print("Empty list")
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if current:
                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    while queue:
                        if queue.pop(0):
                            return False
            return True
            
        
    # def searchAncestors(self, current, node):
    #     if self.isEmpty():
    #         print("Empty tree")
    #     else:
    #         if current is None:
    #             return
    #         if not current == node:
    #             print(f"{current.data} ", end="")
    #             if node.data < current.data:
    #                 return self.searchAncestors(current.left, node)
    #             else:
    #                 return self.searchAncestors(current.right, node)
                
    # def searchDescendants(self, node):
    #     if self.isEmpty():
    #         print("Empty tree")
    #     else:
    #         if node is None:
    #             return
    #         if node.left:
    #             print(f"{node.left.data} ", end="")
    #             self.searchDescendants(node.left)
    #         if node.right:
    #             print(f"{node.right.data} ", end="")
    #             self.searchDescendants(node.right)

    # def printChildrenNodes(self, node):
    #     if node is None:
    #         return
    #     if node.left:
    #         print(f"{node.left.data} ", end="")
    #     if node.right:
    #         print(f"{node.right.data} ", end="")

    # def searchAncestorAndDescendants(self, current, node):
    #     if self.isEmpty():
    #         print("Empty tree")
    #     else:
    #         if node is None:
    #             return
    #         if node == self.root:
    #             print("Parent: None \n")
    #             print("Descendants: ")
    #             self.searchDescendants(node)
    #         else:
    #             if node.data < current.data:
    #                 if current.left.data == node.data:
    #                     print(f"Parent: {current.data} \n")
    #                     print("Children: ")
    #                     self.printChildrenNodes(node)
    #                 else:
    #                     self.searchAncestorAndDescendants(current.left, node)
    #             if node.data > current.data:
    #                 if current.right.data == node.data:
    #                     print(f"Parent: {current.data} \n")
    #                     print("Childre3n: ")
    #                     self.printChildrenNodes(node)
    #                 else:
    #                     self.searchAncestorAndDescendants(current.right, node)



            