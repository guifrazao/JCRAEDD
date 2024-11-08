from doubly_circular_linked_unordered_list import DoublyCircularLinkedUnorderedList

def main():
    print("### Sistema de Cadastro de Alunos ###\n")
    
    # Criando a lista de alunos
    my_list = DoublyCircularLinkedUnorderedList()

    # Perguntar quantos alunos o usuário quer adicionar
    num_students = int(input("Quantos alunos você quer cadastrar? "))
    
    for _ in range(num_students):
        name = input("Digite o nome do aluno: ")
        grade = float(input("Digite a nota final do aluno: "))
        my_list.insert_end((name, grade))
        print("=-"*30)
    
    # Exibir apenas os alunos aprovados
    print("\n### Alunos Aprovados ###")
    my_list.show_approved()

main()

