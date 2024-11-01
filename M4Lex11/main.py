from unorderedLinkedList import UnorderedLinkedList
from unorderedLinkedListRecursive import UnorderedLinkedListRecursive

def cadastro():
    linkedList = UnorderedLinkedListRecursive() if input("Recursivo ou não? [s/n]: ").lower() == "s" else UnorderedLinkedList()
    continuar = "s"
    try:  
        while continuar == "s":
            number = int(input("Digite um número: "))
            linkedList.append(number)
            continuar = input("Deseja inserir mais números? [s/n]: ").lower()              
    except Exception as e:
        print(f"Erro: {e}, tente novamente")
        cadastro()
    
    return linkedList

def main():
    ull = cadastro()
    menor_no = ull.searchSmallestNode(ull.head, ull.head) if isinstance(ull, UnorderedLinkedListRecursive) else ull.searchSmallestNode()
    print(f"Nó com o menor número é: {menor_no}, seu número: {menor_no.data}")
    ull.print()
    ull2 = cadastro()
    ull2.print()
    igual = ull.isEqual(ull2, ull.head, ull2.head) if isinstance(ull, UnorderedLinkedListRecursive) else ull.isEqual(ull2) 
    print(igual)

main()