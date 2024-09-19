"""
13. Calcule a complexidade, no pior caso, do fragmento de código abaixo:
for i in range(0,n,2):
    for j in range(n,-1,-1):
        if V[i] < V[j]:
            print(i)
"""
n = 4
v = [1, 2, 3, 4, 5, 6, 7]
for i in range(0, n, 2): #n/2 + 1
    for j in range(n, -1, -1): #n + 1
        if v[i] < v[j]:
            print(i, j)

#constantes e termos multiplicativos/divisórios não importam no pior caso. Sendo assim, a complexidade é O(n*n) = O(n²)
