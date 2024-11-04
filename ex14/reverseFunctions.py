def reverseIterative(linked_list):
    prev = None
    current = linked_list.head
    linked_list.tail = current
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def reverseRecursive(linked_list):
    def _reverseRecursive(current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev
        return _reverseRecursive(next_node, current)

    linked_list.tail = linked_list.head
    linked_list.head = _reverseRecursive(linked_list.head, None)
