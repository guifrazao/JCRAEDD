"""
2. O método de lista reverse inverte os elementos da lista. Defina uma função chamada
reverse que inverte os elementos no argumento de lista (sem usar o método reverse).
Tente tornar essa função a mais eficiente possível e indique sua complexidade
computacional usando a notação big-O.
"""
def reverse(arr):
    comeco = 0
    fim = len(arr) - 1
    while(comeco < fim): #no pior caso, o programa roda aproximadamente n/2 vezes, ou seja, O(n)
        aux = arr[fim]
        arr[fim] = arr[comeco]
        arr[comeco] = aux
        comeco += 1
        fim -= 1
    return arr

lista = [1, 2, 3, 4, 5, 6]
print(reverse(lista))
