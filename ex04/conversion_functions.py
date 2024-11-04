from doubly_circular_linked_list import DoublyCircularLinkedUnorderedList

def makeTwoWay(linked_list):
    new_list = DoublyCircularLinkedUnorderedList()
    current = linked_list.head

    while current:
        new_list.insert_end(current.data)
        current = current.next

    return new_list
