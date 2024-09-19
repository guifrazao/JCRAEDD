'''Escreva um algoritmo que receba valores em um vetor e imprima “ORDENADO” se o
vetor estiver em ordem crescente. Qual é a complexidade deste seu algoritmo?'''

def verificar_ordem(vetor):
    for i in range(1, len(vetor)):
        if vetor[i] < vetor[i - 1]:
            print("NÃO ORDENADO")
            return
    print("ORDENADO")

# Exemplo de uso:
vetor = [1, 2, 3, 4, 5]
verificar_ordem(vetor)  # Saída: ORDENADO

vetor = [1, 3, 2, 4, 5]
verificar_ordem(vetor)  # Saída: NÃO ORDENADO

# Operações críticas: A operação crítica é a comparação entre vetor[i] e vetor[i-1] em cada iteração.

# Número de iterações: O loop percorre o vetor inteiro, realizando n-1 comparações, onde n é o tamanho do vetor.

# Como o número de comparações é proporcional ao tamanho do vetor, a complexidade é O(n).

