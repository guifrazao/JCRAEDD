"""
6. Dada uma tabela de horários de ônibus que fazem viagens para as diversas cidades
do Estado, escreva um programa que possibilite a localização dos horários de saída e
de chegada quando se forneça o destino.

7. Implemente uma versão generalizada para busca binária numa matriz m x n.
"""
"""
def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return -1, -1

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return mid // n, mid % n
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, -1

def buscar_horarios(destino, tabela_horarios):
    destinos = list(tabela_horarios.keys())
    destinos.sort()  # Garantindo que os destinos estão ordenados
    index = binary_search_matrix([destinos], destino)  # Busca binária na lista de destinos
    if index[0] != -1:
        return tabela_horarios[destinos[index[1]]]
    return None

def buscar_destinos_por_horario(tabela_horarios, horario_busca):
    resultados = []
    
    for destino, horarios in tabela_horarios.items():
        for saida, _ in horarios:
            # Verifica se o horário de saída é exatamente igual ao horário buscado
            if saida == horario_busca:
                resultados.append(destino)
                break
    return resultados


def main():
    tabela_horarios = {
        "Santos": [("06:00", "08:00"), ("10:00", "12:00"), ("14:30", "16:30")],
        "São José dos Campos": [("08:00", "09:30"), ("12:00", "13:30"), ("16:00", "17:30")],
        "Campinas": [("07:00", "09:00"), ("11:00", "13:00"), ("15:00", "17:00")],
        "Taubaté": [("09:00", "10:30"), ("13:00", "14:30"), ("17:00", "18:30")],
        "Aparecida": [("10:00", "12:00"), ("14:00", "16:00"), ("18:00", "20:00")]
    }

    while True:
        print("\n" + "="*30)
        print("      RODOVIÁRIA SP")
        print("\n" + "="*30)
        print("      MENU DE OPÇÕES")
        print("="*30)
        print("1️⃣  Buscar horários por destino")
        print("2️⃣  Buscar destinos por horário")
        print("3️⃣  Sair")
        print("="*30)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            destino = input("\n🔍 Digite o destino desejado: ")
            horarios = buscar_horarios(destino, tabela_horarios)
            if horarios:
                print(f"\n🚌 Horários de São Paulo para **{destino}**:")
                print("-"*30)
                for saida, chegada in horarios:
                    print(f"⏰ Saída: {saida} Hrs, Chegada: {chegada} Hrs")
                print("-"*30)
            else:
                print(f"\n⚠️ Destino '{destino}' não encontrado na tabela de horários.")
        
        elif opcao == "2":
            horario_busca = input("\n🔍 Informe o horário de saída (HH:MM): ")
            destinos = buscar_destinos_por_horario(tabela_horarios, horario_busca)
            if destinos:
                print(f"\n📍 Destinos com saída às {horario_busca}:")
                print("-"*30)
                for destino in destinos:
                    print(f"🚌 {destino}")
                print("-"*30)
            else:
                print(f"\n⚠️ Nenhum destino encontrado com saída exatamente às {horario_busca}.")
        
        elif opcao == "3":
            print("\n✅ Saindo do programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

main()
"""

"""
7. Implemente uma versão generalizada para busca binária numa matriz m x n.
"""

def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return -1, -1

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return (mid // n) + 1, (mid % n) + 1
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, -1


def main():

    matrix = [
        [1, 3, 5, 6],
        [7, 9, 10, 11],
        [13, 14, 15, 17],
        [20, 23, 26, 32]
    ]

    print("=" * 40)
    print("           BUSCA EM MATRIZ           ")
    print("=" * 40)

    try:
        target = int(input("Digite um número para buscar: "))
        row, col = binary_search_matrix(matrix, target)

        if row == -1 and col == -1:
            print("\n" + "-" * 40)
            print("❌ Número não encontrado na matriz.")
            print("-" * 40)
        else:
            print("\n" + "-" * 40)
            print(f"✅ Número {target} encontrado na posição: ({row}, {col})")
            print("-" * 40)
    except ValueError:
        print("Por favor, insira um número válido.")

main()