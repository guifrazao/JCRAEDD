from node import Node
class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def insert(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            tempPrevious = None
            tempCurrent = self.head

            while tempCurrent != None and new_node.data['salary'] < tempCurrent.data['salary']:
                tempPrevious = tempCurrent
                tempCurrent = tempCurrent.next
            
            if tempPrevious == None:
                new_node.next = self.head
                self.head = new_node
            elif tempCurrent == None:
                self.tail.next = new_node
                self.tail = new_node
            else:
                tempPrevious.next = new_node
                new_node.next = tempCurrent

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
        while temp.next:
            count += 1
            temp = temp.next
        return count

    def searchHighestSalaryEmployee(self):
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self.head
            list = []
            highestEmployee = self.head.data
            
            while temp.next:
                if temp.data['salary'] < temp.next.data['salary']:
                    highestEmployee = temp.data
                temp = temp.next
            

            temp = self.head
            while temp:
                if temp.data['salary'] == highestEmployee['salary']:
                    list.append(temp.data)
                temp = temp.next
            return list

    def getAverageSalary(self):
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self.head
            sum = 0
            length = self.length()
            while temp:
                sum += temp.data['salary']
                temp = temp.next

            return f"{sum/length:.2f}"
        
    def requisiteC(self, salary):
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self.head
            count = 0        
            while temp:
                if temp.data['salary'] > salary:
                    count += 1
                temp = temp.next
            
            if count == 0:
                print("No employee has a salary higher than informed")
                return
            
            return count


