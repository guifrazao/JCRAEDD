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
