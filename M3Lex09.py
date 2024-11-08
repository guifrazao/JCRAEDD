"""
Faça um programa que cadastre o nome e o salário de n funcionários. Usando um
método de ordenação diferente para cada item a seguir, liste todos os dados dos
funcionários das seguintes formas:
a. Em ordem crescente de salário;  ----- (insertionSort)
b. Em ordem decrescente de salário;  --- (selectionSort)
c. Em ordem alfabética.  --------------- (quicksort)
"""

def swap(list, i, j):
    """Troca os itens nas posições i e j."""
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def selectionSort(list):
    # Ordenação por salário em ordem decrescente
    for i in range(len(list)):
        maxIndex = i
        for j in range(i + 1, len(list)):
            if list[j][1] > list[maxIndex][1]:  # Ordena por salário (decrescente)
                maxIndex = j
        if maxIndex != i:
            swap(list, i, maxIndex)

def insertionSort(list):
    # Ordenação por salário em ordem crescente
    for i in range(1, len(list)):
        itemToInsert = list[i]
        j = i - 1
        while j >= 0 and list[j][1] > itemToInsert[1]:  # Ordena por salário (crescente)
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = itemToInsert

def partition(list, left, right):
    # Função auxiliar para o quicksort: ordenação por nome em ordem alfabética
    pivot = list[right]
    i = left - 1
    for j in range(left, right):
        if list[j][0].lower() < pivot[0].lower():  # Ordena por nome (alfabética)
            i += 1
            swap(list, i, j)
    swap(list, i + 1, right)
    return i + 1

def quicksortHelper(list, left, right):
    if left < right:
        pivotIndex = partition(list, left, right)
        quicksortHelper(list, left, pivotIndex - 1)
        quicksortHelper(list, pivotIndex + 1, right)

def quicksort(list):
    quicksortHelper(list, 0, len(list) - 1)

# Funções de entrada seguem como no código original


def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 3 and not nome.replace('.', '', 1).isdigit():
            return nome
        else:
            print("❌ Nome inválido! O nome deve ter pelo menos 3 caracteres e não pode ser um número.")

def obter_numero(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("❌ Erro! Por favor, digite um número válido.")

def obter_salario(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
                break
            else:
                print("❌ Erro! Por favor, digite um salário válido.")
        except ValueError:
            print("❌ Erro! Por favor, digite um salário válido.")

def main():
    print("SISTEMA DE CADASTRO DE FUNCIONÁRIOS!\n")
    n = obter_numero("➡️  Digite o número de funcionários: ")
    funcionarios = []

    for i in range(n):
        nome = obter_nome(f"👤 Nome do funcionário {i + 1}: ")
        salario = obter_salario(f"💰 Salário do funcionário {i + 1}: R$")
        funcionarios.append((nome, salario))

    print("\n📋 Dados Originais:")
    for funcionario in funcionarios:
        print(f"🔸 Nome: {funcionario[0]}, Salário: R${funcionario[1]:.2f}")

    while True:
        print("\n========== 📜 Menu 📜 ==========")
        print("1️⃣  Ordenar por Salário (Crescente)")
        print("2️⃣  Ordenar por Salário (Decrescente)")
        print("3️⃣  Ordenar por Nome (Alfabética)")
        print("4️⃣  Sair")
        print("================================")
        opcao = obter_numero("➡️  Escolha uma opção: ")

        if opcao == 1:
            insertionSort(funcionarios)
            print("\n📋 Dados Ordenados por Salário (Crescente):")
            for funcionario in funcionarios:
                print(f"🔹 Nome: {funcionario[0]}, Salário: R${funcionario[1]:.2f}")
        elif opcao == 2:
            selectionSort(funcionarios)
            print("\n📋 Dados Ordenados por Salário (Decrescente):")
            for funcionario in funcionarios:
                print(f"🔹 Nome: {funcionario[0]}, Salário: R${funcionario[1]:.2f}")
        elif opcao == 3:
            quicksort(funcionarios)
            print("\n📋 Dados Ordenados por Nome (Alfabética):")
            for funcionario in funcionarios:
                print(f"🔹 Nome: {funcionario[0]}, Salário: R${funcionario[1]:.2f}")
        elif opcao == 4:
            print("👋 Saindo... Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

main()
