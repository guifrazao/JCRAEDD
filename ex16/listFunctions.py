from node import Node

def remove_node_iterative(linked_list, p):
    if linked_list.isEmpty() or p is None or p.next == linked_list.head:
        return False

    next_node = p.next
    p.next = next_node.next
    next_node.next.previous = p

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
    if linked_list.isEmpty() or p is None or p.next == linked_list.head:
        return False

    next_node = p.next
    p.next = next_node.next
    next_node.next.previous = p

    if next_node == linked_list.head:
        linked_list.head = p.next

    return True

def insert_after_node_recursive(linked_list, p, x):
    if linked_list.isEmpty() or p is None:
        return False

    new_node = Node(x)
    new_node.next = p.next
    new_node.previous = p
    p.next.previous = new_node
    p.next = new_node

    return True
