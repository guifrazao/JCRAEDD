'''
3. Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar todos
3 – Mostrar a sub-árvore direita de um nó
4 – Mostrar a sub-árvore esquerda de um nó
5 – Sair
'''

from nodeTree import NodeTree

class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
    def insert(self, node, data):
        if self.root is None:
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
    
    def deleteTree(self):
        self.root = None

    def printTree(self, node, level):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(" "*level + f"-> {node.data}")
            self.printTree(node.left, level + 1)
    
    def printLeftSubtree(self, node):
        if node and node.left:
            print("Left subtree:")
            self.printTree(node.left, 0)  
        else:
            print("No left subtree.")

    def printRightSubtree(self, node):
        if node and node.right:
            print("Right subtree:")
            self.printTree(node.right, 0) 
        else:
            print("No right subtree.")
