"""
Enunciado
Escreva um algoritmo que receba um vetor ordenado e um número extra e insira esse
número na sua posição correta no vetor ordenado, deslocando os outros números, se
necessário. Qual é a complexidade no melhor e no pior caso deste algoritmo?
"""
import time

def inserir_nmr(vetor,num):
    i = 0
    while i < len(vetor) and vetor[i] < num:
        i += 1
    vetor.insert(i,num)
    return vetor

def medir_tempo(vetor,num):
    inicio = time.time()
    vetor_ordenado = inserir_nmr(vetor,num)
    fim = time.time()
    tempo_execucao = inicio - fim
    print(f"Tempo de execução: {tempo_execucao:.10f} segundos")
    return vetor_ordenado

vetor_teste = list(range(1, 1000001)) 
numero_para_inserir = 0
vetor_final = medir_tempo(vetor_teste, numero_para_inserir)

"""
Neste caso
Complexidade no melhor caso: O(1) 
    - O algoritmo percorre o vetor sem encontrar nenhum número maior que num. Assim fazenso apenas a verificação até o final do 
    vetor e inserindo-o diretamente.
Complexidade no pior caso: O(n) (inserção no início ou deslocamento máximo)
    - O algoritmo vai percorrer o vetor até encontrar a posição correta (ex: primeira posição). E depois disso, todos os numeros encontrados
    a direita da posição de inserção deverão ser deslocados uma posição a frente (deslocando todos os elementos)
"""
