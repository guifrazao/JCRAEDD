import time
import random
import matplotlib.pyplot as plt

''' 
Dada a função abaixo, determine a complexidade:
def ache_min(array, n):
    min = array[0]

    for i=0 to n-1:
        if array[i] < min:
            min = array[i]
return min

'''

def ache_min(array, n):
    min_val = array[0]
    for i in range(n):
        if array[i] < min_val:
            min_val = array[i]
    return min_val

# Tabela de Complexidade - Função ache_min

# | Etapa          | Descrição                                                      | Complexidade |
# |----------------|------------------------------------------------------------------- |--------------|
# | Inicialização  |'min_val' é inicializada com o primeiro elemento do array.          | O(1)         |
# | Laço for       | O laço percorre o array do índice 0 até n-1 (n elementos no total).| O(n)         |
# | Comparação     | Em cada iteração, compara o valor atual do array com 'min_val'.    | O(1)         |
# | Atribuição (se menor)| Se um valor menor for encontrado, 'min_val' é atualizado.    | O(1)         |
# | Retorno       | Retorna o valor mínimo encontrado.                                  | O(1)         |

# Complexidade Total: O(n)

# Função para testar a complexidade
def testar_complexidade():
    tamanhos = [500000, 1000000, 5000000, 10000000, 20000000, 40000000, 80000000]  # Diferentes tamanhos de arrays
    tempos = []  # Lista para armazenar os tempos de execução
    for tamanho in tamanhos:
        # Gerar um array aleatório de tamanho 'tamanho'
        array = [random.randint(1, 1000000) for _ in range(tamanho)]
        
        # Medir o tempo de execução
        inicio = time.time()
        ache_min(array, len(array))
        fim = time.time()
        
        # Exibir o tempo de execução
        print(f"Tamanho do array: {tamanho}, Tempo de execução: {fim - inicio:.6f} segundos")

        tempos.append(fim - inicio)

    # Plotar o gráfico
    plt.plot(tamanhos, tempos, marker='o')
    plt.title('Complexidade Temporal da Função ache_min')
    plt.xlabel('Tamanho do Array (n)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.grid(True)
    plt.show()

def main():
    testar_complexidade()

main()
