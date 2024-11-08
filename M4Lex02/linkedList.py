from node import Node

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, position, item):
        new_node = Node(item)
        
        # Caso a lista esteja vazia ou posição seja 0, insere no início
        if position == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Percorre até a posição anterior à desejada ou o final da lista
        current = self.head
        current_position = 0
        while current_position < position - 1 and current.next is not None:
            current = current.next
            current_position += 1

        # Insere o novo nó na posição correta
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Para indicar o final da lista