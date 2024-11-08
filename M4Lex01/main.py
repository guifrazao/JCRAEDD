"""
1. Defina uma função length (não len) que espera uma estrutura unicamente ligada
como argumento. A função retorna o número de itens na estrutura.
"""

from unorderedLinkedList import UnorderedLinkedList
def length(linkedList: UnorderedLinkedList):
    if linkedList.isEmpty():
        return 0
    
    count = 1
    temp = linkedList.head
    while temp.next:
        count += 1
        temp = temp.next
    return count

def main():
    list = UnorderedLinkedList()
    data = ""
    while data != "0":
        data = input("Data: ")
        list.push(data)
    
    list.print()
    print(length(list))

main()
