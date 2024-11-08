from grade import Grade

class GradeQueue:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = tail

    def isEmpty(self):
        return self.head == None
    
    def push(self, grade, number):
        newGrade = Grade(grade, number)

        if self.isEmpty():
            self.head = newGrade
            self.tail = newGrade
        else:
            newGrade.next = self.head
            self.head = newGrade

    def gradeFind(self, number):
        grades = []
        temp = self.head

        while temp:
            if temp.number == number:
                grades.append(temp.data)
            temp = temp.next
        
        return grades

    def gradesList(self):
        temp = self.head
        students = []
        while temp:
            if not temp.data in students:
                students.append(temp.number)
            temp = temp.next
        return students
    
    def pop(self):
        if self.isEmpty():
            print("Fila vazia")
        else:
            penult = self.head
            last = self.head
            while last.next:
                penult = last
                last = last.next
            penult.next = None
            self.tail = penult