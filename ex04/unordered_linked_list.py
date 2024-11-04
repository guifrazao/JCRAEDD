from node_single import Node

class UnorderedLinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
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

    def printList(self):
        if self.isEmpty():
            print("Empty list.")
        else:
            temp = self.head
            while(temp):
                print(temp.data + " ",end="")
                temp = temp.next
            print()

    def clear(self):
        if self.isEmpty():
            print("Empty list.")
        else:
            self.head = None

    
