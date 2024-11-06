def common_elements(queue, stack):
    if queue and stack:
        queue_elements = set()
        stack_elements = set()
        temp = queue.head
        while temp:
            queue_elements.add(temp.data)
            temp = temp.next
        temp = stack.head
        while temp:
            stack_elements.add(temp.data)
            temp = temp.next
        return queue_elements.intersection(stack_elements)
    else:
        print("Ambas as estruturas devem ser criadas primeiro.")
        return None

def only_in_queue(queue, stack):
    if queue:
        queue_elements = set()
        stack_elements = set()
        temp = queue.head
        while temp:
            queue_elements.add(temp.data)
            temp = temp.next
        temp = stack.head
        while temp:
            stack_elements.add(temp.data)
            temp = temp.next
        return queue_elements - stack_elements
    else:
        print("A fila deve ser criada primeiro.")
        return None

def only_in_stack(queue, stack):
    if stack:
        queue_elements = set()
        stack_elements = set()
        temp = queue.head
        while temp:
            queue_elements.add(temp.data)
            temp = temp.next
        temp = stack.head
        while temp:
            stack_elements.add(temp.data)
            temp = temp.next
        return stack_elements - queue_elements
    else:
        print("A pilha deve ser criada primeiro.")
        return None
