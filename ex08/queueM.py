from node import Node

class QueueM():
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
            new_node.next = self.head # o next aponta para onde o head esta apontando
            self.head = new_node # o head vai apontar para o new_node
    
    def print(self):
        if self.isEmpty():
            print("Fila vazia.")
        else:
            temp = self.head
            while(temp):
                print(temp.data + " ",end="")
                temp = temp.next
            print()
    
    def pop(self):
        if self.isEmpty():
            print("Fila vazia.")
        else:
            penult = self.head
            last = self.head
            while (last.next):
                penult = last
                last = last.next
            penult.next = None
            self.tail = penult
        '''
        Quando o loop termina, penult está apontando para o penúltimo nó da fila, e last está apontando para o último.
        penult.next é definido como None, efetivamente removendo o último nó da fila.
        O ponteiro tail é atualizado para penult, que agora é o novo último nó da fila.
        '''
    
    def clear(self):
        if self.isEmpty():
            print("Fila vazia.")
        else:
            self.head = None
    
    # OBS: Ler = como "aponta"
    