'''10. Faça um programa que apresente o menu de opções abaixo:
MENU
1- Cadastrar aluno
2- Cadastrar nota
3- Calcular média de um aluno
4- Listar os nomes dos alunos sem notas
5- Excluir aluno
6- Excluir nota
7- Sair
Observações:
a. Na opção 1, deve ser cadastrado um aluno (número e nome) de cada vez em
uma pilha. A mensagem disponível nesta opção é: Aluno cadastrado. Os
números dos alunos devem ser gerados automaticamente, partindo do no 1.
b. Na opção 2, deve ser cadastrada uma nota (número do aluno e nota) em uma
fila. Uma nota só pode ser cadastrada se pertencer a um aluno cadastrado na
pilha de alunos. As mensagens disponíveis nessa opção são: Nota cadastrada
e Aluno não cadastrado. Cada aluno pode ter várias notas cadastradas.
c. Na opção 3, o usuário deve digitar o número de um aluno e o programa deve
mostrar o nome dele e a média aritmética das notas desse aluno. As
mensagens disponíveis nessa opção são: Aluno não cadastrado, Aluno sem
notas e Média do aluno = valor calculado.
d. Na opção 4, os nomes dos alunos que não possuem notas devem ser listados.
As mensagens disponíveis nesta opção são: A listagem dos nomes sem nota e
Todos os alunos possuem notas.
e. Na opção 5, um aluno da pilha de alunos de alunos deve ser excluído,
respeitando duas regras: (i) um aluno só pode ser excluído se não possuir
notas; e (ii) o usuário não deve escolher o aluno a ser excluído, pois a
exclusão deve obedecer à lógica da pilha. As mensagens são: Aluno excluído,
Pilha vazia e Este aluno possui notas, logo, não poderá ser excluído.
f. Na opção 6, uma nota deve ser excluída, respeitando as regras de
funcionamento da fila. As mensagens disponíveis são: Nota excluída e Fila
vazia.
g. A opção 7 é a única que sai do programa. Uma mensagem deve ser mostrada
para opções inválidas.'''

from studentStack import StudentStack
from gradeQueue import GradeQueue

def menu():
    print("MENU")
    print("1- Cadastrar aluno")
    print("2- Cadastrar nota")
    print("3- Calcular média de um aluno")
    print("4- Listar os nomes dos alunos sem notas")
    print("5- Excluir aluno")
    print("6- Excluir nota")
    print("7- Sair")

    option = input("Escolha uma opção: ")
    print("-"*60)
    return option


def main():
    global students
    students = StudentStack()
    grades = GradeQueue()

    while True:
        option = menu()

        if option == "1":
            name = input("Insira o nome do aluno: ")
            students.push(name)
            print("Aluno cadastrado")
            print("-"*60)
        elif option == "2":
            grade = float(input("Insira a nota: "))
            number = int(input("Insira o número do aluno: "))

            if students.findStudent(number):
                grades.push(grade, number)
                print("Nota cadastrada")
            else:
                print("Aluno não cadastrado")

        elif option == "3":
            number = int(input("Insira o número do aluno: "))
            if students.findStudent(number):
                student = students.findStudent(number)
                grade = grades.gradeFind(number)
                if len(grade) == 0:
                    print("Aluno sem nota")
                else:
                    print(f"Nome: {student.name}")
                    print(f"Média: {sum(grade)/len(grade)}")
            else:
                print("Aluno não cadastrado")

        elif option == "4":
            studentsWithGrades = grades.gradesList()
            studentsWithOutGrade = students.checkGrade(studentsWithGrades)

            if len(studentsWithOutGrade) > 0:
                for i in studentsWithOutGrade:
                    print(i.name)
            else:
                print("Todos os alunos possuem notas")
        elif option == "5":
            studentsWithGrades = grades.gradesList()

            if students.isEmpty():
                print("Pilha vazia")
            elif not students.lastStudent() in studentsWithGrades:
                students.pop()
                print("Aluno excluído")
            else:
                print("Este aluno possui notas, logo, não poderá ser excluído.")
        elif option == "6":
            grades.pop()
            print("Nota excluída")
        elif option == "7":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida")
main()  