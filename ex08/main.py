'''
8. Faça um programa que cadastre n números em uma fila dinâmica e mais n em uma 
pilha dinâmica. Em seguida, o programa deve mostrar 3 relatórios. O primeiro terá os 
números que estão nas duas estruturas. O segundo terá os que estão apenas na fila e 
o terceiro terá os que estão apenas na pilha. 
'''

from queueM import QueueM
from stackM import StackM
from functions import common_elements, only_in_queue, only_in_stack

def main():
    queue = None
    stack = None
    
    while True:
        print("\nMenu:")
        print("1. Criar fila")
        print("2. Criar pilha")
        print("3. Imprimir fila")
        print("4. Imprimir pilha")
        print("5. Relatório 1: Números que estão nas duas estruturas")
        print("6. Relatório 2: Números que estão apenas na fila")
        print("7. Relatório 3: Números que estão apenas na pilha")
        print("8. Limpar fila e pilha")
        print("9. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            queue = QueueM()
            while True:
                number = input("Digite um número para adicionar à fila ('n' para parar): ")
                if number.lower() == 'n':
                    break
                queue.push(number)
            print("Fila criada e números adicionados.")
        elif choice == '2':
            stack = StackM()
            while True:
                number = input("Digite um número para adicionar à pilha ('n' para parar): ")
                if number.lower() == 'n':
                    break
                stack.push(number)
            print("Pilha criada e números adicionados.")
        elif choice == '3':
            if queue:
                print("Fila: ", end="")
                queue.print()
            else:
                print("A fila deve ser criada primeiro.")
        elif choice == '4':
            if stack:
                print("Pilha: ", end="")
                stack.print()
            else:
                print("A pilha deve ser criada primeiro.")
        elif choice == '5':
            result = common_elements(queue, stack)
            if result is not None:
                print("Números nas duas estruturas:", result)
        elif choice == '6':
            result = only_in_queue(queue, stack)
            if result is not None:
                print("Números apenas na fila:", result)
        elif choice == '7':
            result = only_in_stack(queue, stack)
            if result is not None:
                print("Números apenas na pilha:", result)
        elif choice == '8':
            if queue:
                queue.clear()
            if stack:
                stack.clear()
            print("Fila e pilha limpas.")
        elif choice == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
