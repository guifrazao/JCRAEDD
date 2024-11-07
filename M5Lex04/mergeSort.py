def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def merge(list, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle + 1

    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = list[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = list[i1]
            i1 += 1
        elif list[i1] < list[i2]:
            copyBuffer[i] = list[i1]
            i1 += 1
        else:
            copyBuffer[i] = list[i2]
            i2 += 1
    for i in range(low, high + 1):
        list[i] = copyBuffer[i]

def mergeSortHelper(list, copyBuffer, low, high):
    if low < high:
        middle = (low+high)//2
        mergeSortHelper(list, copyBuffer, low, middle)
        mergeSortHelper(list, copyBuffer, middle+1, high)
        merge(list, copyBuffer, low, middle, high)

def mergeSort(list):
    copyBuffer = [0] * (len(list))
    mergeSortHelper(list, copyBuffer, 0, len(list)-1)