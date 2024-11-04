'''
5. Faça um programa que cadastre n números, não permitindo números repetidos. 
Ordene-os e, em seguida, verifique se o número digitado pelo usuário está no vetor. 
Caso encontre, verifique se está numa posição par ou ímpar do vetor: 
a. Usando busca sequencial. 
b. Usando busca binária.
'''

def receive_list():
    input_list = []
    while True:
        num = input("Enter a number (only press enter to stop): ")
        if num == "":
            return input_list
        else:
            num = int(num)
            if num not in input_list:
                input_list.append(num)

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def selectionSort(lst):
    i = 0
    while i < len(lst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lst):
            if lst[j] < lst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lst, minIndex, i)
        i += 1
    return lst

def sequencialSearchO(target, lst):
    position = 0
    while position < len(lst) and target >= lst[position]:
        if target == lst[position]:
            return position
        position += 1
    return -1

def binarySearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

def main():
    input_list = receive_list()

    sorted_list = selectionSort(input_list)

    print(f"Ordered list: {sorted_list}")

    n = int(input("Enter the number you wish to search for: "))

    position_sequencial = sequencialSearchO(n, sorted_list)
    position_binary = binarySearch(n, sorted_list)

    if position_sequencial == position_binary == -1:
        print("Number not found")
    else:
        print(f"Index(sequencial search): {position_sequencial}")
        print(f"Index(binary search): {position_binary}")


main()
    

        