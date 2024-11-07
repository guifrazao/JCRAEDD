from node import Node
class DoublyCircularUnorderedLinkedList:
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
            
            while current.next != self.head:
                current = current.next
            
            new_node.next = current.next
            new_node.previous = current
            current.next.previous = new_node
            current.next = new_node

    def print(self):
        if self.isEmpty():
            print("Empty list")
        else:
            current = self.head.next
            if current == None:
                print("Empty list")
            else:
                print(f"{self.head.data['id']}: {self.head.data['name']} ", end="")
                while current != self.head:
                    print(f"{current.data['id']}: {current.data['name']} ", end="")
                    current = current.next
                print()

    def searchNode(self, data):
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self.head
            while temp:
                if temp.data['id'] == data:
                    return temp
                temp = temp.next
                if temp == self.head:
                    return None
            return None
        
    def pop(self):
        if self.isEmpty():
            print("Empty list")
        elif self.head == self.head.next:
            self.head = None
        else:
            current = self.head.next
            current.previous = self.head.previous
            self.head.previous.next = current
            self.head = None #facultativo?
            self.head = current
    
    def popEnd(self):
        if self.isEmpty():
            print("Empty list")
        elif self.head.next == self.head:
            self.head = None
        else:      
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.previous.next = current.next
            current.next.previous = current.previous
            current = None

    def deleteNode(self, key):
        if self.isEmpty():
            print("Empty list")
        else:
            if self.head.data['id'] == key:
                self.pop()
            else:
                current = self.head.next
                while current.data['id'] != key:
                    if current == self.head:
                        print("Element not found")
                        return
                    current = current.next

                current.previous.next = current.next
                current.next.previous = current.previous
                current = None

    def clear(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            self.head = None

    def length(self):
        if self.isEmpty():
            return 0
        
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count



