'''8. Faça um programa que receba n números e armazene os pares em uma lista
simplesmente encadeada e não ordenada e os ímpares em uma segunda lista
simplesmente encadeada e não ordenada. Posteriormente, o programa deve montar
uma terceira lista, duplamente encadeada e ordenada de forma crescente, com os
números das duas listas anteriores. Para finalizar, o programa deve mostrar todos os
números da terceira lista das seguintes formas:
a. Crescente.
b. Decrescente.'''

from simpleLinkedList import SimpleLinkedList 
from doublyLinkedList import DoublyLinkedList 

def main():
    even_list = SimpleLinkedList()
    odd_list = SimpleLinkedList()
    sorted_list = DoublyLinkedList()

    try:
        n = int(input("Quantos números você deseja inserir? "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return
    
    for i in range(n):
        while True:
            try:
                num = int(input(f"Insira o número {i+1}/{n}: "))
                if num % 2 == 0:
                    even_list.append(num)
                else:
                    odd_list.append(num)
                break
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

    # Inserir números das listas simples (pares e ímpares) na lista duplamente encadeada
    current = even_list.head
    while current:
        sorted_list.insert(current.data)
        current = current.next

    current = odd_list.head
    while current:
        sorted_list.insert(current.data)
        current = current.next

    print("\nLista em ordem crescente:")
    sorted_list.display()

    print("Lista em ordem decrescente:")
    sorted_list.display_reverse()

main()
