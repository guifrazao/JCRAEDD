from linkedList import LinkedList


def main():
    ll = LinkedList()
    while True:
        print("\nMenu de opções:")
        print("1. Inserir número na lista encadeada")
        print("2. Converter lista encadeada para vetor (iterativa)")
        print("3. Converter lista encadeada para vetor (recursiva)")
        print("4. Criar lista encadeada a partir de vetor (iterativa)")
        print("5. Criar lista encadeada a partir de vetor (recursiva)")
        print("6. Sair")
        try:
            choice = int(input("Digite sua escolha: "))
        except ValueError:
            print("Opção inválida. Digite um número entre 1 e 6.")
            continue
        
        if choice == 1:
            try:
                data = int(input("Digite o número para inserir: "))
                ll.insert(data)
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro.")
        
        elif choice == 2:
            print("Lista encadeada convertida para vetor (iterativa):", ll.to_list_iterative())
        
        elif choice == 3:
            print("Lista encadeada convertida para vetor (recursiva):", ll.to_list_recursive())
        
        elif choice == 4:
            try:
                lst = list(map(int, input("Digite os elementos do vetor separados por espaço: ").split()))
                ll.from_list_iterative(lst)
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar apenas números inteiros separados por espaço.")
        
        elif choice == 5:
            try:
                lst = list(map(int, input("Digite os elementos do vetor separados por espaço: ").split()))
                ll.from_list_recursive(lst)
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar apenas números inteiros separados por espaço.")
        
        elif choice == 6:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Escolha um número entre 1 e 6.")

main()