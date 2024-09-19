"""
11. Calcule a complexidade, no pior caso, do fragmento de código abaixo:
s = 0
for i=0 to n-2:
    for j=1 to 2*N:
        s = s+1
"""
s = 0
n = 3
for i in range(n-2): #n-1, +1 devido à falha
    for j in range(2*n): #2*n, + 1 devido à falha e -1 já que j = 1
        s = s + 1

#(n-1)*(2n) = 2n² - n. No pior caso, as constantes e termos multiplicativos não são relevantes -> n² - n ~= O(n²)
print(s)
