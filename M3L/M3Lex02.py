"""
2. Implemente um programa estruturado e recursivo para pesquisa binária. Faça uma
função de busca chamada pesquisaBR que receba como parâmetro o valor a ser
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1,
caso não encontre o item, ou retornará o índice, caso o encontre.
"""

def pesquisaBR_estruturado(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        mid = (left+right)//2
        if target == sortedList[mid]:
            return mid
        elif target < sortedList[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def pesquisaBR_recursiva(target, left, right, sortedList):
    if left > right:
        return -1
    mid = (right+left)//2
    if target == sortedList[mid]:
        return mid
    elif target < sortedList[mid]:
        return pesquisaBR_recursiva(target, left,  mid - 1, sortedList)
    else:
        return pesquisaBR_recursiva(target, mid + 1, right, sortedList)
   
lista = [1, 2, 3, 5, 8]

normal = pesquisaBR_estruturado(3, lista)
recursivo = pesquisaBR_recursiva(3, 0, len(lista)-1, lista)

print(normal, recursivo)


