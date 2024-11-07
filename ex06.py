'''
6. Dada uma tabela de horários de ônibus que fazem viagens para as diversas cidades 
do Estado, escreva um programa que possibilite a localização dos horários de saída e 
de chegada quando se forneça o destino. 
'''

def buscar_horarios(destino, tabela_horarios):
    for cidade in tabela_horarios:
        if cidade == destino:
            return tabela_horarios[cidade]
    return None

def main():
    tabela_horarios = {
        "São José dos Campos": [("08:00", "09:30"), ("12:00", "13:30"), ("16:00", "17:30")],
        "Jacareí": [("08:30", "10:00"), ("12:30", "14:00"), ("16:30", "18:00")],
        "Campinas": [("07:00", "09:00"), ("11:00", "13:00"), ("15:00", "17:00")],
        "Taubaté": [("09:00", "10:30"), ("13:00", "14:30"), ("17:00", "18:30")],
        "Aparecida": [("10:00", "12:00"), ("14:00", "16:00"), ("18:00", "20:00")]    
    }  

    destino = input("Digite o destino: ")
    horarios = buscar_horarios(destino, tabela_horarios)

    if horarios:
        print(f"Horários de São Paulo para {destino}:")
        for saida, chegada in horarios:
            print(f"Saída: {saida}, Chegada: {chegada}")
    else:
        print(f"Destino '{destino}' não encontrado na tabela de horários.")

main()
