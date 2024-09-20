"""
Enunciado
Escreva um algoritmo que receba um vetor ordenado e um número extra e insira esse
número na sua posição correta no vetor ordenado, deslocando os outros números, se
necessário. Qual é a complexidade no melhor e no pior caso deste algoritmo?
"""

def inserir_nmr(vetor,num):
    i = 0
    while i < len(vetor) and vetor[i] < num:
        i += 1
    vetor.insert(i,num)
    return vetor

"""
Neste caso
Complexidade no melhor caso: O(1) 
    - O algoritmo percorre o vetor sem encontrar nenhum número maior que num. Assim fazenso apenas a verificação até o final do 
    vetor e inserindo-o diretamente.
Complexidade no pior caso: O(n) (inserção no início ou deslocamento máximo)
    - O algoritmo vai percorrer o vetor até encontrar a posição correta (ex: primeira posição). E depois disso, todos os numeros encontrados
    a direita da posição de inserção deverão ser deslocados uma posição a frente (deslocando todos os elementos)
"""
