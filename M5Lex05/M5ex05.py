class Aviao:
    def __init__(self, nome, identificador, companhia, destino):
        self.nome = nome
        self.identificador = identificador
        self.companhia = companhia
        self.destino = destino

    def __str__(self):
        return (f"Nome: {self.nome}, ID: {self.identificador}, "
                f"Companhia: {self.companhia}, Destino: {self.destino}")

class ControlePista:
    def __init__(self):
        self.fila_decolagem = []  # Usando uma lista simples para representar a fila de decolagem
        self.identificadores = set()  # Para garantir identificadores únicos

    def listar_numero_avioes(self):
        return len(self.fila_decolagem)

    def autorizar_decolagem(self):
        if self.fila_decolagem:
            aviao = self.fila_decolagem.pop(0)  # Removendo o primeiro avião da fila (como uma fila)
            self.identificadores.remove(aviao.identificador)
            print(f"Avião {aviao.nome} (ID: {aviao.identificador}) autorizado para decolagem.")
        else:
            print("Não há aviões na fila de decolagem.")

    def adicionar_aviao(self, aviao):
        if aviao.identificador in self.identificadores:
            print("Erro: Já existe um avião com esse identificador na fila.")
        else:
            self.fila_decolagem.append(aviao)  # Adicionando o avião ao final da fila
            self.identificadores.add(aviao.identificador)
            print(f"Avião {aviao.nome} (ID: {aviao.identificador}) adicionado à fila de decolagem.")

    def listar_avioes_fila(self):
        if self.fila_decolagem:
            print("Aviões na fila de decolagem:")
            for aviao in self.fila_decolagem:
                print(aviao)
        else:
            print("Não há aviões na fila de decolagem.")

    def mostrar_primeiro_aviao(self):
        if self.fila_decolagem:
            print("Primeiro avião na fila:")
            print(self.fila_decolagem[0])  # Mostrando o primeiro avião na fila
        else:
            print("Não há aviões na fila de decolagem.")

def obter_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    controle = ControlePista()

    while True:
        print("\nControle da Pista de Decolagem")
        print("1. Listar número de aviões na fila de decolagem")
        print("2. Autorizar decolagem do primeiro avião da fila")
        print("3. Adicionar um avião à fila de espera")
        print("4. Listar todos os aviões na fila de espera")
        print("5. Mostrar características do primeiro avião da fila")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(f"Número de aviões na fila: {controle.listar_numero_avioes()}")
        elif opcao == '2':
            controle.autorizar_decolagem()
        elif opcao == '3':
            nome = input("Nome do avião: ")
            identificador = obter_inteiro("Identificador: ")
            companhia = input("Companhia aérea: ")
            destino = input("Destino: ")
            aviao = Aviao(nome, identificador, companhia, destino)
            controle.adicionar_aviao(aviao)
        elif opcao == '4':
            controle.listar_avioes_fila()
        elif opcao == '5':
            controle.mostrar_primeiro_aviao()
        elif opcao == '6':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção entre 1 e 6.")


main()
