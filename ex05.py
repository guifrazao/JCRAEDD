def tem_duplicacao(array, n):
    for i in range(0, n): 
        val = array[i]
        for j in range(i + 1, n):  
            if array[i] == val:
                return True
    return False

print(tem_duplicacao([1,2,3,4,5], 5))
'''
Combinação Simples: O(n) = n * (n-1) / 2 -> O(n²)
'''
