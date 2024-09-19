"""
Enunciado:
Do fragmento de código abaixo, determine a complexidade:
for i=0 to n-1:
    for j=0 to n-1:
        mat[i][j] = 0
        for k=0 to n-1:
            mat[i][j] += A[i][k] * B[k][j]
"""

#for i=0 to n-1:
#    for j=0 to n-1:
#        mat[i][j] = 0
#        for k=0 to n-1:
#            mat[i][j] += A[i][k] * B[k][j]


"""A complexidade deste fragmento de código é O(n³)
Esse código é uma implementação de uma multiplicação de duas matrizes, podemos analisar a complexidade dele pelo número de loops alinhados
1° O primeiro loop ( variavel i) executa i=0 até n-1, desse modo, faz n iterações
2° O segundo loop (veriavel j) assim como i, executa j=0 até n-1, desse modo, faz n iterações
3° O terceiro loop (variavel K) para cada combinação de i e j, faz n iterações"""