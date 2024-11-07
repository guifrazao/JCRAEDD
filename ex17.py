'''
17. Crie uma aplicação que permita inserir cerca de 10 mil números inteiros aleatórios de 
1 a 10 mil num vetor de inteiros. Registre o tempo de início e término da operação de 
ordenação e compare essas diferenças entre os algoritmos bubbleSort, insertionSort 
e quickSort. Comente as diferenças e considere testar com números diferentes de 
elementos. Dica: quando tiver rodando os algoritmos, evite executar outros 
programas na máquina.
'''

from random import randint
import time

def create_list():
    lst = []
    for c in range(10000):
        random_number = randint(1, 10000)
        lst.append(random_number)
    return lst


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

#bubblesort = troca pares adacentes desordenados
def bubbleSort(lst):
    n = len(lst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lst[i] < lst[i - 1]:
                swap(lst, i, i - 1)
                swapped = True
            i += 1
        if not swapped: return
        n -= 1

#insertionsort = ordena dados inserindo cada elemento em sua posição correta
def insertionSort(lst):
    i = 1
    while i < len(lst):
        itemToInsert = lst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            else:
                break
        lst[j + 1] = itemToInsert
        i += 1

#quicksort = escolhe um pivô e particiona o array
def partition(lst, left, right):
    middle = (left + right) // 2
    pivot = lst[middle]
    lst[middle] = lst[right]
    lst[right] = pivot
    boundry = left
    for index in range(left, right):
        if lst[index] < pivot:
            swap(lst, index, boundry)
            boundry += 1
    swap(lst, right, boundry)
    return boundry


def quicksortHelper(lst, left, right):
    if left < right:
        pivotLocation = partition(lst, left, right)
        quicksortHelper(lst, left, pivotLocation - 1)
        quicksortHelper(lst, pivotLocation + 1, right)

def quicksort(lst):
    quicksortHelper(lst, 0, len(lst) - 1)


def main():
    random_list = create_list()
    
    # Measure time for bubbleSort
    bubble_sort_list = random_list.copy()
    start_time = time.time()
    bubbleSort(bubble_sort_list)
    end_time = time.time()
    bubble_sort_time = end_time - start_time
    
    # Measure time for insertionSort
    insertion_sort_list = random_list.copy()
    start_time = time.time()
    insertionSort(insertion_sort_list)
    end_time = time.time()
    insertion_sort_time = end_time - start_time
    
    # Measure time for quicksort
    quicksort_list = random_list.copy()
    start_time = time.time()
    quicksort(quicksort_list)
    end_time = time.time()
    quicksort_time = end_time - start_time

    print(f"Tempo de execução do bubbleSort: {bubble_sort_time} segundos")
    print(f"Tempo de execução do insertionSort: {insertion_sort_time} segundos")
    print(f"Tempo de execução do quicksort: {quicksort_time} segundos")

main()
