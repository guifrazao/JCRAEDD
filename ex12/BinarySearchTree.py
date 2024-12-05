'''
12. Adicione um método range Find a uma Árvore Binária de Busca. Esse método espera
dois itens como argumentos que especificam os limites de um intervalo dos itens a
serem encontrados na árvore. O método percorre a árvore e constrói e retorna uma
lista ordenada dos itens encontrados dentro do intervalo especificado.
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

    def printTree(self, node, level):
            if node is not None:
                self.printTree(node.right, level + 1)
                print(" "*level + f"-> {node.data}")
                self.printTree(node.left, level + 1)
    
    def deleteTree(self):
        self.root = None
    
    def rangeFind(self, node, low, high):
        if node is None:
            return []

        result = []

        if low <= node.data <= high:
            result.append(node.data)

        if node.data > low:
            result.extend(self.rangeFind(node.left, low, high))

        if node.data < high:
            result.extend(self.rangeFind(node.right, low, high))

        return sorted(result)

