from node_double import Node

class DoublyCircularLinkedUnorderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def insert_end(self, new_data):
        new_node = Node(new_data)

        if self.isEmpty():
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
        else:
            current = self.head

            while(current.next != self.head):
                current = current.next

            new_node.next = current.next
            new_node.previous = current
            current.next.previous = new_node
            current.next = new_node

    def display(self):
        if self.isEmpty():
            print("List is Empty!!")
            return
        
        else:
            current = self.head.next
            if current == None:
                print("List is Empty!!")
            else:
                print(self.head.data," ",end="")
                while current != self.head:
                    print(current.data," ",end="")
                    current = current.next
    
    def clear(self): 
        self.head = None 
        self.tail = None