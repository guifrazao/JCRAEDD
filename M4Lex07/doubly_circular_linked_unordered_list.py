from node import Node

class DoublyCircularLinkedUnorderedList:
    """Classe para lista duplamente encadeada não ordenada."""
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert_end(self, new_data):
        """Função para inserir um nó no final da lista."""
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

    def show_approved(self):
        """Exibe apenas os alunos aprovados (nota ≥ 7)."""
        if self.isEmpty():
            print("A lista está vazia!")
            return
        current = self.head
        approved = False
        while True:
            if current.data[1] >= 7:
                print(f"{current.data[0]}")
                approved = True
            current = current.next
            if current == self.head:
                break
        if not approved:
            print("Nenhum aluno aprovado.")
