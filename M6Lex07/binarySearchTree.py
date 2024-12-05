from nodeTree import NodeTree
import random

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None
    
    def insert(self, data):
        if self.isEmpty():
            self.root = NodeTree(data)
        else:
            self.insert_random(self.root, data)

    def insert_random(self, node, data):
        if random.choice([True, False]):
            if node.left is None:
                node.left = NodeTree(data)
            else:
                self.insert_random(node.left, data)
        else:
            if node.right is None:
                node.right = NodeTree(data)
            else:
                self.insert_random(node.right, data)

    def imprimeRelacoes(self, node):
        if self.isEmpty():
            print("Empty tree")
        elif node is None:
            return
        else:
            if node.left:
                print(f"O nó de valor {node.left.data} é filho esquerdo de {node.data}")
            else:
                print(f"O nó de valor {node.data} não tem filho esquerdo")
            
            if node.right:
                print(f"O nó de valor {node.right.data} é filho direito de {node.data}")
            else:
                print(f"O nó de valor {node.data} não tem filho direito")
        
        # Recursivamente, imprime os filhos dos nós
        self.imprimeRelacoes(node.left)
        self.imprimeRelacoes(node.right)

    # Percurso em Ordem (inOrdem)
    def printInOrder(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if node.left:
                self.printInOrder(node.left)
            print(f"{node.data}", end=" ")
            if node.right:
                self.printInOrder(node.right)

    # Percurso Pré-Ordem (preOrder)
    def printPreOrder(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            print(f"{node.data}", end=" ")
            if node.left:
                self.printInOrder(node.left)
            if node.right:
                self.printInOrder(node.right)

    # Percurso Pós-Ordem (postOrder)
    def printPostOrder(self, node):
        if self.isEmpty():
            print("Empty tree")
        else:
            if node.left:
                self.printInOrder(node.left)
            if node.right:
                self.printInOrder(node.right)
            print(f"{node.data}", end=" ")

    # Método para encontrar o maior número na árvore
    def biggestNumber(self, node):
        if self.isEmpty():
            print("Empty tree")
        elif node is None:
            return float("-inf")
        else:
            biggest_left = self.biggestNumber(node.left)
            biggest_right = self.biggestNumber(node.right)
            return max(node.data, biggest_left, biggest_right)