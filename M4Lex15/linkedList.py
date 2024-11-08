from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserido {data}. Lista atual:", self.to_list_iterative())

    def to_list_iterative(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_recursive(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.head
        if node:
            result.append(node.data)
            self.to_list_recursive(node.next, result)
        return result

    def from_list_iterative(self, lst):
        self.head = None  
        for item in reversed(lst):
            self.insert(item)
        print("Lista criada a partir do vetor (iterativa):", self.to_list_iterative())

    def from_list_recursive(self, lst, index=0):
        self.head = None  
        self._from_list_recursive_helper(lst, index)
        print("Lista criada a partir do vetor (recursiva):", self.to_list_iterative())

    def _from_list_recursive_helper(self, lst, index):
        if index < len(lst):
            self.insert(lst[index])
            self._from_list_recursive_helper(lst, index + 1)