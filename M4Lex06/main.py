from orderedLinkedList import OrderedLinkedList

def cadastro():
    linkedList = OrderedLinkedList()
    continuar = "s"
    try:  
        while continuar == "s":
            nome_func = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            linkedList.insert({"name": nome_func, "salary": salario})
            continuar = input("Deseja cadastrar mais funcionários? [s/n]: ").lower()              
    except Exception as e:
        print(f"Erro: {e}, tente novamente")
        cadastro()
    
    return linkedList
    
def imprimirListaMaiorSalarios(list):
    for funcionario in list:
        print(f"Nome: {funcionario['name']}, Salário: {funcionario['salary']}")


def imprimirDados(oll: OrderedLinkedList):
    print("\nFuncionário(s) que tem maior salário:")
    imprimirListaMaiorSalarios(oll.searchHighestSalaryEmployee())
    print(f"\nMédia salarial de todos os funcionários: {oll.getAverageSalary()}")
    qtd = float(input("Digite um salário: "))
    print(f"\nQuantidade de funcionários com salário maior que o informado: {oll.requisiteC(qtd)}")


def main():
    oll = cadastro()
    oll.print()
    imprimirDados(oll)

main()

