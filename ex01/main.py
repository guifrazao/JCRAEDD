'''
1. Escreva um programa que use uma pilha para testar strings de entrada e determinar 
se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma 
forma de frente para trás e de trás para a frente; por exemplo, arara. 
'''

from stackM import StackM

def menu():
    opcao = -1
    
    while opcao < 0 or opcao > 5:
        print("\n1 - Inserir um novo nó na pilha.\n" + 
             "2 - Imprimir a pilha.\n" + 
             "3 - Excluir um nó da pilha.\n" +
             "4 - Verificar se é um palíndromo.\n" +
             "5 - Limpar toda a pilha.\n" + 
             "0 - Sair.\n")
        opcao = int(input("Digite sua opção:"))
        if opcao < 0 or opcao > 5:
            print("\tOpção inválida! Digite novamente.")
        
    return opcao

def main():
    print("### Palíndromo ###\n")
    escolha = 100
    
    minhaPilha = StackM()
    
    while escolha != 0:
        escolha = menu()
        
        if escolha == 0:
            print("Fechando...\n")
            break
        
        elif escolha == 1:
            minhaPilha.push(input("Digite um item:"))
            
        elif escolha == 2:
            minhaPilha.print()
        
        elif escolha == 3:
            minhaPilha.pop()
        
        elif escolha == 4:
            if minhaPilha.isPalindrome():
                print("É um palíndromo")
            else:
                print("Não é um palíndromo")
        
        else:
            minhaPilha.clear()

main()
