'''
1. Escreva um programa que use uma pilha para testar strings de entrada e determinar 
se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma 
forma de frente para trás e de trás para a frente; por exemplo, arara. 
'''

from stackM import StackM

def menu():
    option = -1
    
    while(option < 0 or option > 5):
        print("\n1 - Insert a new node in the stack.\n" + 
             "2 - Print the stack.\n" + 
             "3 - Delete a node from stack.\n" +
             "4 - Check if it is a palindrome.\n" +
             "5 - Clear all stack.\n" + 
             "0 - Exit.\n")
        option = int(input("Enter your option:"))
        if(option < 0 or option > 5):
            print("\tInvalid option!Enter again.")
        
    return option

def main():
    print("### Stack's test ###\n")
    choice = 100
    
    myStack = StackM()
    
    while(choice != 0):
        choice = menu()
        
        if choice == 0:
            print("Closing...\n")
            break
        
        elif choice == 1:
            myStack.push(input("Enter a item:"))
            
        elif choice == 2:
            myStack.print()
        
        elif choice == 3:
            myStack.pop()
        
        elif choice == 4:
            if myStack.isPalindrome():
                print("It is a palindrome")
            else:
                print("It is not a palindrome")
        
        else:
            myStack.clear()

main()