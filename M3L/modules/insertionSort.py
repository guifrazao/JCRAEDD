def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def insertionSort(list):
    i = 1
    while i < len(list):
        itemToInsert = list[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < list[j]:
                list[j + 1] = list[j]
                j -= 1
            else:
                break
        list[j + 1] = itemToInsert
        i += 1