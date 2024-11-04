'''
18. Crie uma aplicação que permita inserir cerca de 8 mil números inteiros aleatórios de 1 a 8 mil num vetor de inteiros. Faça um comparativo considerando o número de trocas 
realizadas entre os algoritmos selectionSort, mergeSort e quickSort. Comente as 
diferenças e considere testar com números diferentes de elementos. Dica: quando 
tiver rodando os algoritmos, evite executar outros programas na máquina.
'''

from random import randint

def create_list():
    lst = []
    for c in range(8000):
        random_number = randint(1, 8000)
        lst.append(random_number)
    return lst

def swap(lst, i, j, counter):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    counter[0] += 1

# selectionSort
def selectionSort(lst):
    counter = [0]
    i = 0
    while i < len(lst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lst):
            if lst[j] < lst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lst, minIndex, i, counter)
        i += 1
    return counter[0]

# mergeSort
def merge(lst, copyBuffer, low, middle, high, counter):
    i1 = low
    i2 = middle + 1
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lst[i1]
            i1 += 1
        elif lst[i1] < lst[i2]:
            copyBuffer[i] = lst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lst[i2]
            i2 += 1
    for i in range(low, high + 1):
        lst[i] = copyBuffer[i]

def mergeSortHelper(lst, copyBuffer, low, high, counter):
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lst, copyBuffer, low, middle, counter)
        mergeSortHelper(lst, copyBuffer, middle + 1, high, counter)
        merge(lst, copyBuffer, low, middle, high, counter)

def mergeSort(lst):
    counter = [0] # Note: Merge sort doesn't use swaps in the traditional sense
    copyBuffer = [0]*(len(lst))
    mergeSortHelper(lst, copyBuffer, 0, len(lst) - 1, counter)
    return counter[0]

# quickSort
def partition(lst, left, right, counter):
    middle = (left + right) // 2
    pivot = lst[middle]
    lst[middle] = lst[right]
    lst[right] = pivot
    counter[0] += 1  # counting the swap
    boundry = left
    for index in range(left, right):
        if lst[index] < pivot:
            swap(lst, index, boundry, counter)
            boundry += 1
    swap(lst, right, boundry, counter)
    return boundry

def quicksortHelper(lst, left, right, counter):
    if left < right:
        pivotLocation = partition(lst, left, right, counter)
        quicksortHelper(lst, left, pivotLocation - 1, counter)
        quicksortHelper(lst, pivotLocation + 1, right, counter)

def quicksort(lst):
    counter = [0]
    quicksortHelper(lst, 0, len(lst) - 1, counter)
    return counter[0]

def main():
    random_list = create_list()
    
    selection_sort_list = random_list.copy()
    selection_sort_swaps = selectionSort(selection_sort_list)
    
    merge_sort_list = random_list.copy()
    merge_sort_swaps = mergeSort(merge_sort_list)
    
    quick_sort_list = random_list.copy()
    quick_sort_swaps = quicksort(quick_sort_list)

    print(f"Número de trocas no selectionSort: {selection_sort_swaps}")
    print(f"Número de trocas no mergeSort: {merge_sort_swaps}")
    print(f"Número de trocas no quickSort: {quick_sort_swaps}")

main()
