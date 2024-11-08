'''Defina uma função chamada Insert que insere um item em uma estrutura unicamente
ligada em determinada posição. A função espera três argumentos: o item, a posição e
a estrutura ligada. (A última pode estar vazia.) A função retorna a estrutura ligada
modificada. Se a posição é maior ou igual ao comprimento da estrutura, a função
insere o item no final. Um exemplo de chamada da função, onde head é uma variável
que é uma ligação vazia ou se refere ao primeiro nó de uma estrutura, é head =
Insert(1, data, head).'''

from linkedList import LinkedList

def main():
    linked_list = LinkedList()
    
    while True:
        try:
            item = int(input("Digite o valor a ser inserido (ou -1 para sair): "))
            if item == -1:
                break
            
            position = int(input("Digite a posição para inserir o valor: "))
            linked_list.insert(position, item)
            print("\nLista atualizada:")
            linked_list.print_list()
        
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
    
    print("\n### Lista final ###")
    linked_list.print_list()

main()