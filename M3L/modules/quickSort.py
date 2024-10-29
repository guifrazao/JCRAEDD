def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def partition(list, left, right):
    mid = (left+right)//2
    pivot = list[mid]
    list[mid] = list[right]
    list[right] = pivot
    boundary = left
    for i in range(left, right):
        if list[i] < pivot:
            swap(list, i, boundary)
            boundary += 1
    swap(list, right, boundary)
    return boundary

def quickSortHelper(list, left, right):
    if left < right:
        pivotLocation = partition(list, left, right)
        quickSortHelper(list, left, pivotLocation - 1)
        quickSortHelper(list, pivotLocation + 1, right)

def quicksort(list):
    quickSortHelper(list, 0, len(list) - 1)