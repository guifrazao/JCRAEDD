from modules import quicksort
def cadastro():
    lista_alunos = []
    cadastrar = True
    while cadastrar:
        try:
            aluno = []

            nome = input("Informe o nome do aluno: ")
            nota1 = float(input("Informe a 1° nota do aluno: "))
            nota2 = float(input("Informe a 2° nota do aluno: "))

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
    return lista
    
lista_alunos = cadastro()
lista_temp = lista_alunos.copy()
teste = ordenarMediaPond(lista_temp)
print(teste)
print(lista_alunos)
    