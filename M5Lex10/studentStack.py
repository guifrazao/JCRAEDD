from student import Student

class StudentStack:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = tail
        self.studentAmount = 1


    def isEmpty(self):
        return self.head == None

    def push(self, studentName):
        newStudent = Student(studentName, self.studentAmount)
        if self.isEmpty():
            self.head = newStudent
            self.tail = newStudent
        else:
            newStudent.next = self.head
            self.head = newStudent

        self.studentAmount += 1

    def findStudent(self, studentNumber):
        temp = self.head

        while temp:
            if temp.number == studentNumber:
                return temp
            temp = temp.next

        return None
    
    def checkGrade(self, studentList):
        temp = self.head
        studentsWithOutGrade = []

        while temp:
            if not temp.number in studentList:
                studentsWithOutGrade.append(temp)
            temp = temp.next
        return studentsWithOutGrade
    
    def pop(self):
        if self.is_empty():
            print("A pilha está vazia.")
            return None
        self.head = self.head.next

    def lastStudent(self):
        return self.tail