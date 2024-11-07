from node import Node
from mergeSort import *
class UnorderedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def isOrdered(self):
        if self.isEmpty():
            print("Empty list")
            return

        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    
    def push(self, new_data):
        new_node = Node(new_data)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node == None:
            print("Previous node not in list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def order(self):
        if self.isEmpty():
            print("Empty list")
        else:
            arr = []
            current = self.head
            while current:
                arr.append(current.data)
                current = current.next

            mergeSort(arr)

            current = self.head
            i = 0
            while current:
                current.data = arr[i]
                i += 1
                current = current.next

    def print(self):
        if self.isEmpty():
            print("Empty list")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ", end="")
                temp = temp.next
            print()

    def searchNode(self, data):
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self.head
            
            while temp:
                if temp.data == data:
                    return temp
                temp = temp.next
            return None
        
    def pop(self):
        if self.isEmpty():
            print("Empty list")
        else:
            self.head = self.head.next   
    
    def popEnd(self):
        if self.isEmpty():
            print("Empty list")
        else:
            
            penult = self.head
            last = self.head
            while last.next:
                penult = last
                last = last.next
            penult.next = None
            self.tail = penult

    def deleteNode(self, key):
        if self.isEmpty():
            print("Empty list")
        else:
            temp = self.head

            if temp is not None:
                if temp.data == key:
                    self.head = temp.next
                    temp = None
                    return
                
                while temp is not None:
                    if temp.data == key:
                        break
                    prev = temp
                    temp = temp.next

                    if temp == None:
                        return
                prev.next = temp.next
                temp = None

    def length(self):
        if self.isEmpty():
            return 0
        
        count = 1
        temp = self.head
        while temp.next:
            count += 1
            temp = temp.next
        return count

    def clear(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            self.head = None
