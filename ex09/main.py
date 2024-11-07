'''
9. Faça um programa que apresente o menu de opções abaixo: 
MENU 
1- Cadastrar número 
2- Mostrar números pares entre o primeiro e o último número cadastrado 
3- Excluir número 
4- Sair 
3 
Observações: 
a. O programa deve ser implementado usando uma estrutura do tipo pilha. 
b. A opção 1 do menu cadastra um número de cada vez. 
c. Mostrar mensagem para opção inválida do menu. 
d. Cuidado com o intervalo de números formado pelo primeiro e pelo último 
número da pilha, pois este pode ser crescente, decrescente ou ainda ser o 
mesmo número. 
e. Quando a opção do menu não puder ser realizada, mostrar mensagem.
''' 

from stackM import StackM

def menu():
    option = -1
    
    while(option < 0 or option > 4):
        print("\n1 - Cadastrar número.\n" + 
             "2 - Imprimir pilha.\n" +
             "3 - Mostrar números pares entre o primeiro e o último número cadastrado.\n" + 
             "4 - Excluir número.\n" +
             "0 - Sair.\n")
        option = int(input("Escolha uma opção:"))
        if(option < 0 or option > 3):
            print("\tOpção invalida. Escolha novamente.")
        
    return option

def main():
    print("### Stack ###\n")
    choice = 100
    
    myStack = StackM()
    
    while(choice != 0):
        choice = menu()
        
        if choice == 0:
            print("Saindo...\n")
            break
        
        elif choice == 1:
            myStack.push(input("Insira um número:"))
        
        elif choice == 2:
            myStack.print()
            
        elif choice == 3:
            if myStack.show_even_numbers():
                print(myStack.show_even_numbers())
            else:
                print("A pilha não possui pares")
        
        else: # choice == 4
            myStack.pop()

main()
