from node import Node

class StackM():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def push(self, new_data):
        new_node = Node(new_data) 
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def print(self):
        if self.isEmpty():
            print("Pilha vazia.")
        else:
            temp = self.head
            while (temp):
                print(temp.data + " ",end="")
                temp = temp.next
            print()
    
    def pop(self):
        if self.isEmpty():
            print("Pilha vazia.")
        else:
            self.head = self.head.next
    
    def clear(self):
        if self.isEmpty():
            print("Pilha vazia.")
        else:
            self.head = None
    