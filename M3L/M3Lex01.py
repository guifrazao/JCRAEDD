def pesquisaLR_estruturado(target, list):
    position = 0
    while position < len(list):
        if target == list[position]:
            return position
        position += 1
    return -1

def pesquisaLR_recursao(target, list):
    position = len(list) - 1
    if position < 1:
        return -1
    if target == list[position]:
        return position
    return pesquisaLR_recursao(target, list[0:position:1])

lista = [5, 3, 1, 8, 2]

normal = pesquisaLR_estruturado(8, lista)
recursivo = pesquisaLR_recursao(2, lista)

print(normal, recursivo)