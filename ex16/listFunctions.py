from node import Node

def remove_node_iterative(linked_list, p):
    if linked_list.isEmpty() or p is None or p.next == linked_list.head:
        return False

    next_node = p.next
    p.next = next_node.next
    (next_node.next).previous = p

    if next_node == linked_list.head:
        linked_list.head = p.next

    return True

def insert_after_node_iterative(linked_list, p, x):
    if linked_list.isEmpty() or p is None:
        return False

    new_node = Node(x)
    new_node.next = p.next
    new_node.previous = p
    p.next.previous = new_node
    p.next = new_node

    return True

def remove_node_recursive(linked_list, p):
    if linked_list.isEmpty():
        return False  

    def _remove_node_recursive(current, p):
        if current is None:
            return False  

        if current.data == p and current.next:
            node_to_remove = current.next
            current.next = node_to_remove.next
            if node_to_remove.next:
                node_to_remove.next.previous = current
            return True

        return _remove_node_recursive(current.next, p)

    return _remove_node_recursive(linked_list.head, p)

def insert_after_node_recursive(linked_list, p, x):
    if linked_list.isEmpty():
        return False  

    def _insert_after_node_recursive(current):
        if current is None:
            return False  

        if current.data == p:
            new_node = Node(x)
            new_node.next = current.next
        
            if current.next is not None:
                current.next.previous = new_node
            current.next = new_node
            return True

        return _insert_after_node_recursive(current.next)

    return _insert_after_node_recursive(linked_list.head)
