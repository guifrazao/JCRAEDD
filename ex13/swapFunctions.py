def swapNodesIterative(linked_list, key1, key2):
    if key1 == key2:
        return False

    prev1, curr1 = None, linked_list.head
    while curr1 and curr1.data != key1: # localizar o nó 1
        prev1 = curr1
        curr1 = curr1.next

    prev2, curr2 = None, linked_list.head
    while curr2 and curr2.data != key2: # localizar o nó 2
        prev2 = curr2
        curr2 = curr2.next

    if not curr1 or not curr2: # verifica se eles não são nulos
        return False

    if prev1: 
        prev1.next = curr2
    else:
        linked_list.head = curr2

    if prev2:
        prev2.next = curr1
    else:
        linked_list.head = curr1

    curr1.next, curr2.next = curr2.next, curr1.next
    return True

def swapNodesRecursive(linked_list, key1, key2, prev1=None, curr1=None, prev2=None, curr2=None):
    if not linked_list.head or key1 == key2:
        return False

    if curr1 is None:
        prev1, curr1 = None, linked_list.head
    if curr2 is None:
        prev2, curr2 = None, linked_list.head

    if curr1 and curr1.data != key1:
        return swapNodesRecursive(linked_list, key1, key2, curr1, curr1.next, prev2, curr2)
    if curr2 and curr2.data != key2:
        return swapNodesRecursive(linked_list, key1, key2, prev1, curr1, curr2, curr2.next)

    if not curr1 or not curr2:
        return False

    if prev1:
        prev1.next = curr2
    else:
        linked_list.head = curr2

    if prev2:
        prev2.next = curr1
    else:
        linked_list.head = curr1

    curr1.next, curr2.next = curr2.next, curr1.next
    return True
