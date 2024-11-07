from unorderedLinkedList import UnorderedLinkedList

def intercalar(l1, l2):
    l3 = UnorderedLinkedList()
    if l1.length() != l2.length():
        print("Listas não são intercaláveis")
        return
    
    currentL1 = l1.head
    currentL2 = l2.head
    current_list = l1

    while currentL1 or currentL2:             
        if current_list == l1:
            l3.append(currentL1.data)
            currentL1 = currentL1.next
            current_list = l2
        else:
            l3.append(currentL2.data)
            currentL2 = currentL2.next
            current_list = l1
    
    l3.order()
    return l3

ull = UnorderedLinkedList()
ull.append(0)
ull.append(6)
ull.append(4)
ull.append(2)
ull.append(5)
ull.print()

ull2 = UnorderedLinkedList()
ull2.append(-5)
ull2.append(-4)
ull2.append(-3)
ull2.append(-2)
ull2.append(-1)
ull2.print()
print()

print(f"Se a primeira lista está ordenada: {ull.isOrdered()}, se a segunda lista está ordenada: {ull2.isOrdered()}")
print()

ull.order()
ull.print()
print()

ull3 = intercalar(ull, ull2)
ull3.print()