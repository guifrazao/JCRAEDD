"""
11. Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados:
nome, nota1 e nota2. Primeiro, liste todos os alunos cadastrados, ordenando-os pela
média ponderada das notas, tendo a primeira nota peso 2 e a segunda, peso 3. Em
seguida, ordene os alunos, de forma crescente, pela nota1, e liste-os. Finalmente,
considerando que, para ser aprovado, o aluno deve ter no mínimo média 7, liste, em
ordem alfabética, os alunos reprovados. Em cada ordenação use um algoritmo
diferente.
"""
from quickSort import quicksort
from mergeSort import mergeSort
from insertionSort import insertionSort
def cadastro():
    lista_alunos = []
    cadastrar = True
    while cadastrar:
        try:
            aluno = []

            nome = input("Informe o nome do aluno: ")
            nota1 = float(input("Informe a 1° nota do aluno: "))
            if nota1 < 0 or nota1 > 10:
                raise Exception("nota inválida")
            nota2 = float(input("Informe a 2° nota do aluno: "))
            if nota2 < 0 or nota2 > 10:
                raise Exception("nota inválida")

            aluno.append(nome)
            aluno.append(nota1)
            aluno.append(nota2)
            lista_alunos.append(aluno)

            cadastrar = True if input("Deseja continuar cadastrando alunos? [s/n]: ").lower() == "s" else False
        except Exception as e:
            print(f"Erro: {e}, tente novamente")
    
    return lista_alunos

def ordenarMediaPond(lista):
    PESO1, PESO2 = 2, 3
    for aluno in lista:
        media_pond = ((aluno[1] * PESO1) + aluno[2] * PESO2)/(PESO1+PESO2)
        aluno.insert(0, media_pond) 
    quicksort(lista)    

    for aluno in lista:
        aluno.append(aluno[0])
        aluno.remove(aluno[0]) #remove a primeira instância do parâmetro na lista

    return lista[::-1] #lista está crescente e deve estar decrescente, por isso o retorno ao contrário

def ordenarNota1(lista):
    for aluno in lista:
        aluno.insert(0, aluno[1]) #aluno[1] = nota1
    mergeSort(lista)

    for aluno in lista:
        aluno.remove(aluno[0])

    return lista

def ordenarAlfabetico(lista): #primeiro elemento da lista (elemento que o algoritmo ordena) já é o nome, não é necessário mover o elemento para o começo
    insertionSort(lista)
    return lista
    
lista_alunos = cadastro()
print(lista_alunos)

lista_temp = lista_alunos.copy()
ord_media_pond = ordenarMediaPond(lista_temp)
print(ord_media_pond)

lista_temp = lista_alunos.copy()
ord_nota_1 = ordenarNota1(lista_temp)
print(ord_nota_1)

reprovados = [aluno for aluno in lista_alunos if aluno[1] < 7]
ord_alfabetico = ordenarAlfabetico(reprovados)
print(ord_alfabetico)

    