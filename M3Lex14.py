"""
Elabore um programa que armazene os seguintes dados de n pessoas: nome, idade e
sexo. O programa deve apresentar os dados em:
a. Ordem crescente alfabética de nome (use o quickSort).
b. Ordem decrescente de idade (use o bubbleSort).
"""

def swap(list, i, j):
    """Swaps the items in positions i and j"""
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def partition(list, left, right):
    middle = (left + right) // 2
    pivot = list[middle]
    list[middle] = list[right]
    list[right] = pivot
    boundary = left
    for index in range(left, right):
        if list[index][0].lower() < pivot[0].lower():  # Ordena pelo nome
            swap(list, index, boundary)
            boundary += 1
    swap(list, right, boundary)
    return boundary

def quicksortHelper(list, left, right):
    if left < right:
        pivotLocation = partition(list, left, right)
        quicksortHelper(list, left, pivotLocation-1)
        quicksortHelper(list, pivotLocation+1, right)

def quicksort(list):
    quicksortHelper(list, 0, len(list)-1)

def bubbleSortWithTweak(list):
    n = len(list)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if list[i][1] > list[i-1][1]:  # Ordena pela idade
                swap(list, i, i-1)
                swapped = True
            i += 1
        if not swapped: return  # Retorna se não há trocas
        n -= 1

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
            print("❌ Por favor, digite um número válido.")

def obter_sexo(mensagem):
    while True:
        sexo = input(mensagem).strip().upper()
        if sexo in ["M", "F"]:
            return sexo
        else:
            print("❌ Por favor, digite 'M' para masculino ou 'F' para feminino.")

def main():
    print("SISTEMA DE CADASTRO DE PESSOAS!\n")
    n = obter_numero("➡️  Digite o número de pessoas: ")
    pessoas = []

    for i in range(n):
        nome = obter_nome(f"👤 Nome da pessoa {i + 1}: ").strip()
        idade = obter_numero(f"🎂 Idade da pessoa {i + 1}: ")
        sexo = obter_sexo(f"⚥ Sexo da pessoa {i + 1} (M/F): ")
        pessoas.append((nome, idade, sexo))

    print("\n📋 Dados Originais:")
    for pessoa in pessoas:
        print(f"🔸 Nome: {pessoa[0]} | Idade: {pessoa[1]} | Sexo: {pessoa[2]}")

    while True:
        print("\n========== 📜 Menu 📜 ==========")
        print("1️⃣  Ordenar por Nome (Crescente)")
        print("2️⃣  Ordenar por Idade (Decrescente)")
        print("3️⃣  Sair")
        print("================================")
        opcao = obter_numero("➡️  Escolha uma opção: ")

        if opcao == 1:
            quicksort(pessoas)  # Assumindo que você já implementou esta função
            print("\n📋 Dados Ordenados por Nome (Crescente):")
            for pessoa in pessoas:
                print(f"🔹 Nome: {pessoa[0]} | Idade: {pessoa[1]} | Sexo: {pessoa[2]}")
        elif opcao == 2:
            bubbleSortWithTweak(pessoas)  # Assumindo que você já implementou esta função
            print("\n📋 Dados Ordenados por Idade (Decrescente):")
            for pessoa in pessoas:
                print(f"🔹 Nome: {pessoa[0]} | Idade: {pessoa[1]} | Sexo: {pessoa[2]}")
        elif opcao == 3:
            print("👋 Saindo... Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

main()
