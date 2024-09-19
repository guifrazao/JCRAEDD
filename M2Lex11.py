s = 0
n = 3
for i in range(n-2): #n-1
    for j in range(2*n): #2*n + 1, + 1 devido à falha
        s = s + 1

#(n-1)*(2n+1) = 2n² + n - 2n -1. No pior caso, as constantes e termos multiplicativos não são relevantes -> n² - n = O(n²)
print(s)