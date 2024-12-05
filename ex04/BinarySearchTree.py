'''
4. Apenas imprimindo linearmente os elementos da árvore não é possível reproduzir
sua estrutura. Faça um método imprimeRelacoes que percorra a árvore imprimindo
as relações entre os nós, de forma que se possa através dessa descrição reproduzir a
estrutura de uma árvore. Exemplos de descrições impressas são:
- o nó de valor XXX é filho esquerdo de YYY
- o nó de valor ZZZ é filho direito de YYY
- o nó de valor XXX não tem filho esquerdo
- o nó de valor ZZZ não tem filho direito
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

    def imprimeRelacoes(self, node):
        if node is None:
            return

        if node.left:
            print(f"O nó de valor {node.left.data} é filho esquerdo de {node.data}")
        else:
            print(f"O nó de valor {node.data} não tem filho esquerdo")

        if node.right:
            print(f"O nó de valor {node.right.data} é filho direito de {node.data}")
        else:
            print(f"O nó de valor {node.data} não tem filho direito")

        self.imprimeRelacoes(node.left)
        self.imprimeRelacoes(node.right)

