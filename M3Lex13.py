"""
13. Crie uma aplicação que implemente uma matriz quadrada com n números inteiros, os
quais devem ser fornecidos aleatoriamente pelo usuário. Implemente um menu com
duas opções:
a. Colocar os elementos em ordem crescente (use o insertionSort).
b. Colocar os elementos em ordem decrescente (use o selectionSort).
"""

def gerar_matriz_quadrada_usuario(n):
    """Recebe os elementos da matriz quadrada n x n do usuário."""
    matriz = []
    print(f"\n🔢 Digite os elementos da matriz {n}x{n}:")
    for i in range(n):
        linha = []
        for j in range(n):
            while True:
                try:
                    elemento = int(input(f"  ➤ Elemento [{i+1}][{j+1}]: "))
                    linha.append(elemento)
                    break
                except ValueError:
                    print("    ❗ Por favor, digite um número inteiro válido.")
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    """Exibe a matriz em formato de matriz quadrada."""
    print("\n🟦 Matriz Atual:")
    for linha in matriz:
        print("    " + " ".join(f"{num:3}" for num in linha))
    print()

def matriz_para_lista(matriz):
    """Converte uma matriz para uma lista para facilitar a ordenação."""
    return [elemento for linha in matriz for elemento in linha]

def lista_para_matriz(lista, n):
    """Converte uma lista de volta para uma matriz quadrada n x n."""
    return [lista[i*n:(i+1)*n] for i in range(n)]

def swap(lista, i, j):
    """Troca os itens nas posições i e j."""
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp

def selectionSort(lista):
    """Ordena a lista em ordem decrescente usando o Selection Sort."""
    i = 0
    while i < len(lista) - 1:
        maxIndex = i
        j = i + 1
        while j < len(lista):
            if lista[j] > lista[maxIndex]:
                maxIndex = j
            j += 1
        if maxIndex != i:
            swap(lista, maxIndex, i)
        i += 1

def insertionSort(lista):
    """Ordena a lista em ordem crescente usando o Insertion Sort."""
    i = 1
    while i < len(lista):
        itemToInsert = lista[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = itemToInsert
        i += 1

def menu():
    print("🎲 Bem-vindo ao Organizador de Matrizes 🎲\n")
    n = int(input("🔹 Digite o tamanho da matriz quadrada (n x n): "))
    matriz = gerar_matriz_quadrada_usuario(n)  # Usa a função para receber entrada do usuário
    print("✅ Matriz inicial fornecida:")
    exibir_matriz(matriz)

    while True:
        print("📋 Menu de Opções:")
        print("  1️⃣  Ordenar elementos em ordem crescente (insertionSort)")
        print("  2️⃣  Ordenar elementos em ordem decrescente (selectionSort)")
        print("  3️⃣  Sair")
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == '1':
            lista = matriz_para_lista(matriz)
            insertionSort(lista)
            matriz = lista_para_matriz(lista, n)
            print("🔼 Matriz em ordem crescente:")
            exibir_matriz(matriz)
        elif opcao == '2':
            lista = matriz_para_lista(matriz)
            selectionSort(lista)
            matriz = lista_para_matriz(lista, n)
            print("🔽 Matriz em ordem decrescente:")
            exibir_matriz(matriz)
        elif opcao == '3':
            print("\n👋 Saindo... Obrigado por usar o Organizador de Matrizes! Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, tente novamente.")

menu()
