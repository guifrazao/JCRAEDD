def pesquisaLR_estruturado(target, list):
    position = 0
    count = 1
    while position < len(list):
        if target == list[position]:
            return position, count
        position += 1
        count += 1
    return -1, count