def pesquisaBR_estruturado(target, sortedList):
    count = 1
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        mid = (left+right)//2
        if target == sortedList[mid]:
            return mid, count
        elif target < sortedList[mid]:
            right = mid - 1
        else:
            left = mid + 1
        count += 1
    return -1, count