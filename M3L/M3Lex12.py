"""
12. Desenvolva uma aplicação que, dados dois vetores de inteiros quaisquer com
tamanho de 20 elementos, gere um terceiro com os elementos de ambos em ordem
crescente, usando o mergeSort. Apresente o resultado final.
"""
import random
from modules import mergeSort

arr1 = []
arr2 = []
for i in range(0, 20):
    arr1.append(random.randint(0, 21))
    arr2.append(random.randint(0, 21))

arr3 = arr1 + arr2
mergeSort(arr3)
print(arr3)

