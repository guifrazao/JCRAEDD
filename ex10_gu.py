'''
10. Do fragmento de código abaixo, determine a complexidade:

for i=0 to n-2:
    for j=i+1 to n-1:
        for k=1 to j-1:
            s=1

'''

import time
import matplotlib.pyplot as plt

# Função que contém os loops aninhados
def nested_loops(n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            for k in range(1, j):
                s = 1  # Operação simples dentro do loop

# Complexidade Explicada:

# O(n) (para i) × O(n) (para j) × O(n) (para k) = O(n³)

# O 1º loop executa n-1 vezes.
# O 2º loop para cada i executa de i+1 até n-1, ou seja, diminui conforme i aumenta.
# O 3º loop executa j-1 vezes, onde j depende de i.
# A complexidade geral é O(n^3) porque o número de iterações cresce rapidamente conforme n aumenta.

# n = 5
# 1º loop (i) executa 4 vezes (n-1).
# 2º loop (j) para i=0 executa de 1 até 4 (4 iterações).
# 3º loop (k) para cada j executa (j-1) vezes.
# Total de iterações: 20
# Fórmula: (1) + (2) + (3) + (1) + (2) + (3) + (2) + (3) + (3)

# O(n) (para i) × O(n) (para j) × O(n) (para k) = O(n³)
# Complexidade do algoritmo: O(n^3)

# Testando a função com diferentes valores de n

# Função para medir o tempo de execução
def measure_execution_time(n_values):
    times = []
    for n in n_values:
        start_time = time.time()  # Marca o início do tempo
        nested_loops(n)           # Executa a função
        end_time = time.time()    # Marca o fim do tempo
        times.append(end_time - start_time)  # Calcula o tempo total
    return times

# Definindo os valores de n que queremos testar
n_values = [75,150,300,600,1200]

# Medindo o tempo de execução para cada valor de n
execution_times = measure_execution_time(n_values)

for n, t in zip(n_values, execution_times):
    print(f"n = {n}: tempo de execução = {t:.6f} segundos")
